import sys

def robot_movement(grid) :

    dp=[]

    for i in range(0,len(grid)+1) :
        dp.append([0]*(len(grid)+1))

    i=len(grid)-1
    j=len(grid)-1

    while i>=0 and i<len(grid)-1 :
        while j>=0 and j<len(grid)-1 :

            if dp[i+1][j]!=1 :
                dp[i][j]+=dp[i+1][j]

            if dp[i][j+1]!=1 :
                dp[i][j]+=dp[i][j+1]


            j-=1

        i-=1

    return dp[0][0]


grid=[]
for line in sys.stdin.readline() :
    l=map(int,line.strip().split())
    grid.append(l)

print robot_movement(grid)
