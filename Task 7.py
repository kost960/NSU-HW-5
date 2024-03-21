quantity = input('Введите данные станций (N, K, M соответственно): ')

quantity_split = quantity.split()
N = int(quantity_split[0])
K = int(quantity_split[1])
M = int(quantity_split[2])
count = 0

if M > K and M - K <= N // 2 or M < K and K - M > N // 2:
    K += 1
    while K != M:
        count += 1
        if K >= N:
            K = 0
        K += 1
elif K == M or abs(K - M) == 1:
    pass
else:
    K -= 1
    while K != M:
        count += 1
        if K <= 0:
            K = N
        K -= 1
print(count)