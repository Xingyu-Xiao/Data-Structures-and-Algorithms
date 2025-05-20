n = int(input())
ans = 0


def dfs(stack=[],i=0,j=0):
    global ans
    if i == n:
        ans += 1
        return
    if stack:
        new_stack1 = stack[:len(stack)-1]
        dfs(new_stack1,i+1,j)
    if j < n:
        dfs(stack+[j],i,j+1)


dfs()
print(ans)
