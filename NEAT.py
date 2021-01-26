import random as random
import copy
from main import glb_innov, glb_node_index
from config import c1, c2, c3
import numpy as np
class Specie:
    def __init__(self, represented, genomes):
        self.represent = None
        self.genomes = []
class Genome:
    # Connection genes connects two node genes
    # Node provide list of input, hidden_nodes and output nodes
    def __init__(self,input_nodes, hidden_nodes, output_nodes,reward):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        #Keeps track of edges in the genome
        self.reward = reward

    def feed_forward(self,input_values):
        for i in range(len(self.input_nodes)):
            # print(len(self.input_nodes))
            self.input_nodes[i].value = input_values[i]
        return [n.feed_output() for n in self.output_nodes]

    def best_move(self):
        #Sorts the outputnodes and chooses the highest value outputnode
        sorted_moves = sorted(self.output_nodes, key=lambda x:x.value, reverse = True)
        return sorted_moves[0].move

    def add_connection(self):
        all_nodes_connected = True
        for i in range(self.output_nodes):
            if self.output_nodes[i].children != self.input_nodes + self.hidden_nodes:
                all_nodes_connected = False
                break
        if not all_nodes_connected:
            while True:
                ordered_node_list = bfs(self.output_nodes, [])
                rnd_output_node_index = random.randint(len(self.output_nodes),len(ordered_node_list))
                rnd_output_node = ordered_node_list[rnd_output_node_index]
                # rnd_input_node_index = random.randint(rnd_output_node_index, len(ordered_node_list)- len(self.input_nodes))
                rnd_input_node = ordered_node_list[rnd_output_node_index]
            
                if rnd_input_node not in rnd_output_node.children:
                    rnd_output_node.children.append(rnd_input_node)
                    rnd_output_node.edges.append(Edge(random.uniform(0,1),innov_maker(glb_innov,rnd_input_node, rnd_output_node), False))
                    break
        return None

    def add_node(self):
        #Doesnt dissable child
        possible_output_nodes = self.hidden_nodes + self.output_nodes
        rnd_output_node = possible_output_nodes[random.randrange(0,len(possible_output_nodes))]
        rnd_index = random.randrange(0,len(rnd_output_node.children))
        rnd_child = rnd_output_node.children[rnd_index]
        #Is_input_node, Index, value, children, edges, move
        new_node = Node(False, innov_maker(glb_node_index,rnd_child, rnd_output_node), None, [rnd_child], [Edge(0.5,innov_maker(glb_innov,rnd_child,rnd_output_node),False)])
        #Same weight as old connection
        old_connection = rnd_output_node.edges[rnd_index]
        new_connection = copy.deepcopy(old_connection)
        #New connection
        self.hidden_nodes.append(new_node)
        rnd_output_node.children.pop(rnd_index)
        rnd_output_node.children.append(new_node)
        #Dissable old connection
        old_connection.dissabled = True
        #Adding connection to output edges
        rnd_output_node.edges.append(new_connection)
        #Giving the new connection an innovation number
        new_connection.innov = innov_maker(glb_node_index, new_node, rnd_output_node)

class Edge:
    def __init__(self, weight, innov,dissabled):
        self.weight = weight
        self.innov = innov
        self.dissabled = dissabled

class Node:
    def __init__(self, is_input_node, index, value, children, edges):
        self.is_input_node = is_input_node
        self.index = index
        self.value = value
        self.children = children
        #Edges from child to node
        self.edges = edges
        self.move = None

    def feed_output(self):
        if self.is_input_node:
            return self.value
        out_sum = 0
        for x in range(len(self.children)):
            child = self.children[x]
            out_sum += child.feed_output()*self.edges[x].weight
        self.value = out_sum
        return out_sum

#global innov
def innov_maker(glb_innov, input_node, output_node):
    key = str(input_node.index) + "_" + str(output_node.index)
    if key not in glb_innov.keys():
        value = len(glb_innov)
        glb_innov[key] = value
    else:
        value = glb_innov[key]
    return value

