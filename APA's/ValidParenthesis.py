def validParenthesis(arr):
    for i in range(0,len(arr)-1,2):
        if arr[i] == '{' and arr[i+1] == '}':
            continue
        elif arr[i] == '[' and arr[i+1] == ']':
            continue
        elif arr[i] == '(' and arr[i+1] == ')':
            continue
        else:
            return False
    return True
        
if __name__ == '__main__':
    arr = list(input().strip())
    print(arr)
    print(validParenthesis(arr))