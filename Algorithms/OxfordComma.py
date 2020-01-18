def commafy(list):
  # Add code here that returns the answer
    s = ''
    if len(list) >= 3:
        for i in range(len(list)):
            if i != len(list) - 1:
                s += list[i] + ", "
            else:
                s += "and " + list[i]
    
    return s

print(commafy(["trinket", "learning", "fun"]))
print(commafy(["lions", "tigers", "bears"]))