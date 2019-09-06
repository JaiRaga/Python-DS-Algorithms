# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty.

def LongestWord(sen): 

    # code goes here 
    word = sen.split(' ')
    arr = []
    s = ''
    for j in word:
      for i in j:
        if i.isalpha():
          s += i
      arr.append(s)
      s = ''
      
    for i in arr:
      if len(i) > len(s):
        s = i
      
    return s


print(LongestWord("fun&!! time")) # ans: "time"
print(LongestWord("I love dogs")) # ans: "love"