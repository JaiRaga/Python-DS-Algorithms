if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        P = input().strip()
        ans = ''
        for x in P:
            if x == 'E':
                ans += 'S'
            else:
                ans += 'E'
        print('Case #{}: {}'.format(i+1, ans))
