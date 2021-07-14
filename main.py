# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

classic_list = [1, 2, 3, 5, 7, 11]
print(type(classic_list))


classic_list = [1, 2, 3, 5, 7, 11]

numpy_array = np.array(classic_list)
print (type(numpy_array))

print(numpy_array.shape)

print(np.array([2,4]).mean())

#Matrix

numpy_matrix = np.array([[1,2,3], [5,7,11]])
print(numpy_matrix.shape)

matrix1 = np.array([
	[1,2,3],
	[4,5,6],
	[7,8,9]
])

#wydrukuje 1 kolumne
print(matrix1[0, :])


#wydrukuje ostatnią kolumne
print(matrix1[:, -1])


matrix2 = np.array([
	[1,2,3],
	[0,8,10],
	[1,10,12]
])

#suma wszytskich elementów
print(matrix2.sum())

#suma kolumn
print(matrix2.sum(axis=0))

#suma wierszy
print(matrix2.sum(axis=1))

#dodawanie 2 macierzy
print(np.array([1,2]) + np.array([8,9]))

#wektory
print(np.array([1,2,3,4,5,6,7,8,9,10]) + np.ones([10]))

#macierz
print(np.array([1,2,3,4,5,6,7,8,9,10]) + np.ones([10]))

print("macierz")
print()
print()


matrix5 = np.array([
	[1,2,3,4,5],
	[6,7,8,9,10],
	[11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
])
print("średnie wierszy")
print(matrix5[0, :].mean())
print(matrix5[1, :].mean())
print(matrix5[2, :].mean())
print(matrix5[3, :].mean())
print(matrix5[4, :].mean())


print("średnie kolumn")
print(matrix5[:, 0].mean())
print(matrix5[:, 1].mean())
print(matrix5[:, 2].mean())
print(matrix5[:, 3].mean())
print(matrix5[:, 4].mean())

print ("jedziemy z panda")
print()

salaries = [
	("Mark", 1000),
	("John", 1500),
	("Daniel", 2300),
	("Greg", 5000)
]

names_series = pd.Series(["Mark", "John", "Daniel", "Greg"])
print(names_series)

salary_series = pd.Series([1000, 1500, 2300, 5000])
print(salary_series)

#Mamy np. funkcję describe, wypisującą parametry właściwe dla typu serii, którą stworzyliśmy.
#W wypadku tekstów to np. liczba unikalnych elementów.

print(names_series.describe())

#Dla liczb to zdecydowanie więcej statystyk, mamy m.in. rozkład wartości (mediany) i inne statystyczne
# właściwości:
print(salary_series.describe())


print('zadanie')

salary_series2 = pd.Series([1100, 1600, 2400, 5100])
print(salary_series2)


print(salary_series.index)


salary_series.index = names_series
print(salary_series)


print(salary_series['Mark'])

print("pauza")

names = ["Mark", "John", "Daniel", "Greg"]
salaries = [1000, 1500, 2300, 5000]
salary_series_improved = pd.Series(salaries, index=names)

print(salary_series)


salaries = [
	("Mark", 1000, 23),
	("John", 1500, 25),
	("Daniel", 2300, 38),
	("Greg", 5000, 42)
]

df = pd.DataFrame(salaries)
print(df)

#dodaje opis kolumn
df = pd.DataFrame(salaries, columns=["name", "salary", "age"])
df = df.set_index("name")
print(df)

#dane statystyczne
print(df.describe())

#podwyżka dla wszystkich o 2000
salary_increased_series = df['salary'].apply(lambda salary: salary + 2000)
df['salary'] = salary_increased_series

print(df)

#podwyżka dla wszystkich o 2000
salary_raise = [2000, 2000, 2000, 2000]
df['salary'] + salary_raise
print(df)

print('zadanie2')

salaries = [
	("Mark", 1000, 23),
	("John", 1500, 25),
	("Daniel", 2300, 38),
	("Greg", 5000, 42)
]

df = pd.DataFrame(salaries)
print(df)

df = pd.DataFrame(salaries, columns=["name", "salary", "age"])
df = df.set_index("name")
print(df)

df2 = df.assign(initials = ['M', 'J', 'D', 'G'])
print(df2)


print('iterator')

salaries = [1000, 5000, 7000]
salary_iterator = iter(salaries)
print(next(salary_iterator))
print(next(salary_iterator))
print(next(salary_iterator))

salary_iterator = iter(salaries)
salary_sum = 0
for salary in salary_iterator:
	salary_sum = salary_sum + salary
print("Total salaries = %d" % salary_sum)

print ('generator')

def give_me_first_ten_numbers():
	for i in range(1,11):
		yield i

for number in give_me_first_ten_numbers():
	print(number)


print('zadanie')
print()

n = 10

def give_me_n_numbers():
	for i in range(1,n+1):
		yield i

for number in give_me_n_numbers():
	print(number)

print ('zadanie')

prices = [
	(1, 2.12),
	(2, 2.56),
	(3, 3.10),
	(4, 3.16),
	(5, 3.58),
	(6, 5.12),
	(7, 5.16),
	(8, 5.20),
	(9, 4.12),
	(10, 4.10),
	(11, 3.65),
	(12, 4.25),

]


df = pd.DataFrame(prices, columns=["month", "price PLN"])
df = df.set_index("month")
print(df)

usd = df['price PLN'].apply(lambda price: price * 4)
df['price USD'] = usd

print(df)





