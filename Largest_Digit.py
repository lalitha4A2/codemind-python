n=int(input())
s=[]
for i in range(1,n+1):
    r=n%10
    n=n//10
    s.append(r)
print(max(s))