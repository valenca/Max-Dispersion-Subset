def dist(p1,p2):
	res = 0
	for c1,c2 in zip(p1,p2):
		res += (c1-c2)**2
	return res**0.5

def closestPair(L,dp):
	best = [dist(L[0],L[1]),[L[0],L[1]],(0,1)]
	for i in range(len(L)):
		for j in range(i+1,len(L)):
			if dist(L[i],L[j]) < best[0]:
				best = [dist(L[i],L[j]),[L[i],L[j]],(i,j)]
		
	return best

def kDispersePoints(vector,k,dp):
	try:
		return dp[tuple(vector)]
	except KeyError:
		pass

	if k>=len(vector):
		dp[tuple(vector)]=closestPair(vector,dp)[0],vector[:]
		return dp[tuple(vector)]
	else:
		ip,iq=closestPair(vector,dp)[2]

		p=vector.pop(ip)
		bp=kDispersePoints(vector,k,dp)
		vector.insert(ip,p)

		q=vector.pop(iq)
		bq=kDispersePoints(vector,k,dp)
		vector.insert(iq,q)

		if bq[0]>bp[0]:
			dp[tuple(vector)] = bq;	
			return bq
		else :
			dp[tuple(vector)] = bp;	
			return bp

if __name__ == '__main__':
	def readVector():
		N=int(input())
		D=int(input())
		k=int(input())
		vector=[]
		for i in range(N):
			a=[]
			for j in range(D):
				a.append(float(input()))
			vector.append(tuple(a))
		return vector,k
			
	vector,k=readVector()
	vector.sort()
	print(kDispersePoints(vector,k,dict()))
