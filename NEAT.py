import random as random
import copy
from main import glb_node_index, glb_innov
class Genome:
    # Connection genes connects two node genes
    # Node provide list of input, hidden_nodes and output nodes
    def __init__(self,input_nodes, hidden_nodes, output_nodes,reward):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
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
        # print(new_node.children)
        #Same weight as old connection
        old_connection = rnd_output_node.edges[rnd_index]
        new_connection = copy.deepcopy(old_connection)
        self.hidden_nodes.append(new_node)
        rnd_output_node.children.pop(rnd_index)
        rnd_output_node.children.append(new_node)

        #Dissable old connection

        #Dissable old connection
        old_connection.dissabled = True
        rnd_output_node.edges.append(new_connection)
        new_connection.innov = innov_maker(glb_node_index, new_node, rnd_output_node)
        # print(rnd_output_node.children)
        # print(rnd_output_node.edges[3].dissabled)
        # input("x")


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
        # print(self.children)
        for x in range(len(self.children)):
            child = self.children[x]
            # print(self.children)
            # print(self.edges[x], "edge")
            # print(self.is_input_node)
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

def print_agent(agent):
    print(agent.input_nodes)
    print(agent.hidden_nodes)
    print(agent.output_nodes)
    print("---------------------------------")
#Kan være at man bare trenger fra noden til output noden som du tenkte på
