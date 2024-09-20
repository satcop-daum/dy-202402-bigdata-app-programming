numbers4 = ['a','b', 'c', 'd']
print('#' * 20)
print(numbers4)

print(numbers4[-4])

# 요소가 2개 => -4 ~ 0 ~ 3
#          => -2^2 ~ 2^2 - 1

numbers5 = numbers4[1:3]
print(numbers5)
print(type(numbers5))

numbers6 = numbers4[1:]
print(numbers6)

numbers7 = numbers4[:3]
print(numbers7)

numbers8 = numbers4[:]
print(numbers8)

numbers8.remove('a')

print('#' * 20)
print(numbers4)
print(numbers8)