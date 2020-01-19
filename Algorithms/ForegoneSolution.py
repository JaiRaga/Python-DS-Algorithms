if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        A = [j for j in str(n)]
        B = [0] * len(A)
        case = i+1
        for v in range(len(A)):
            if A[v] == '4':
                A[v] = '2'
                B[v] = 2

                # print(A, B)
        A = "".join(A)
        b = ''
        for x in B:
            b += str(x)
        # print(A, b)

        print('Case #{}: {} {}'.format(case, int(A), int(b)))
