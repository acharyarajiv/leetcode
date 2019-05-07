'''
https://www.techgig.com/codegladiators/opencontest
'''


def main():
    tc = int(input())
    while tc > 0:
        players = int(input().strip())
        result = True
        villans = sorted(map(int, input().strip().split(' ')))
        heros = sorted(map(int, input().strip().split(' ')))
        for i in range(players - 1, 0, -1):
            if villans[i] > heros[i]:
                result = False
                break
        print('WIN' if result else 'LOSE')
        tc -= 1


main()
