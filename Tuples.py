if __name__ == '__main__':
    n = int(input())
    i = map(int, input().split())
    a=tuple (i)
    print(hash(a))
