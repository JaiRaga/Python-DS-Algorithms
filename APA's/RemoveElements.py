def rem(arr, target):
    times = arr.count(target)
    if times > 0:
        for i in range(times):
            arr.remove(target)
        return arr
    return arr

if __name__ == '__main__':
    arr = list(map(int, input().strip().split(' ')))
    target = int(input().strip())
    print(rem(arr, target))