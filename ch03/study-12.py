
hong = {
    '이름': '홍길동',
    '나이': 20,
    '주소': '율도국'
}

print(type(hong))
print(hong)
print(hong['이름'])

hong['나이'] = 30
print(hong)

print(len(hong))

print(hong.keys())
print(type(hong.keys()))

for key in hong.keys():
    print(key, hong[key])

print(hong.values())
print(type(hong.values()))

for value in hong.values():
    print(value)

hong.






