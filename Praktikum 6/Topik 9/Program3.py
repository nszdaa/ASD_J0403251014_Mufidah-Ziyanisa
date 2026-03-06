buah = ['Apel', 'Buah Naga', 'Ceri']
try:
    x = buah.index("Ceri")
except ValueError:
    x = -1
try:
    y = buah.index("Kedondong")
except ValueError:
    y = -1
print(x)
print(y)

"""
Latihan:
Diberikan suatu list berikut:
data = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
Apakah keluaran dari:
● data.index(3, 0, 3)
● data.index(3, 5, 6)
● data.index(3, 3, 0)
● data.index(3, 0, 11)
"""

data = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]

try:
    print(data.index(3, 0, 3))
except ValueError:
    print("ValueError")

try:
    print(data.index(3, 5, 6))
except ValueError:
    print("ValueError")

try:
    print(data.index(3, 3, 0))
except ValueError:
    print("ValueError")

try:
    print(data.index(3, 0, 11))
except ValueError:
    print("ValueError")
