def lastWord(s):
    s = s.split(' ')
    return s[-1]

if __name__ == "__main__":
    s = input().strip()
    print(lastWord(s))