from itertools import combinations
s,k=input().split()

for i in range(1, int(k)+1) :
  for e in sorted(list(combinations(sorted(s), i))):
       print(*["".join(e) ])
