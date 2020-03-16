class node:
    def __init__(self):
        self.left=None
        self.right=None
        self.par=None

        self.val=0
        
        #size of subtree
        self.size=1
        
        #[2]  no. of adjacent nodes in graph in fully dynamic-tree(1) and non -tree(0)
        self.adjacent_nodes=[0,0] 

        #[2] sum of adjacent_nodes in subtree
        self.sum_adjacent_nodes=[0,0] 
        
    def update(self):
        self.size=1
        self.sum_adjacent_nodes[0]=self.adjacent_nodes[0]
        self.sum_adjacent_nodes[1]=self.adjacent_nodes[1]

        if(self.left):
            self.size+=self.left.size
            self.sum_adjacent_nodes[0]+=self.left.sum_adjacent_nodes[0]
            self.sum_adjacent_nodes[1]+=self.left.sum_adjacent_nodes[1]

        if(self.right):
            self.size+=self.right.size
            self.sum_adjacent_nodes[0]+=self.right.sum_adjacent_nodes[0]
            self.sum_adjacent_nodes[1]+=self.right.sum_adjacent_nodes[1]    

        pass


class BinarySearchTree:
    def __init__(self):
        pass
    #node nn
    def rotate(self,nn):
        p=nn.par
        if(not p):
            return
        if(nn==p.left):
            __rotate_right(nn)
        else:
            __rotate_left(nn)
        pass
    
    #node nn
    def delete_node(self,nn):
        self.change_root(nn)
        l=nn.left
        r=nn.right

        if(not l and not r):
            return
        elif(not l):
            self.remove_child(r)
        elif(not r):
            self.remove_child(l)
        else:
            self.remove_child(l)
            self.remove_child(r)
            newroot=self.leftmost(r)
            newroot.left=l
            newroot.update()

        pass

    #node nn
    def change_root(self,nn):
        if(not nn):
            return
        while(nn.par):
            p=nn.par
            gp=p.par
            if(not gp):
                self.rotate(nn)
                break
            if((nn==p.left) == (p==gp.left)):
                #left-left
                self.rotate(p)
                #right-right  
                self.rotate(nn)
            else:
                #zig-zig
                self.rotate(nn)
                self.rotate(nn)
                
        pass

    #node nn
    def remove_child(self,nn):
        p=nn.par
        if(not p):
            return
        if(nn==p.left):
            p.left=None
        else:
            p.right=None
        nn.par=None
        p.update()
        pass

    #node nn
    def leftmost(self,nn):
        self.change_root(nn)
        while(nn.left):
            nn=nn.left
        self.change_root(nn)
        return nn
        pass

    #node nn
    def rightmost(self,nn):
        self.change_root(nn)
        while(nn.right):
            nn=nn.right
        self.change_root(nn)
        return nn
        pass

    #node nn
    def next_in_seq(self,nn):
        self.change_root(nn)
        nn=nn.right
        if(not nn):
            return None
        while(nn.left):
            nn=nn.left
        self.change_root(nn)
        return nn
        pass

    #node nn
    def insert_new(self,nn):
        if(not nn):
            return node()
        
        self.change_root(nn)
        
        while(nn.right):
            nn=nn.right
        
        newnode=node()
        newnode.par=nn
        nn.right=newnode
        nn.update()

        self.change_root(newnode)

        return newnode

        pass

    #static functions
    #node nn
    def __rotate_right(nn):
        p=nn.par
        gp=p.par
        rc=nn.right
        nn.par=gp
        if(gp):
            if(p==gp.left):
                gp.left=nn
            else:
                gp.right=nn
        nn.right=p
        p.par=nn
        p.left=rc
        if(rc):
            rc.par=p

        p.update()
        nn.update()
        pass
    def __rotate_left(nn):
        p=nn.par
        gp=p.par
        lc=nn.left

        nn.par=gp

        if(gp):
            if(p==gp.left):
                gp.left=nn
            else:
                gp.right=nn

        nn.left=p
        p.par=nn

        p.right=lc

        if(lc):
            lc.par=p

        p.update()
        nn.update()
        pass
    def __str__(self):
        if()
 def main():
