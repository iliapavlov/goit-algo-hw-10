# Набір доступних монет
COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in COINS:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount):
    # Ініціалізація масиву для зберігання мінімальної кількості монет
    min_coins = [float('inf')] * (amount + 1)
    coin_used = [0] * (amount + 1)
    min_coins[0] = 0  # 0 монет для суми 0

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    # Відновлення словника з номіналами
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result