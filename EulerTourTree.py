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
        else:
            ##TODO get 1st element of the set
            next=self.NodeSet[u].begin()#change here
            BinarySearchTree().change_root(nn)
            next.adjacent_nodes[0]=n0
            next.adjacent_nodes[1]=n1
            next.update

    
        pass
    def __remove_edge(self,u,v):
        p=(u,v)
        del self.edgemap[p]
        pass
    def __re_root(self,nn):
        BinarySearchTree().change_root(nn)
        if(not nn.left):
            return
        l=nn.left
        front=BinarySearchTree().leftmost(l)
        front.left=nn
        nn.par=front
        front.update()
        BinarySearchTree().change_root(nn)

        pass



    def link(self,u,v):
        if(self.is_connected(u,v)):
            return False
        x=self.__get_node(u)
        y=self.__get_node(v)
        if(x):
            self.__re_root(x)
        if(y):
            self.__re_root(x)
        utemp=BinarySearchTree().insert_new(x)
        vtemp=BinarySearchTree().insert_new(y)
        utemp.val=u
        vtemp.val=v

        self.__add_node(u,utemp)
        self.__add_node(v,vtemp)

        if(not y):
            y=vtemp
        BinarySearchTree().change_root(y)
        utemp.right=y
        y.par=utemp
        utemp.update()

        self.__add_edge(u,v,utemp)
        self.__add_edge(v,u,vtemp)
        return True
        pass
    def cut(self,u,v):
        x=self.__get_edge(u,v)
        if(not x):
            return False
        y=self.__get_edge(v,u)
        self.__re_root(x)
        BinarySearchTree().change_root(y)
        while(x.par!=y):
            BinarySearchTree().rotate(x)
        BinarySearchTree().remove_child(x)

        next=BinarySearchTree().next_in_seq(y)
        if(next):
            temp=next.val
            t=BinarySearchTree().rightmost(next)
            self.__remove_edge(v,temp)
            self.__add_edge(v,temp,t)

        self.__remove_node(u,x)
        self.__remove_node(v,y)
        self.__remove_edge(u,v)
        self.__remove_edge(v,u)
        BinarySearchTree().delete_node(x)
        BinarySearchTree().delete_node(y)
        return True
        pass

    def is_connected(self,u,v):
        if(u==v):
            return True
        x=self.__get_node(u)
        y=self.__get_node(v)
        if(not x or not y):
            return False
        BinarySearchTree().change_root(x)
        BinarySearchTree().change_root(y)

        while(x.par and x.par!=y):
            BinarySearchTree().rotate(x)
        return x.par==y

        pass
    def size(self,u):
        x=self.__get_node(u)
        if(not x):
            return 1
        BinarySearchTree().change_root(x)
        return (x.size)/2+1
        
        pass
    def get_adjacent(self,u,is_treeedge):
        x=self.__get_node(u)
        if(not x):
            if(self.adj_map[is_treeedge][u]>0):
                return u
            else:
                return -1
        BinarySearchTree().change_root(x)
        if(x.sum_adjacent_nodes[is_treeedge]<=0):
            return -1
        while(self.adj_map[is_treeedge][x.val]==0):
            l=x.left
            r=x.right
            if(l and l.sum_adjacent_nodes[is_treeedge]>0):
                x=1
            elif(r and r.sum_adjacent_nodes[is_treeedge]>0):
                x=r
        BinarySearchTree().change_root(x)
        return x.val


        pass
    def update_adjacent(self,u,add_adj,is_treeedge):
        self.adj_map[is_treeedge][u]+=add_adj
        x=self.__get_node(u)
        if(not x):
            return
        BinarySearchTree().change_root(x)
        x.adjacent_nodes[is_treeedge]+=add_adj
        x.update()
        pass