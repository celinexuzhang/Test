
n = int(input())
if n % 2 > 0 or (n % 2 == 0 and n in range(6, 21)):
    print('Weird')
elif n % 2 == 0 and n in range(2, 6) or n > 20:
    print('Not Weird')


print('Rico is so cool!')
