from calc_rome import *


def menu():
    action = ''
    while action != '0':
        print("1 - первая задача\n2 - вторая задача\n3 - третья задача\n4 - четвертая задача\n5 - пятая задача\n0 - выключить")
        action = input()
        if action == '1':
            n = int(input('students: '))
            k = int(input('apple: '))
            answer = first_tasks(n, k)
            print(answer)
        elif action == '2':
            ticket = input('input bus ticket: ')
            answer = second_tasks(ticket)
            print(answer)
        elif action == '3':
            xy = input('input xy: ')
            third_tasks(xy)
        elif action == '4':
            words = input('input words: ')
            fourth_tasks(words)
        elif action == '5':
            words = input('input: ')
        elif action == '0':
            print('exit from program')
            return 0





menu()