def biSearch(arr, target):
    left = 0
    right = len(arr)-1
    middle = 0

    counter = 0
    for i in range(len(arr)):
        middle = (left + right) // 2
        counter += 1
        if arr[middle] == target:
            print("counter:", counter)
            return middle
        elif arr[left] == target:
            print("counter:", counter)
            return left
        elif arr[right] == target:
            print("counter:", counter)
            return right
        elif arr[middle] > target:
            right = middle
        elif arr[middle] < target:
            left = middle+1
    return -1


if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    target = int(input().strip())
    print(biSearch(arr, target))