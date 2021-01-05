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
            self.input_nodes[i].value = input_values[i]
            print(self.input_nodes[i].value)
        print(self.output_nodes[0].feed_output())
        print(self.output_nodes[1].feed_output())
        print(self.output_nodes[1].value)
        return [n.feed_output() for n in self.output_nodes]

    def best_move(self):
        #Sorts the outputnodes and chooses the highest value outputnode
        sorted_moves = sorted(self.output_nodes, key=lambda x:x.value, reverse = True)
        return sorted_moves[0].move

    # def add_connection():
    # def add_node():

class Edge:
    def __init__(self, weight, innov):
        self.weight = weight
        self.innov = innov
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
