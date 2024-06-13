import numpy as np

scores = np.array([[[20, 40, 56, 80, 0, 5, 25, 27, 74, 1],
         [0, 98, 67, 100, 8, 56, 34, 82, 100, 7],
         [78, 54, 23, 79, 100, 0, 0, 42, 95, 83],
         [51, 50, 47, 23, 100, 94, 25, 48, 38, 77],
         [90, 87, 41, 89, 52, 0, 5, 17, 28, 99],
         [32, 18, 21, 18, 29, 31, 48, 62, 76, 22],
         [6, 0, 65, 78, 43, 22, 38, 88, 94, 100],
         [77, 28, 39, 41, 0, 81, 45, 54, 98, 12],
         [66, 0, 88, 0, 44, 0, 55, 100, 12, 11],
         [17, 70, 86, 96, 56, 23, 32, 49, 70, 80],
         [20, 24, 76, 50, 29, 40, 3, 2, 5, 11],
         [33, 63, 28, 40, 51, 100, 98, 87, 22, 30],
         [16, 54, 78, 12, 25, 35, 10, 19, 67, 0],
         [100, 88, 24, 33, 47, 56, 62, 34, 77, 53],
         [50, 89, 70, 72, 56, 29, 15, 20, 0, 0]]])
print(scores)
print(type(scores))
#1. Свойства массивов Numpy
print(scores.ndim) # Размерность массива
print(scores.size) # Размер массива
print(scores.shape) # Форма массива
print(scores.dtype) # Тип данных в массиве
print('---------------')
# 2. Способы создания массивов Numpy
print(np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
          [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]))
print(np.zeros([3,4,2]))
print(np.ones([4,2,3], dtype=np.int32))
print(np.full([4,2], 8))
print(np.full_like(scores, 1))
print(np.eye(5, dtype=np.int32))
print(np.random.rand(6,6)*6-3) #Создание массива с случайными эллементами в диапазоне (-3;3)
print(np.random.randint(7, 12, [6,6]))
print('---------------')
# 3. Slice/нарезка массивов Numpy
print('3. Slice/нарезка массивов Numpy')
print(scores[0])
print(scores[0][1])
print(scores[0][1][2])
print(scores[0, 1, 2])
print(scores[0, 2:-1, 4])
scores[0, 2:-1, 4] = 0
print(scores)
print('---------------')
#4. Операции с массивами Numpy
print('4. Операции с массивами Numpy')
a = np.full_like(scores, 4)
b = np.full_like(scores, 3)
c = np.full((10,15), 5)
print(a)
print(b)
print(a+b)
print(a-2)
print(a*b)
print(b@c)
print(a/b)
print('---------------')
# 5. Булевы массивы Numpy
print('5. Булевы массивы Numpy')
a = np.random.rand(3,4) * 5
b = np.random.rand(3,4) * 5
c = a>2
print(a)
print(c)
print(a[a>2])
print(b)
print('---------------')
#6. Стандартные функции массивов Numpy
print('6. Стандартные функции массивов Numpy')
a = np.random.rand(3,4) * 5
b = np.array(range(4))
print(scores)
#help(np.argmax)
print(np.argmax(scores))
print(a)
print(np.sin(a))
print(np.exp(a))
print(b)
print(np.sum(b))
print(np.prod(b[1:-1]))
print(np.min(a))
print(np.max(a))

print('---------------')
#7. Массивы Numpy с множеством измерений
print('7. Массивы Numpy с множеством измерений')
cube1 = np.random.randint(1,3,[3,3,3])
cube2 = np.random.randint(3,5,[3,3,3])
cube3 = np.random.randint(6,8,[3,3,3])
arr4 = np.array([cube1, cube2, cube3, cube3, cube3])
arr5 = np.array([arr4, arr4, arr4, arr4])
print(arr4[:-2])
print(arr5.shape)
print(arr5[-2:-1, :-2, ..., -1])

#https://github.com/Ethertrust/DataWorkThursday.git