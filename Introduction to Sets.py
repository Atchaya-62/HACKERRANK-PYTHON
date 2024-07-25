def average(array):
    arr_set = set(arr)
    avg = sum(arr_set)/len(arr_set)
     
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
