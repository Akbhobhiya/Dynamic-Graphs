class Node:
    def __init__(self,x):
        self.val = x
        self.parent = self
        self.rank = 0
        self.par=self

    def __str__(self):
        return str(self.val)

class DisjointSets: 
    def makeset(self,i):
        return Node(i)

    def union(self,i,j):

        pari=self.findset(i)
        parj=self.findset(j)
        if( pari.rank > parj.rank):
            parj.parent=pari
            parj.par=pari
            return

        if( parj.rank > pari.rank ):
            pari.parent=parj
            pari.par=parj
            return

        pari.rank+=1
        parj.parent=pari
        parj.par=pari


    def findset(self,x):

        temp=x
        while(temp.parent!=temp):
            temp=temp.parent

        while( x.parent!=x):
            t=x.parent
            x.parent=temp
            x=t
        return temp



   
def main():
    ds = DisjointSets()
    
    nodes = []
    for i in range(10):
        node = ds.makeset(i)
        nodes.append(node)

    ds.union(nodes[0],nodes[1])
    # print(ds.findset(nodes[0]))    # Should print 1
    ds.union(nodes[0],nodes[2])
    # print(ds.findset(nodes[2]))    # Should print 1
    ''' Add more tests!'''
    ds.union(nodes[3],nodes[4])
    # ds.union(nodes[4],nodes[5])
    ds.union(nodes[7],nodes[6])

    ds.union(nodes[7],nodes[3])
    print(ds.findset(nodes[4]))

    print(nodes[4].parent)

    # ds.union(nodes[6],nodes[0])
    # print(ds.findset(nodes[2]))

if __name__ == '__main__':
    main()