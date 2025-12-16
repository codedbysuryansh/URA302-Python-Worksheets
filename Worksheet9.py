import tkinter as tk
import math

#Question1
root = tk.Tk()
root.title("Robot Control Panel")
root.geometry("500x400")
root.configure(bg="yellow")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

#Question2
canvas.create_oval(98, 98, 102, 102, fill="black")

#Question3
path_points = [20,50, 100,120, 180,90, 250,150]
canvas.create_line(path_points, fill="blue", width=3)

#Question4
x = 10
y = 50
pt = canvas.create_oval(x, y, x+10, y+10, fill="red")

def move_point():
    global x
    if x < 480:
        canvas.move(pt, 5, 0)
        x += 5
        root.after(100, move_point)

move_point()

#Question5
canvas.create_rectangle(300, 250, 360, 300, fill="gray")
canvas.create_oval(305, 300, 325, 320, fill="black")
canvas.create_oval(335, 300, 355, 320, fill="black")

#Question6
robot = canvas.create_oval(50, 150, 70, 170, fill="green")

def move(dx, dy):
    canvas.move(robot, dx, dy)

tk.Button(root, text="Up", command=lambda: move(0, -10)).pack()
tk.Button(root, text="Down", command=lambda: move(0, 10)).pack()
tk.Button(root, text="Left", command=lambda: move(-10, 0)).pack()
tk.Button(root, text="Right", command=lambda: move(10, 0)).pack()

#Question7
bx, by = 200, 100
vx, vy = 4, 4
ball = canvas.create_oval(bx-15, by-15, bx+15, by+15, fill="purple")

def bounce():
    global bx, by, vx, vy
    bx += vx
    by += vy
    if bx <= 15 or bx >= 485:
        vx = -vx
    if by <= 15 or by >= 385:
        vy = -vy
    canvas.coords(ball, bx-15, by-15, bx+15, by+15)
    root.after(50, bounce)

bounce()

#Question8
rx = 50
line_robot = canvas.create_oval(rx-10, 200, rx+10, 220, fill="blue")

def move_line():
    global rx
    if rx < 450:
        rx += 3
        canvas.coords(line_robot, rx-10, 200, rx+10, 220)
        root.after(50, move_line)

move_line()

#Question9
A = (150, 300)
D = (400, 300)

L2 = 120
L3 = 150
L4 = 130
theta = math.radians(30)

Bx = A[0] + L2 * math.cos(theta)
By = A[1] - L2 * math.sin(theta)
B = (Bx, By)

# Circle intersection to find C
dx = D[0] - B[0]
dy = D[1] - B[1]
d = math.hypot(dx, dy)

a = (L3**2 - L4**2 + d**2) / (2*d)
h = math.sqrt(L3**2 - a**2)

xm = B[0] + a * dx / d
ym = B[1] + a * dy / d

Cx = xm + h * (-dy) / d
Cy = ym + h * dx / d
C = (Cx, Cy)

canvas.create_line(A, B, fill="red", width=3)
canvas.create_line(B, C, fill="green", width=3)
canvas.create_line(C, D, fill="orange", width=3)
canvas.create_line(A, D, fill="black", width=3)

#Question10
robot2 = canvas.create_oval(250, 200, 260, 210, fill="brown")
trail = []

def key_move(e):
    dx = dy = 0
    if e.keysym == "Up": dy = -5
    if e.keysym == "Down": dy = 5
    if e.keysym == "Left": dx = -5
    if e.keysym == "Right": dx = 5
    canvas.move(robot2, dx, dy)
    x1, y1, x2, y2 = canvas.coords(robot2)
    trail.append(canvas.create_line(x1+5, y1+5, x1+5, y1+5))

def reset():
    for t in trail:
        canvas.delete(t)
    trail.clear()

tk.Button(root, text="RESET", command=reset).pack()
root.bind("<Up>", key_move)
root.bind("<Down>", key_move)
root.bind("<Left>", key_move)
root.bind("<Right>", key_move)

root.mainloop()