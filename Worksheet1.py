#Question1
print("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are")

#Question2
f=input("First name: ")
l=input("Last name: ")
print(l,f)

#Question3
r=float(input("Enter radius: "))
print(3.14159*r*r)

#Question4
color_list=["Red","Green","White","Black"]
print(color_list[0],color_list[-1])

#Question5
n=int(input())
print(n+n*n+n*n*n)

#Question6
x=input().split(",")
print(list(x))
print(tuple(x))

#Question7
c=float(input())
print((c*9/5)+32)

#Question8
a,b=map(int,input().split())
a,b=b,a+1
print(a,b)

#Question9
n=int(input())
print("Even" if n%2==0 else "Odd")

#Question10
y=int(input())
print("Leap" if (y%4==0 and y%100!=0) or (y%400==0) else "Not Leap")

#Question11
import math
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
print(math.dist([x1,y1],[x2,y2]))

#Question12
a,b,c=map(int,input().split())
print("Triangle" if a+b+c==180 else "Not Triangle")

#Question13
p,r,t=map(float,input().split())
print(p*((1+r/100)**t -1))

#Question14
n=int(input())
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

#Question15
N=int(input())
print(sum(i*i for i in range(1,N+1)))
