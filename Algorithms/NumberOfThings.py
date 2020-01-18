def how_many(the_list):
    # Add code here that returns the answer
    if the_list[0] == 1:
        return 'There is 1 '+ the_list[1]
    return 'There are '+ str(the_list[0]) + " " + the_list[1]+"s"
  
# Add print statements here to test what your code does:
print(how_many([5, "trinket"]))
print(how_many([1, "king"]))
print(how_many([1, "eraser"]))
print(how_many([4, "pencil"]))