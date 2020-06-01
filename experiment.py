from connectivity import Connect
# from connectivity_by_dfs import Graph
from connectivity_by_dfs import Graph
from EulerTourTree import EulerTourTree
f=open('graph_input2.txt','r')

k = f.readline()
l=k.split()
n=int(l[0])
m=int(l[1])

print(n,m)

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
o.delete_edge(6,10)
g.delete_edge(6,10)
o.delete_edge(52,27)
g.delete_edge(52,27)
o.delete_edge(65,17)
g.delete_edge(65,17)

o.delete_edge(6,10)
g.delete_edge(6,10)
o.delete_edge(81,9)
g.delete_edge(81,9)

# o.is_connected(2,99)


import time	
tr=0
fl=0

start=time.time()
for i in range(1,n+1):
	for j in range(1,n+1):
		if o.is_connected(i,j) ==True:
			tr+=1
		else:
			fl+=1

print(time.time() - start,tr,fl)	


tr=0
fl=0

start=time.time()
for i in range(1,n+1):
	for j in range(1,n+1):
		if g.is_connected(i,j) ==True:
			tr+=1
		else:
			fl+=1
print(time.time()-start,tr,fl)
