
hong = {
    '이름': '홍길동',
    '나이': 20,
    '주소': '율도국'
}

for key in hong.keys():
    print(key)

for key in hong:
    print(key)

print('=' * 50)
for item in hong.items():
    print(item)
    print(type(item))

print('=' * 50)
for key in hong.keys():
    print((key, hong[key]))






