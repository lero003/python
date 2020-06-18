#for文
for i in range(5):
    print(i)

#break文
for i in range(5):
    if i == 3:
        break
    print(i)

#continue文
for i in range(5):
    if i == 3:
        continue
    print(i)

#for文ネスト構造（sep引数）
for i in range(3):
    for j in range(3):
        print(i,j,sep="-")

#組み合わせ
arr = [2,4,6,8,10]
sum = 0
for i in arr:
    sum += i
print(sum)