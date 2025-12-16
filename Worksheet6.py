import pandas as pd

#Question1
print(pd.__version__)

#Question2
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

#Question3
s = pd.Series([100, 200, 300, 400, 500])
print(s)
print(s[1])
print(s[3])

#Question4
s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([1, 2, 3, 4, 5])
print(s1 + s2)

#Question5
print(df[['Name', 'City']])

#Question6
df['Salary'] = [50000, 60000, 70000]
print(df)

#Question7
print("Average Age:", df['Age'].mean())
print("Total Salary:", df['Salary'].sum())

#Question8
print(df[df['Age'] > 28])

#Question9
df.set_index('Name', inplace=True)
print(df)

#Question10
df.reset_index(inplace=True)
print(df)

#Question11
emp = {
    'Name': ['John', 'Jane', 'Emily', 'Mark'],
    'Department': ['HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 55000, 65000]
}
emp_df = pd.DataFrame(emp)
print(emp_df)

#Question12
print(emp_df[emp_df['Salary'] > 55000][['Name', 'Department']])

#Question13
print(emp_df.groupby('Department')['Salary'].mean())

#Question14
print(emp_df.groupby('Department')['Salary'].agg(['min', 'max']))

#Question15
df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})

df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience': [5, 7, 3]
})

merged = pd.merge(df1, df2, on='Name')
print(merged)

#Question16
print(merged.sort_values(by='Experience', ascending=False))