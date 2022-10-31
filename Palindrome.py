n=int(input())
rev=0
t=n
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
if t==rev:
    print("True")
else:
    print("False")