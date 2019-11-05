#possible path follow the distrinution of the middle vertical line in pascal Triangle so we will first compute it but, for how many rows?
#possible paths for 2x2 grid is at row:2 (when the first one is number 0)
#possible paths for 3x3 grid is at row:3
#possible paths for 4x4 grid is at row:4
#...
#possible paths for NxN frid is at row: N

N=20
pascalTriangle=[[1 for i in range(N+1)] for j in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        pascalTriangle[i][j]=pascalTriangle[i-1][j]+pascalTriangle[i][j-1]
for i in range(N+1):
    print(pascalTriangle[i])
    


