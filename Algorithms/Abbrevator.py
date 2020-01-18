def abbreviator(string):
  # Add code here that returns the answer
    if len(string) <= 5:
        return string
    return string[:4]+"."
  
# Add print statements here to test what your code does:
print(abbreviator("arg"))
print(abbreviator("Trinket"))
print(abbreviator("bells"))
print(abbreviator("bells!"))