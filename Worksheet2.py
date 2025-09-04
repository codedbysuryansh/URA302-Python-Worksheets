#Question1(i-xii)
L=[11,12,13,14]
L.append(50);L.append(60);print(L)
L.remove(11);L.remove(13);print(L)
L.sort();print(L)
L.sort(reverse=True);print(L)
print(13 in L)
print(len(L))
print(sum(L))
print(sum(i for i in L if i%2))
print(sum(i for i in L if i%2==0))
def isprime(n): 
    if n<2:return False
    for j in range(2,int(n**0.5)+1):
        if n%j==0:return False
    return True
print(sum(i for i in L if isprime(i)))
L.clear();print(L)
del L

#Question2
a=[1,2,3,4]
s=0
for i in a:s+=i
print(s)

#Question3
a=[1,2,3,4]
m=1
for i in a:m*=i
print(m)

#Question4
a=[[["*" for k in range(6)]for j in range(4)]for i in range(3)]
print(a)

#Question5(i-vii)
D={1:5.6,2:7.8,3:6.6,4:8.7,5:7.7}
D[8]=8.8;print(D)
D.pop(2);print(D)
print(6 in D)
print(len(D))
print(sum(D.values()))
D[3]=7.1;print(D)
D.clear();print(D)

#Question6(i-vi)
S1={10,20,30,40,50,60}
S2={40,50,60,70,80,90}
S1.update([55,66]);print(S1)
S1.discard(10);S1.discard(30);print(S1)
print(40 in S1)
print(S1|S2)
print(S1&S2)
print(S1-S2)

#Question7(i)
import random,string
for _ in range(100):
    print("".join(random.choice(string.ascii_letters) for i in range(random.randint(6,8))))

#Question7(ii)
for n in range(600,801):
    if isprime(n):print(n)

#Question7(iii)
for n in range(100,1001):
    if n%7==0 and n%9==0:print(n)

#Question8
exam_st_date=(11,12,2025)
print("The examination will start from: %i / %i / %i"%exam_st_date)

#Question9
nums=[10,15,23,45,60]
for i in nums:
    if i%5==0:print(i)

#Question10
n=int(input())
is_even=(n%2==0)
print("Even" if is_even else "Odd")

#Question11
s="Emma is good. Emma likes python. Emma"
print(s.count("Emma"))

#Question12
l1=[1,2,3,4,5]
l2=[10,11,12,13,14]
new=[i for i in l1 if i%2]+[j for j in l2 if j%2==0]
print(new)

#Question13
positions=[(2,3),(4,5),(6,7),(7,8)]
print([p for p in positions if p[0]%2==0])

#Question14
sensor_data={1:2.3,2:4.5,3:1.8,4:3.6}
print([k for k,v in sensor_data.items() if v>3.0])

#Question15
commands_received={"MOVE","TURN_LEFT","TURN_RIGHT","STOP"}
commands_executed={"MOVE","TURN_LEFT","STOP"}
print(commands_received-commands_executed)