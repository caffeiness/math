def solve(a,b,c):
    D=(b**2-4*a*c)**(1/2)
    x_1=(-b+D)/2*a
    x_2=(-b+D)/2*a

    print("x1={}".format(x_1))
    print("x2={}".format(x_2))

a=int(input())
b=int(input())
c=int(input())

solve(a,b,c)