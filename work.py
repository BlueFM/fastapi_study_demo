length = int(input())
gold = silver = bronze = 0
x = 0.0
nor = [0 for i in range(length)]
for i in range(length):
    str = input().strip()
    l = str.split(" ")
    num = [int(s) for s in l]
    if 140 >= num[0] >= 90 and 90 >= num[1] >= 60:
        nor[i] = 1
length = 0
temp = 0
for i in range(len(nor)):
    if nor[i] == 1:
        temp += 1
    if temp > length:
        length = temp
        temp = 0
print(length)