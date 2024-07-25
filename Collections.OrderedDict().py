# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
purchases = OrderedDict()

for i in range(n):
    *key, value = input().split(' ')
    key = ' '.join(key)
    purchases[key] = purchases.get(key, 0) + int(value)
    
[print(key, value) for key,value in purchases.items()]
