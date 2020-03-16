from BinarySearchTree import BinarySearchTree,node
class EulerTourTree:
    def __init__(self):
        #<int,node*>
        self.IDtoNode={}
        #<int,set<node*>>
        self.NodeSet={}
        #<pair<int,int>,node*,hash_pair>
        self.edgemap={}
        #<int,int>
        self.adj_map=[{},{}]
    
    def link(self,u,v):
        pass
    def cut(self,u,v):
        pass
    def is_connected(self,u,v):
        pass
    def size(self,u):
        pass
    def get_adjacent(self,u,is_treeedge):
        pass
    def update_adjacent(self,u,add_adj,is_treeedge):
        pass

    def __get_node(self,u):
        if(not self.IDtoNode.get(u)):
            return None
        return self.IDtoNode[u]
        pass

    ##TODO Check
    def __get_edge(self,u,v):
        p=(u,v)
        it=self.edgemap.get(p)
        if(it==self.edgemap.end()):#TODO change to get last element of the dictionary.Although doesnt make sense as the cpp code has an unordered map
            return None
        return it[1]
        pass
    def __add_node(self,u,nn):
        BinarySearchTree().change_root(nn)
        self.NodeSet[u].add(nn)
        if(not self.IDtoNode.get(u)):
            self.IDtoNode[u]=nn
            nn.adjacent_nodes[0]=self.adj_map[0][u]
            nn.adjacent_nodes[1]=self.adj_map[1][u]
        nn.update()
        pass

    def __add_edge(self,u,v,nn):
        p=(u,v)
        self.edgemap[p]=nn
        pass

    def __remove_node(self,u,nn):
        n0=nn.adjacent_nodes[0]
        n1=nn.adjacent_nodes[1]
        self.NodeSet[u].remove(nn)
        if(len(self.NodeSet[u])==0):
            del self.IDtoNode[u]


    
        pass
    def __remove_edge(self,u,v):
        pass
    def __re_root(self,nn):
        pass