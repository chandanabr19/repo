n=int(input("enter the fibonacci number:"))
n1,n2=0,1
count=0
if n<=0:
    print("please enter the positive number")
elif n==1:
    print("fibonacci sequence upto",n,":")
    print(n)
else:
    print("fibonacci sequence:")
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2n2=nth
        count+=1
