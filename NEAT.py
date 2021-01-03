class Genome:
    # Connection genes connects two node genes
    # Node provide list of input, hidden and output nodes
    def __init__(self,inputs, hidden, outputs, edges, reward):
        self.inputs = inputs
        self.hidden = hidden
        self.outputs = outputs
        self.edges = edges
        self.reward = reward
    def dfs(self, current_node,visited, parent):
        # dfs approach. Checking every
        children = current_node.children
        for child in children:
            if child not in visited:
                visited.append(child)
                parent = current_node
                self.dfs(child,visited,parent)
    def feed_forward(self):
        #Loops through every output and dfs
        for i in range(len(self.outputs)):
            visited= []
            self.dfs(self.outputs[i], visited, None)
            visited.clear()
        sorted_moves = sorted(self.outputs, key=lambda x:x.value, reverse = True)
        return sorted_moves[0].move


    def feed_observation(self,obs):
        for i in range(len(self.inputs)):
            self.inputs[i].value = obs[0][i]

    def feed_value(self,current_node,parent):
        for edge in self.edges:
            if edge.in_node == current_node.index and edge.out_node == parent.index:
                parent.value += edge.weight*current_node.value
        


        
    # def add_connection():
    # def add_node():

class Edge:
    def __init__(self, in_node, out_node, weight, innov):
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.innov = innov
class Node:
    def __init__(self, index, value, children,move):
        self.index = index
        self.value = value
        self.children = children
        self.move = move


#Under
        # if current_node not in self.inputs:
        #     activation_fun()
        # feed_value(current_node,parent)
        # if (current_node.children =! []) and (child not in visited):
        #     children = current_node.children
        #     child = children.pop()
        #     if child not in visited:
        #         visited.append(child)
        #         feed_output(child)
        # if current_node in self.inputs: