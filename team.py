n=int(input())
a=0
for i in range(n):
    p=list(map(int,input().split()))
    if sum(p)>=2:
        a+=1
print(a)