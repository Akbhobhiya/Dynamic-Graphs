from EulerTourTree import EulerTourTree as Tree
from collections import defaultdict
def multi_dict():
	return defaultdict(lambda: multi_dict(1, int))
class Connect:

	def __init__(self):
		self.vertices=set()
		self.spf=[]
		self.adj = [{}]
		self.treeadj = multi_dict()
		self.edge_level=multi_dict()
		self.exists={}

	def add_vertex(self,u):
		self.vertices.add(u)
		self.spf.append(Tree())
		self.exists[u]=1
		# adj.append({})

	def add_edge(self,u,v):
		self.edge_level[(u,v)]=[]
		if self.exists.get(u)==None or self.exists.get(v)==None:
			return False

		if not (self.spf[0].is_connected(u,v)):
			self.spf[0].link(u,v)
			self.add_edge_level(u,v,0,True)
		else :
			self.spf[0].link(u,v)
			self.add_edge_level(u,v,0,False)

		# self.treeadj[u][v]=[]
		# pass
	def delete_edge(self,u,v):
		if self.exists.get(u)==None or self.exists.get(v)==None:
			return False
		lvl = self.level(u,v)
		if lvl ==-1 :
			return False
		if not(self.spf[0].cut(u,v)):
			self.remove_edge_level(u,v,lvl,False)
			return True

		self.remove_edge_level(u,v,lvl,True)

		i=lvl 
		while(i>=0):
			if self.spf[i].size(u) > self.spf[i].size(v):
				t=u
				u=v
				v=t 
			while True:
				x=self.spf[i].get_adjacent(u,True)
				if x==-1:
					break
				while len(self.treeadj[i][x])>0:
					y= self.treeadj[i][x][0]
					self.remove_edge_level(x,y,i+1,True)
					self.add_edge_level(x,y,i+1,True)
					self.spf[i+1].link(x,y)

			ff= False
			while ff==False :
				x= self.spf[i].get_adjacent(u,False)
				if x==-1:
					break 
				while len(self.adj[i][x])>0 :
					y=adj[i][x][0]
					if self.spf[i].is_connected(u,v):
						for j in range(i+1):
							self.spf[j].link(x,y)
						ff= True
						self.remove_edge_level(x,y,i,False)
						self.add_edge_level(x,y,i+1,False)

			if ff:
				break
			i=i-1
		return True

	def is_connected(self,u,v):
		if self.exists.get(u)==None or self.exists.get(v)==None:
			return False
		if u==v:
			return True
		return self.spf[0].is_connected(u,v)

	def add_edge_level(self,u,v,level,is_treeedge):
		# pass
		if u > v:
			t=u
			u=v
			v=t 
		self.edge_level[(u,v)].append(level)

		if is_treeedge:
			if self.treeadj[level][u]==None:
				self.treeadj[level][u]=[v]
			else:
				self.treeadj[level][u].append(v)
			if self.treeadj[level][v]==None:
				self.treeadj[level][v]=[u]
			else:
				self.treeadj[level][v].append(u)

			# pass
		else :
			if self.adj[level][u]==None:
				self.adj[level][u]=[v]
			else:
				self.adj[level][u].append(v)
			if self.adj[level][v]==None:
				self.adj[level][v]=[u]
			else:
				self.adj[level][v].append(u)

			# pass
		self.spf[level].update_adjacent(u,-1,is_treeedge)
		self.spf[level].update_adjacent(v,-1,is_treeedge)


	def remove_edge_level(self,u,v,level,is_treeedge):
		# pass 
		if u > v:
			t=u
			u=v
			v=t
		self.edge_level[(u,v)].remove(level)

		if is_treeedge:
			self.treeadj[level][u].remove(v)
			self.treeadj[level][v].remove(u)
		else :
			self.adj[level][u].remove(v)
			self.adj[level][v].remove(u)

		self.spf[level].update_adjacent(u,-1,is_treeedge)
		self.spf[level].update_adjacent(v,-1,is_treeedge)


	def level(self,u,v): #done
		if u > v:
			t=u
			u=v
			v=t 
		# self.edge_level[[u,v]]
		if self.edge_level.get((u,v))==None:
			return -1 
		return self.edge_level[[u,v]]

def main():
	o = Connect()
	o.add_vertex(0)
	o.add_vertex(1)
	o.add_edge(0,1)
	# print(o.is_connected(0,1))
	# o.delete_edge(0,1)
main()