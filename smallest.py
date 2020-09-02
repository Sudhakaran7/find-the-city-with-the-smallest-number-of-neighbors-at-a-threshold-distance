class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        dist = [[float("inf")]*n for _ in range(n)]
        for i in range(n):
            dist[i][i]= 0
        
        for edge in edges:
            i,j,w = edge
            dist[i][j] = w
            dist[j][i] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
        
        d = {i:sum([d <= distanceThreshold for d in dist[i]])  for i in range(n)}
        return min(range(n), key = lambda x: (d[x],-x))
val=Solution()
n,m,k=map(int,input().split())
matrix=[]
for i in range(n):
  rows=list(map(int,input().split()))
  matrix.append(rows)
print(val.findTheCity(m,matrix,k))
