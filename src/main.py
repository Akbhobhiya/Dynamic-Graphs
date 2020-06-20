from connectivity import Connect
# from connectivity_by_dfs import Graph
from connectivity_by_dfs import Graph
from EulerTourTree import EulerTourTree
import random
f=open('graph_input2.txt','r')

k = f.readline()
l=k.split()
n=int(l[0])
m=int(l[1])



o=Connect()
g=Graph()
for i in range(n+1):
	o.add_vertex(i)
	g.add_vertex(i)

flag=1
i=0

for k in f:
	if flag==1:
		flag=0
		continue
	# print(k)
	i+=1
	# print(i)
	l=k.split()
	# print(l)
	u=int(l[0])
	v=int(l[1])
	o.add_edge(u,v)
	g.add_edge(u,v)


	
# print(o.delete_edge(58,15))
# o.delete_edge(58,15)
# g.delete_edge(58,15)
# o.delete_edge(6,10)
# g.delete_edge(6,10)
# o.delete_edge(52,27)
# g.delete_edge(52,27)
# o.delete_edge(65,17)
# g.delete_edge(65,17)

# o.delete_edge(6,10)
# g.delete_edge(6,10)
# o.delete_edge(81,9)
# g.delete_edge(81,9)

def del_edge(e):
	if e in del_edges:
		return
	o.delete_edge(e)

def rand_edge():
	e1 = random.randint(1,n+1)
	e2 = random.randint(1,n+1)
	while e1 == e2:
		e2 = random.randint(1,n+1)
	del_edge((e1, e2))
	return (e1, e2)

# o.is_connected(2,99)


import time	
tr=0
fl=0

print(f"No. of verices in the graph - {n}")
print(f"No. of edges in the graph - {m}")
print()
print('Running is_connected query on all vertices with one another using DFS(Naive algorithm)')
start=time.time()
for i in range(1,n+1):
	for j in range(1,n+1):
		if g.is_connected(i,j) ==True:
			tr+=1
		else:
			fl+=1

print(f"Time taken by DFS - {time.time() - start}")
print(f"No. of connected and disconnected vertices - {tr} , {fl}")	
print()

tr=0
fl=0
print('Running is_connected query on all vertices with one another using Eulertour tree method')
start=time.time()
for i in range(1,n+1):
	for j in range(1,n+1):
		if o.is_connected(i,j) ==True:
			tr+=1
		else:
			fl+=1
print(f"Time taken by our implementation - {time.time() - start}")
print(f"No. of connected and disconnected vertices - {tr} , {fl}")
