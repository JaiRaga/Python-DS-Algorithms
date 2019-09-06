def long(arr):
    word = ''
    count = 0
    arr.sort(key=len)
    l = len(arr[0])
    for i in range(l):
        for j in range(len(arr)):
            if arr[0][i] == arr[j][i]:
                count += 1
                continue
        if count == len(arr):
            word += arr[0][i]
            count = 0
        else:
            return word
    return word     

if __name__ == "__main__":
    lis = list(input().strip().split(' '))
    print(long(lis))
    