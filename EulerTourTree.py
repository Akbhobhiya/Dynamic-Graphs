from BinarySearchTree import BinarySearchTree,node
class EulerTourTree:
    def __init__(self):
        #<int,node*>
        self.IDtoNode={}
        #<int,set<node*>>
        self.NodeSet={}
        #<pair<int,int>,node*>
        self.edgemap={}
        #<int,int>
        self.adj_map=[{},{}]
    

    #return node params:int u
    def __get_node(self,u):
        if(not self.IDtoNode.get(u)):
            return None
        return self.IDtoNode[u]
        pass

    #return node params:int u int v
    def __get_edge(self,u,v):
        p=(u,v)
        it=self.edgemap.get(p)
        if(not it):
            return None
        return it
        pass

    #return void params:int u node nn
    def __add_node(self,u,nn):
        BinarySearchTree().change_root(nn)
        if(not self.NodeSet.get(u)):
            self.NodeSet[u]=set()
        self.NodeSet[u].add(nn)
        if(not self.IDtoNode.get(u)):
            self.IDtoNode[u]=nn
            if( u in self.adj_map[0] and u in self.adj_map[1]) :
                nn.adjacent_nodes[0]=self.adj_map[0][u]
                nn.adjacent_nodes[1]=self.adj_map[1][u]
        nn.update()
        pass

    #return void params:int u int v node nn
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
            ##TODO replace if possible with a better way to get  1st element of the set
            next=None
            for i in self.NodeSet[u]:
                next=i
                break
                        
            BinarySearchTree().change_root(nn)
            next.adjacent_nodes[0]=n0
            next.adjacent_nodes[1]=n1
            next.update()
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
        BinarySearchTree().remove_child(l)
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
        # print("Tree",u,is_treeedge)
        # print(self.adj_map)
        if(not x):
            if self.adj_map[is_treeedge].get(u)==None:
                return -1
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
        # print(self.adj_map[is_treeedge])
        if self.adj_map[is_treeedge].get(u)==None:
            self.adj_map[is_treeedge][u]=0
        self.adj_map[is_treeedge][u]+=add_adj
        # print("add adj",add_adj)
        # print(self.adj_map)
        x=self.__get_node(u)
        if(not x):
            return
        BinarySearchTree().change_root(x)
        x.adjacent_nodes[is_treeedge]+=add_adj
        x.update()
        pass

def main():
        e = EulerTourTree();
        e.link(1,2);
        e.link(2,3);
        # e.link(1,4);
        # e.link(1,3)
        e.cut(1,2)
        # print(e.edgemap)
        print(e.is_connected(2,3))



        # print(e.is_connected(2,4))
        # print("Size\n")
        # for i in range(1,8):
        #     print(str(i)+" : "+str(e.size(i)))
        # print(e.link(1,5))
        # print("IS connedcted:",e.is_connected(1,5))
        # for i in range(1,8):
        #     print(str(i)+" : "+str(e.size(i)))
        # print(e.cut(1,5))
        # print("IS connedcted:",e.is_connected(1,5))
       
        # for i in range(1,8):
        #     print(str(i)+" : "+str(e.size(i)))
main()