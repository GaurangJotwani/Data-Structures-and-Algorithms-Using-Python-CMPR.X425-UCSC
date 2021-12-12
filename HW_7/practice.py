coins = [1, 2, 5]


def get_min_coin(amount):
    min_coins = [0]
    kind_of_coin = [0]
    for i in range(1, amount+1):
        d = {}
        for coin in coins:
            a = i - coin
            if a < 0:
                continue
            else:
                if min_coins[a] == -1:
                    continue
                d[coin] = 1 + min_coins[a]
        if d:
            x = min(d, key=d.get)
            min_coins.append(d[x])
            kind_of_coin.append(x)
        else:
            min_coins.append(-1)
            kind_of_coin.append(-1)
    a = amount
    l = [0]
    while a > 0:
        if kind_of_coin[a] == -1:
            return -1
        l.append(kind_of_coin[a])
        a = a - kind_of_coin[a]
    return l


print(get_min_coin(11))
