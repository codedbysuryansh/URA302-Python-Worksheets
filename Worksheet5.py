import numpy as np
import matplotlib.pyplot as plt

#Question1
a = np.random.randint(1, 100, 10)
print(a)
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard Deviation:", np.std(a))

#Question2
b = np.random.randint(1, 50, (4, 4))
print(b)
print("Row wise sum:", np.sum(b, axis=1))
print("Column wise sum:", np.sum(b, axis=0))

#Question3
c = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Transpose:")
print(c.T)

#Question4
x = np.array([10, 20, 30, 40, 50])
y = np.array([1, 2, 3, 4, 5])
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

#Question5
arr = np.random.randint(1, 100, 15)
print(arr)
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Index of Max:", np.argmax(arr))
print("Index of Min:", np.argmin(arr))

#Question6
m = np.array([[2, 4],
              [6, 8]])
n = np.array([[1, 3],
              [5, 7]])
print("Dot Product:")
print(np.dot(m, n))

#Question7
data = np.array([5, 10, 15, 20, 25])
print("Cumulative Sum:", np.cumsum(data))

#Question8
values = np.array([12, 15, 7, 9, 20, 18])
print("Sorted Array:", np.sort(values))

#Question9
marks = np.array([78, 85, 90, 66, 72])
subjects = ['Math', 'Physics', 'Chemistry', 'English', 'CS']
plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

#Question10
x = np.linspace(0, 10, 50)
y = x ** 2
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("X vs X^2")
plt.show()