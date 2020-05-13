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
            print("Befor re root")
            self.printTree()
            self.__re_root(x)
            print("after re root")
            self.printTree()

        if(y):
            print("Befor re root")
            self.printTree()
            self.__re_root(y)
            print("after re root")
            self.printTree()
            
        self.printTree()
        self.printNodesStored()
        utemp=BinarySearchTree().insert_new(x)

        self.printTree()
        self.printNodesStored()
        vtemp=BinarySearchTree().insert_new(y)

        utemp.val=u
        vtemp.val=v

        self.printTree()
        self.printNodesStored()
        
        self.__add_node(u,utemp)
        self.printTree()
        self.printNodesStored()

        self.__add_node(v,vtemp)
        self.printTree()
        self.printNodesStored()

        if(not y):
            y=vtemp

        BinarySearchTree().change_root(y)

        self.printTree()
        self.printNodesStored()

        utemp.right=y
        y.par=utemp
        utemp.update()

        self.printTree()
        self.printNodesStored()

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
        bst = BinarySearchTree();
        bst.change_root(x)
        bst.change_root(y)
        
        while(x.par and x.par!=y):
            # print("X parent:" , x.par) 
            bst.rotate(x)
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
        if(x.sum_adjacent_nodes[is_treeedge]<=1):
            return -1
        while(self.adj_map[is_treeedge][x.val]==1):
            l=x.left
            r=x.right
            if(l and l.sum_adjacent_nodes[is_treeedge]>1):
                x=1
            elif(r and r.sum_adjacent_nodes[is_treeedge]>1):
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

    def printEdgeMap(self):
        for i in self.edgemap:
            print(i,":")
            print(str(self.edgemap[i].val))
    def printNodesStored(self):
        e=self
        print("------------------------")
        print("Keys inside")
        for key in e.IDtoNode:
            print(key)
            print("PArent:")
            if(e.IDtoNode[key].par):
                print(e.IDtoNode[key].par.val)
            else:
                print("None")
            print("Left:")

            if(e.IDtoNode[key].left):
                print(e.IDtoNode[key].left.val)
            else:
                print("None")

            print("Right:")

            if(e.IDtoNode[key].right):
                print(e.IDtoNode[key].right.val)
            else:
                print("None")

        print("------------------------")

    def printTree(self):
            print("------------------------------------")

            print("Tree")
            for key in self.IDtoNode:
                BinarySearchTree().printTree(self.IDtoNode[key])
                break
            print("------------------------------------")


def main():
        e = EulerTourTree();
        print("Step 1")
        e.link(1,2);
        e.printTree()
        e.printNodesStored()

        print("Step 2")
        e.link(2,3);
        e.printTree()
        e.printNodesStored()

        print("Step 3")
        e.cut(1,2)
        e.printTree()
        e.printNodesStored()    

        pass
main()