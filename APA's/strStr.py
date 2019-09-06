def strStr(haystack, needle):
    needleLen = len(needle)
    for i in range(len(haystack)-1):
        if haystack[i:i+needleLen] == needle:
            return i
    return -1

if __name__ == "__main__":
    haystack = input().strip()
    needle = input().strip()
    print(strStr(haystack, needle))