#Finding nodes in ordered sequence
def bfs(nodes, queue):
    nodes_on_layer = []
    for i in range(len(nodes)):
        if len(nodes[i].children) != 0:
            nodes_on_layer.append(nodes[i].children)
            queue.append(nodes[i].children)
            children = True
    if children:
        bfs(nodes_on_layer, queue)
        children = False
    else:
        return queue
def get_nodes_in_genome(a):
    return  a.hidden_nodes + a.output_nodes

def get_innovs_in_genome(nodes):
    return set([edge.innov for node in nodes for edge in node.edges])

def get_weights_innov_dict(nodes):
    return {edge.innov: edge.weight for node in nodes for edge in node.edges}
# def compare_edges2(a,b):
#     a_edges = get_weights_innov(a)
#     b_edges = get_weights_innov(b)
#     a_edges.sort(key= lambda x:x[1], reverse = False)
#     b_edges.sort(key= lambda x:x[1], reverse = False)
#     if len(a_edges) 

#     for i in range len(most_edges):
    
def compare_edges(a, b):
    a_nodes = get_nodes_in_genome(a)
    b_nodes = get_nodes_in_genome(b)

    a_edge_dict = get_weights_innov_dict(a_nodes)
    b_edge_dict = get_weights_innov_dict(b_nodes)

    a_innovs = set(a_edge_dict.keys())
    b_innovs = set(b_edge_dict.keys())

    all_genes = a_innovs.union(b_innovs)
    matching = a_innovs.intersection(b_innovs)

    list_all_genes = list(all_genes)
    list_matching = list(matching)

    excess = set([list_all_genes[i] for i in range(-1, -len(list_all_genes)) if list_all_genes[i] > list_matching[-1]])
    disjoint = all_genes - matching - excess


    sum_weight_difference = 0
    for element in matching:
       sum_weight_difference += abs(a_edge_dict[element] - b_edge_dict[element])
    avg_weight_difference = sum_weight_difference/(len(matching))
 
    return len(matching), len(disjoint), len(excess), avg_weight_difference

def distance_function(N, E, D, W, c1, c2, c3):
    distance = c1*E/N + c2*D/N + c3*W
    return distance

def make_species():
    
    return None
def genomic_distance(a,b):
    matching, disjoint, excess, avg_weight_difference = compare_edges(a,b)
    total = matching + disjoint + excess
    distance = distance_function(total, excess, disjoint, avg_weight_difference, c1, c2, c3)

    print("Disjoint ",disjoint)
    print("Matching ", matching)
    print("Excess", excess)
    print("Average", avg_weight_difference)
    return distance

def print_agent(agent):
    print(agent.input_nodes)
    print(agent.hidden_nodes)
    print(agent.output_nodes)
    print("---------------------------------")
#Kan være at man bare trenger fra noden til output noden som du tenkte på

    # a_edges_innovs = [innov for innovs in a_edges.innov]
    # b_edges_innovs = [innov for innovs in b_edges.innov]

    # matching_edges = a_edges_innovs.intersection(b_edges_innovs)

    # for a_edge in a_edges_innovs:
    #     for b_edge in b_edge_innovs:
    #         if a_edge.innov == b_edge.innov:
    #             a = "hsa"
    # longest = max(a_edges, b_edges, key = len)
    # for i in range(longest):
        
    # a_edges_sorted = sorted(a_edges, key = lambda x:x.innov, reverse = True)
    # b_edges_sorted = sorted(b_edges, key = lambda x:x.innov, reverse = True)
    # matching_genes = 
    # excess = abs(int(a_edges_sorted[0].innov) - int(b_edges_sorted[0].innov))
    # disjoint =  (len(a_edges) - len(b_edges)) - excess

    # weight_difference = sum()
    # excess = a.innov_counter - b.innov_counter