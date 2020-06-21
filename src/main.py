from connectivity import Connect
# from connectivity_by_dfs import Graph
from connectivity_by_dfs import Graph
from EulerTourTree import EulerTourTree
import random
f=open('graph_input.txt','r')

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
o.delete_edge(58,15)
g.delete_edge(58,15)
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

del_edges = set()

def del_edge(e):
	global del_edges
	if e in del_edges:
		return
	o.delete_edge(e[0],e[1])
	g.delete_edge(e[0],e[1])

def del_rand_edge():
	e1 = random.randint(1,n+1)
	e2 = random.randint(1,n+1)
	while e1 == e2:
		e2 = random.randint(1,n+1)
	del_edge((e1, e2))
	return (e1, e2)

# o.is_connected(2,99)

for i in range(m//10):
	del_rand_edge()


import time	
tr=0
fl=0

print(f"Graph is present in graph_input.txt file, first line contains no.of vertices no.of edges. Following lines contain the edges")
print(f"WE ARE DELETING {m//10} RANDOM EDGES TO PROVE THE CORRECTNESS OF OUR IMPLEMENTATION.\nSO RESULTS WILL BE VARIED EVERYTIME THE PROGRAM RUNS")
print(f"\nNo. of verices in the graph - {n}")
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

print(f"Time taken by DFS - {time.time() - start} seconds")
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
print(f"Time taken by our implementation - {time.time() - start} seconds")
print(f"No. of connected and disconnected vertices - {tr} , {fl}")

g_man = []
dc = Connect()
def create_g(n):
	global g_man, dc
	g_man = [[0]*n for i in range(n)]
	dc = Connect()
	for i in range(1,n+1):
		dc.add_vertex(i)

def insert_e(u,v):
	global g_man, dc
	if g_man[u-1][v-1] == 1:
		print('Edge already exists')
		return
	g_man[u-1][v-1] = 1
	g_man[v-1][u-1] = 1
	dc.add_edge(u,v)

def del_e(u,v):
	global g_man, dc
	if g_man[u-1][v-1] == 0:
		print('Edge doesn\'t exists')
		return
	g_man[u-1][v-1] = 0
	g_man[v-1][u-1] = 0
	dc.delete_edge(u,v)

print('\nMANUAL TESTING')

c = 2
n = 0
choice_str = '\nEnter choice\n0 - QUIT\n1 - CREATE new Graph\n2 - add edge\n3 - del edge\n4 - is connected\n'
while c!=0:
	c = int(input(choice_str))

	if c == 0:
		exit()
	elif c == 1:
		n = int(input('Enter no. of vertices\n'))
		create_g(n)
		print(f"Created Graph with {n} vertices")

	elif c == 2:
		u = int(input('Enter vertex 1 of the edge to be added\n'))
		v = int(input('Enter vertex 2 of the edge to be added\n'))
		if u < 1 or u > n or v < 1 or v > n:
			print("Vertices should be between",1,n)
			continue
		insert_e(u,v)
		print(f"Added edge({u}, {v}) to the graph")

	elif c == 3:
		u = int(input('Enter vertex 1 of the edge to be deleted\n'))
		v = int(input('Enter vertex 2 of the edge to be deleted\n'))
		if u < 1 or u > n or v < 1 or v > n:
			print("Vertices should be between",1,n)
			continue
		del_e(u,v)
		print(f"Deleted edge({u}, {v}) from the graph")

	elif c == 4:
		u = int(input('Enter vertex 1 of the edge to check\n'))
		v = int(input('Enter vertex 2 of the edge to check\n'))
		if u < 1 or u > n or v < 1 or v > n:
			print("Vertices should be between",1,n)
			continue
		if dc.is_connected(u,v):
			print(f"Vertices {u} and {v} are connected")
		else:
			print(f"Vertices {u} and {v} are not connected")