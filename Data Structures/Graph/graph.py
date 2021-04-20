# Recreation of a graph

# 3----4----5
# |    |    |
# 1----2    6
#  \  /
#    0

# using adjacency list (with a hash table)

class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes +=1
        return self.adjacent_list

    def add_edge(self, node1, node2):
        # undirected graph
        self.adjacent_list[node1].extend(node2)
        self.adjacent_list[node2].extend(node1)
        return self.adjacent_list
            

    def show_connections(self):
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            connections = ""

            for vertex in node_connections:
                connections += vertex + " "
            
            print(node + "-->" + connections)

        

my_graph = Graph()
my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')

my_graph.add_edge('3', '1')
my_graph.add_edge('3', '4')
my_graph.add_edge('4', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '0')
my_graph.add_edge('0', '2')
my_graph.add_edge('6', '5')

my_graph.show_connections()

