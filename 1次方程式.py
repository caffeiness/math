eq=input().rstrip(" ")
EQ=eq.split("=")

a=EQ[0]
A=a.split(" ")
num=(A[0])
sign=(A[1])
num2=(A[2])

b=EQ[1]   #右辺
count=0 

if "x" in b :
    
    if sign=="+":
        count=int(int(num)+int(num2))
    elif sign=="-":
        count=int(int(num)+int(num2))
    print(count)

else:
    if num=="x":
        if sign=="+":
            count=int(int(b)-int(num2))
        elif sign=="-":
            count=int(int(b)+int(num2))
    elif  num2=="x":
        if sign=="+":
            count=int(int(b)-int(num))
        elif sign=="-":
            count=-1*int(int(b)-int(num))
    print(count)
