def wordedMath(equ):
    numObj = {
        'zero': 0,
        'one': 1,
        'two': 2
    }

    num = {
        "1": 'One',
        "2": 'Two',
        "0": "zero"
    }

    equ = equ.lower().split(' ')
    val = 0
    sign = ''

    if equ[1] == 'plus':
        sign = 'add'
    else: 
        sign = 'min'
    
    if sign == 'add':
        val = numObj[equ[0]] + numObj[equ[2]]
    else:
        val = numObj[equ[0]] - numObj[equ[2]]

    return num[str(val)]


print(wordedMath('One plus one'))