if __name__ == '__main__':
    n = int(input())
    score = map(int, input().split())
    arr = []
    for i in (score):
        arr.append(int(i))
    max_arr= max(arr)
    while max_arr in (arr):
        arr.remove(max_arr)

    print(max(arr))
