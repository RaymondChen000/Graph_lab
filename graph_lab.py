class Graph:
    def __init__(self, directed=False):
       self.directed = directed
       self.vertices = [] # list of vertices 
       self.adj = {} # dict: map vertex to adj list 
       #Todo: add additional data members, for BFS, DFS
       # e.g., dict d, pred, color, ... 
       #        pre-order, post-order 
       self.d = {}
       self.pred = {}

    def add_vertex(self, v):
       if v not in self.vertices:
            self.vertices.append (v) 
       if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)

        if not self.directed:
            self.adj[v].append(u)

    def initialize_from_file(self, file_name):
        print(f"Loading graph from {file_name}")
        self.vertices = [] 
        self.adj = {} 

        try:
           f = open(file_name, "r")
        except IOError:
           print(f"Failed to open file {file_name}")
           raise

        # Read directed flag
        word = f.readline().strip()
        if word.lower() == "true":
            self.directed = True
        elif word.lower() == "false":
            self.directed = False
        else:
            raise ValueError(f"Invalid directed flag: {word}")

        print(f"The graph is directed: {word}")

        # Read number of nodes
        line = f.readline().strip()
        node_num = int(line)
        print(f"With {node_num} nodes")

        # Read node list and initialize adjacency lists
        nodes = f.readline().split()
        for u in nodes: 
            self.add_vertex (u)

        # Read edges of the form: "u label v"
        for line in f:
            parts = line.split()
            if len(parts) != 3:
                continue
            from_node, label, to_node = parts
            self.add_edge(from_node, to_node)

        f.close()


    def print(self):
        print ("Vertices:")
        print (self.vertices)

        print ("Adjacency lists:")
        # Iterate through all key value pair in the dict adj: 
        for u, adjList in self.adj.items():
            print ("Node ", u, "'s adjacency list:")
            print (adjList)

    #self is the graph, s is start node
    def BFS (self, s): 
        print ("Perform a BFS from src node", s)
        #Todo by you 
        visited=set()                       # visited is an empty array to track all visited nodes
        visited.add(s)                      # s is visited
        #use member var instead
        #d=dict() # map node to hop cnt from s, same as d={}
        #pred = dict() #map node to its predecessor node 
        self.d[s] = 0                       # distance to source is 0
        self.pred[s] = None                 # predecessor of source is none
        Q = []                              # Empty list to queue nodes 
        Q.append(s)                         # Queue source node to start bfs
        while len(Q)>0:                     # main bfps loop. keeps going if theres something in queue
            u=Q.pop(0)                      # removes the first from queue FIFO. u is the current node being processed
            for v in self.adj[u]:           # for each neighbor(v) of current node(u)
                if v not in visited:        # has to be not visited before undergoing it   
                    self.d[v] = self.d[u]+1 # distance from u to v is +1 edge
                    self.pred[v] = u        # record pred of v is u
                    visited.add (v)         # mark v as visited
                    Q.append (v)            # add v to end of queue



    # return the path in the format of a list of nodes, s, u, v, ... d 
    # If there is no path from s to do, return an emtpy list 
    def ShortestHopPath (self, s, d): 
        print ("Find shortest hop path from ", s, "to ", d) 
        # todo by you 

    # perform a DFS traversal from node s, to reach all nodes
    # reachable from s 
    def DFS (self, s): 
        print ("Perform a DFS from src node", s)
        # todo by you 

    # perform a complete DFS traversal  
    def DFS_Graph(self):
        print ("Perform a complete DFS")
        # Initialize color dictionary , visited set, pre-order list 
        # and post-order list 

        # todo by you 

 
    # Check if a directed graph has cycle or not, and 
    # return topological order ...
    def DAG_TopoSort(self):
        print ("DAG: cycle detection, topological sort")
        # Initialize color dictionary , visited set 

        # todo by you 

# Example usage
if __name__ == "__main__":
    g = Graph(directed=False)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("C", "D")

    g.print()

    
    g1 = Graph (directed=False)
    g1.initialize_from_file("dressing.txt")
    g1.print()

    g2 = Graph (directed=False)
    g2.initialize_from_file("undirected_graph.txt")
    g2.print()

    # Todo #1 Test BFS on g2 using node B as source node 
    # print out the d[], and pred[] dict after BFS() 

    # Todo #2: Find shortest hop path in g1 from one node to another 

    # Todo #3: test DFS_Graph on g1, print the pre-order and post-order 

    # Todo #4: test DFS_TopoSort on g2, print the topological order 


    # Todo #5: add an edge to g2 to make it cyclic, and test DFS_TopoSort on g2, 
    #  it should report there is a cycle 

    # Todo #6: test DFS_TopoSort 
