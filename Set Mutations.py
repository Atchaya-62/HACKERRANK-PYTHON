n = int(input())
A = set(map(int, input().split(" ")))
N = int(input())

for i in range(N):
    cmd_line = input().split()
    cmd_set = set(map(int, input().split()))
    
    if (cmd_line[0] == "intersection_update"):
        A.intersection_update(cmd_set)
    elif (cmd_line[0] == "update"):
        A.update(cmd_set)
    elif (cmd_line[0] == "symmetric_difference_update"):
        A.symmetric_difference_update(cmd_set)
    elif (cmd_line[0] == "difference_update"):
        A.difference_update(cmd_set)

print(sum(A))
