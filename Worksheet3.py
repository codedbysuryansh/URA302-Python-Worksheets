#Question1
def diff17(n): return abs(n-17)*2 if n>17 else 17-n
print(diff17(22),diff17(14))

#Question2
def test_range(n): return (100<=n<=1000) or n==2000
print(test_range(500),test_range(1500))

#Question3
def rev(s): return s[::-1]
print(rev("robot"))

#Question4
def count_case(s):
    return {"UPPER":sum(1 for c in s if c.isupper()),"LOWER":sum(1 for c in s if c.islower())}
print(count_case("RoBot"))

#Question5
def distinct(l): return list(set(l))
print(distinct([1,2,2,3,4,4]))

#Question6
def evens(l): return [i for i in l if i%2==0]
print(evens([1,2,3,4,5,6,7,8,9]))

#Question7
def robot():
    def move(): print("Robot is moving")
    move()
robot()

#Question8
def student(name,age,course): pass
print(student.__code__.co_varnames[:student.__code__.co_argcount])

#Question9
def move_robot(x,y,d):
    if d=="up":y+=1
    elif d=="down":y-=1
    elif d=="left":x-=1
    elif d=="right":x+=1
    return (x,y)
print(move_robot(0,0,"up"))

#Question10
def classify_temperature(t):
    if t<15:return "Cold"
    elif t<=30:return "Moderate"
    else:return "Hot"
print(classify_temperature(10),classify_temperature(25),classify_temperature(35))

#Question11
def is_goal_reached(path):
    x=y=0
    for p in path:
        if p=="up":y+=1
        elif p=="down":y-=1
        elif p=="left":x-=1
        elif p=="right":x+=1
    return (x,y)==(2,0)
print(is_goal_reached(["up","right","right","down"]))

#Question12
class Student:
    def __init__(self,id,name,cls): self.student_id=id;self.student_name=name;self.student_class=cls
    def display(self): print(vars(self))
s=Student(1,"John","CS")
s.display()

#Question13
class Student:
    def __init__(self,id,name,cls): self.student_id=id;self.student_name=name;self.student_class=cls
student1=Student(1,"A","Math")
student2=Student(2,"B","Bio")
print(vars(student1))
print(vars(student2))

#Question14
import math
class Circle:
    def __init__(self,r): self.r=r
    def area(self): return math.pi*self.r**2
    def perimeter(self): return 2*math.pi*self.r
c=Circle(5)
print(c.area(),c.perimeter())

#Question15
class String:
    def get_String(self): self.s=input()
    def print_String(self): print(self.s.upper())
st=String()
#st.get_String();st.print_String()

#Question16
class Robot:
    def __init__(self,name,task): self.name=name;self.task=task;self.battery_level=100
    def perform_task(self): print(self.task,"in progress");self.battery_level-=10
    def recharge(self): self.battery_level=100
    def status(self): print(self.name,self.task,self.battery_level)
r=Robot("Robo1","Cleaning")
r.perform_task();r.status();r.recharge();r.status()