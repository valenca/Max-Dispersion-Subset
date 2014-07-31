from pprint import pprint
from math import sqrt
from sys import maxint
from copy import deepcopy
D=[0]

def dist(p1,p2):
	res = 0
	for c1,c2 in zip(p1,p2)[1:]:
		res += (c1-c2)**2
	return sqrt(res)

def closestPair(L):
	best = [dist(L[0],L[1]), (L[0],L[1]),(0,1)]
	dim = len(vector[0])
	threshold = (3**dim)-(3**(dim-1))

	def testPair(p,q,ip,iq):
		d = dist(p,q)
		if d < best[0]:
			best[0] = d
			best[1] = p,q
			best[2] = ip,iq
			
	def merge(A,B):
		i = 0
		j = 0
		while i < len(A) or j < len(B):
			if j >= len(B) or (i < len(A) and A[i][1] <= B[j][1]):
				yield A[i]
				i += 1
			else:
				yield B[j]
				j += 1

	def recur(L,ind):
		if len(L) < 2:
			return L
		split = int(len(L)/2)
		splitx = L[split][0]
		L2 = list(merge(recur(L[:split],ind), recur(L[split:],ind+split)))

		E = [p for p in L2 if abs(p[0]-splitx) < best[0]]
		for i in range(len(E)):
			for j in range(1,len(E)):
				if i+j < len(E):
					testPair(E[i],E[i+j],ind+L.index(E[i]),ind+L.index(E[i+j]))

		return L
	
	recur(L,0)
	return best

def kDispersePoints(vector,k,l,s,D):
	if k>=len(vector):
		d=closestPair(vector)[0],vector[:]
		if d[0]>=D[0]:
			D=deepcopy(d)
		return d
		
	c=closestPair(vector)
	
	ip,iq=c[2]
	p,q=c[1]

	"""
	print "Level:", l, s
	pprint(vector)
	print c
	raw_input()
	"""

	#Case 3
	if vector[ip][0] + vector[iq][0] == 2:
		return [0]

	#Case 1
	elif vector[ip][0] == 1:
		vector.pop(iq)
		rgt=kDispersePoints(vector,k,l+1,"R",D)
		vector.insert(iq,q)

	#Case 2
	elif vector[iq][0] == 1:
		vector.pop(ip)
		rgt=kDispersePoints(vector,k,l+1,"R",D)
		vector.insert(ip,p)

	#Case 0
	else:
		vector[ip][0]=1
		vector.pop(iq)
		rgt=kDispersePoints(vector,k,l+1,"R",D)
		vector.insert(iq,q)
		vector[ip][0]=0

	vector.pop(ip)
	lft=kDispersePoints(vector,k,l+1,"L",D)
	vector.insert(ip,p)

	if lft[0]>rgt[0]:
		return lft
	else :
		return rgt

if __name__ == '__main__':
	D=[0]
	def readVector():
		N=int(input())
		D=int(input())
		k=int(input())
		vector=[]
		for i in range(N):
			a=[]
			a.append(0)
			for j in range(D):
				a.append(float(input()))
			vector.append(list(a))
		return vector,k
		
	vector,k=readVector()
	vector.sort()
	print(kDispersePoints(vector,k,0,"first",D))
	#pprint(D)
