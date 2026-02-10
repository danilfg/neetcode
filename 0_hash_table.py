'''
Hash Table = набор "коробок" (ячеек)

Индекс (ключ) → Значение
'''
s = set()
d = {}
#
# print(type(s))
# print(type(d))

size = 8
# value = 42
# print('hash', hash(value))
# index = hash(value) % size
# print(index)

'''
Index | Bucket
----------------
  0   | [ ]
  1   | [ ]
  2   | [ 42 ]
  3   | [ ]
  4   | [ ]
  5   | [ ]
  6   | [ ]
  7   | [ ]
'''

'''
Ищем: 42


→ смотрим только ячейку 2
→ нашли сразу
Время поиска: O(1)
(не перебираем весь массив)

'''
# Коллизия

value_1 = 42
value_2 = 10
print(f"hash значения '{value_1}':", hash(value_1))
print(f"hash значения '{value_2}':", hash(value_2))
# print(hash(value_2))
index_1 = hash(value_1) % size
print(f"index значения '{value_1}':", index_1)

index_2 = hash(value_2) % size
print(f"index значения '{value_2}':", index_2)
'''
Index | Bucket
----------------
  0   | [ ]
  1   | [ ]
  2   | [ 42 ]
  3   | [ 8 ]
  4   | [ ]
  5   | [ ]
  6   | [ ]
  7   | [ ]
'''

'''
Ищем: 8

hash(8)
→ смотрим список [42 → 8]
→ проверяем по очереди
В худшем случае: O(n)
В среднем: O(1)
'''


# Пример DICT

'''
Index | Bucket
-----------------------------
  0   | [ ]
  1   | [ ]
  2   | [ ("age", 42) ]  ← dict хранит ПАРУ
  3   | [ ]
  4   | [ ]
  5   | [ ]
  6   | [ ]
  7   | [ ]
'''

'''
стартовый размер: 8
рост: ×2
resize при ~66% заполнения
все ключи перехэшируются
средняя сложность: O(1)
'''