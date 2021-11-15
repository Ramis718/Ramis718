from random import  randint
from datetime import  datetime

print(randint(1, 6))
print(randint(1, 6))


attempts = int(input("ВВЕДИТЕ КОЛТЧЕСТВО ПОПЫТОК:"))

yehb
cash = 100
while attempts != 0:
    player = [randint(1, 6), randint(1, 6)]
    comp = [randint(1, 6), randint(1, 6)]
    if cash == 0:
        print('YOU lost')
        break
    bet = int(input(f"Сделайте ставку: ' \n Доступно:, {cash}"))
    if bet < 1 or bet > cash:
        print('Ставка не должен превышать')
        continue

    attempts -= 1
    if attempts == 0:
        player = [randint(1, 2), randint(1, 3)]
        comp = [randint(4, 6), randint(5, 6)]
    if sum(player) > sum(comp):
        cash += bet
    elif sum(player) < sum(comp):
        cash -= bet
    else:
        pass
    with open('res.txt', 'a') as result:
        result.write(f'Player: {player} \n,comp: {comp} \n {cash}')

    print(cash)
    print('Player', player)
    print('COMP', comp)

