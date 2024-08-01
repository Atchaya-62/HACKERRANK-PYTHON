from collections import Counter
X = int(input())
xs = list(map(int, input().split()))
N = int(input())

counter = Counter(xs)
price = 0
for x in range(N):
    ss, sp = list(map(int, input().split()))
    if counter[ss] > 0:
        counter[ss] -= 1
        price += sp
print(price)
