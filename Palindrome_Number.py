t=int(input())
for i in range(t):
    n=int(input())
    rev=0
    s=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if s==rev:
        print("True")
    else:
        print("False")
        
        