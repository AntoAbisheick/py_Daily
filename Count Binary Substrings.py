s = "00110011"
count = 1
g = []
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        g.append(count)
        count = 1
g.append(count)
ans = 0
for i in range(len(g)-1):
    ans += min(g[i],g[i+1])
print(ans)