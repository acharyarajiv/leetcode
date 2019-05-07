'''
https://www.techgig.com/codegladiators/opencontest
'''


def normalize(i):
    if i > 0:
        return i, str(i)
    else:
        return 0, ''


def appendstr(str_i, str_n):
    if str_n != '':
        if str_i == '':
            str_i = str_n
        else:
            str_i = str_n + ',' + str_i
    return str_i


def comapreAndPrint(csv_last, csv_second_last):
    if csv_last == csv_second_last:
        print(''.join(c for c in csv_last.split(',')))
    else:
        int_a = list(map(int, csv_last.split(',')))
        int_b = list(map(int, csv_second_last.split(',')))
        sum_a, sum_b = sum(int_a), sum(int_b)
        if sum_a > sum_b:
            print(''.join(c for c in csv_last.split(',')))
        else:
            la, lb = len(int_a) - 1, len(int_b) - 1
            i = 0
            while i < la and i < lb:
                if int_a[i] > int_b[i]:
                    print(''.join(c for c in csv_last.split(',')))
                    break
                elif int_a[i] < int_b[i]:
                    print(''.join(c for c in csv_second_last.split(',')))
                    break
                i += 1


def main():
    tc = int(input())
    while tc > 0:
        total_player = int(input())
        tickets = list(map(int, input().strip().split(' ')))
        int_tickets = tickets
        total_player = len(int_tickets)

        if total_player == 0:
            print(max(tickets))
            return

        sum_arr = [0] * total_player
        composition = [None] * total_player 

        ticket, str_ticket = normalize(int_tickets[0])
        sum_arr[0] = ticket
        composition[0] = appendstr('', str_ticket)

        ticket, str_ticket = normalize(int_tickets[1])
        if ticket >= sum_arr[0]:
            sum_arr[1] = ticket
            composition[1] = appendstr('', str_ticket)
        else:
            sum_arr[1] = sum_arr[0]
            composition[1] = appendstr('', composition[0])

        for i in range(2, total_player):
            ticket, str_ticket = normalize(int_tickets[i])
            if sum_arr[i - 2] + ticket >= sum_arr[i - 1]:
                composition[i] = appendstr(composition[i - 2], str_ticket)
                sum_arr[i] = sum_arr[i - 2] + ticket
            else:
                sum_arr[i] = sum_arr[i - 1]
                composition[i] = appendstr(composition[i - 1], '')
        comapreAndPrint(composition[total_player - 1], composition[total_player - 2])
        tc -= 1


main()
