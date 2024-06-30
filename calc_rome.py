def first_tasks(n, k):
    return n - k % n


def second_tasks(number):
    first_sum, second_sum = 0, 0
    for i in range(len(number) // 2):
        first_sum += int(number[i])
        second_sum += int(number[len(number) - i - 1])

    if first_sum == second_sum:
        return 'YES'
    else:
        return 'NO'


def third_tasks(xy):
    mas_a = 'ACEG'
    mas_i = '2468'
    if xy[0] in mas_a and xy[1] in mas_i or xy[0] not in mas_a and xy[1] not in mas_i:
        print('WHITE')
    else:
        print('BLACK')


def fourth_tasks(elem):
    elem = elem.split(' ')
    print(len(elem))


def fiveth_tasks():
    arr = input('input: ')
    arr = arr.split()
    for j in range(len(arr)-1):
        for i in range(0, len(arr)-1):
            arr[i], arr[i+1] = arr[i+1], arr[i]

    print(arr)

