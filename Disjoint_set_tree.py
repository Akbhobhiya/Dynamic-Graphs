from Disjoint_sets import DisjointSets
class Tree:

	def __init__(self):
		self.ds = DisjointSets()
		self.nodes = []
		self.adj = []

	def add_node(self,i):
		self.nodes.append(self.ds.makeset(i))
		self.adj.append([])

	def link(self,u,v):
		self.ds.union(self.nodes[u],self.nodes[v])
		self.adj[u].append(v)
		self.adj[v].append(u)


	def cut(self,u,v):
		pa = u
		child = v
		# print(self.nodes[u].par,self.nodes[v])

		if(self.nodes[u].par == self.nodes[v]):
			# print("S")
			child = u
			pa = v
		self.adj[pa].remove(child)

		self.adj[child].remove(pa)
		self.nodes[child].par = self.nodes[child]
		self.nodes[child].parent = self.nodes[child]

		# print(self.nodes[child].par,self.nodes[pa].par)
		l = [child]
		visited = [0 for _ in range(len(self.nodes))]
		visited[child] = 1
		while len(l)>0:

			t = l[-1]
			l.pop()
			for vertices in self.adj[t]:
				# print("S")
				if visited[vertices] == 1:
					continue
				self.nodes[vertices].parent = self.nodes[child]
				visited[vertices] = 1
				l.append(vertices)

	def is_connected(self,u,v):
		if self.ds.findset(self.nodes[u])==self.ds.findset(self.nodes[v]):
			return True
		return False
	def __str__(self):
		for i in range(len(self.nodes)):
			print(self.nodes[i],self.adj[i])
		return ""

def main():
	T = Tree()
	T.add_node(0)
	T.add_node(1)
	T.add_node(2)
	T.add_node(3)
	T.add_node(4)
	T.link(0,1)
	T.link(0,2)
	T.link(0,3)
	T.link(3,4)
	T.cut(0,3)
	T.link(0,4)
	T.cut(4,0)
	print(T)
	print(T.is_connected(0,4))

main()
