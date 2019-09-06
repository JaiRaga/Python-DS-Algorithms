def FirstFactorial(num): 

    # code goes here 
    if num == 0:
      return 1
    return num * FirstFactorial(num-1)