data1 = ['a', 'b']
data2 = ['c', 'd']


data3 = data1 + data2
print(data3)


del data3[2]


print('-' * 40)
print(type(data3))
print(data3)

data3.remove('a')

print('-' * 40)
print(data3)

#data3.delete(2)



