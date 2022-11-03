a,b=map(int,input().split())
if a>b:
    a,b=b,a
for i in range(1,b+1):
    m=b*i
    if m%a==0:
        print(m)
        break