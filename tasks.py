
def tasks_2():
    for i in range(100, 0, -1):
        if (int(str(i)[0]) % 2 == 0) and ((i % 3) != 0) and ((i % 5) == 0):
            print(i)
            break

def tasks_5():
    for i in range(10000):
        b = 4
        b = ((b + 2) * i) + 2
        if b == 56:
            print(i)
            break

# amount = int(input())
# count = 0
# mas = []
# for i in range(amount):
#     elem = int(input())
#     if elem % 3 == 0 and int(str(elem)[-1]) == 2:
#         mas.append(elem)
#
# print(len(mas))



# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             for w in (0, 1):
#                 if ((not(y) or x) and not(z) and w):
#                     print(x, y, z, w)



days = int(input())
sr = 0
count = 0
for i in range(days):
    degree = float(input())
    if degree > 0:
        sr += degree
        count +=1

sr /= count
print(sr, count)
