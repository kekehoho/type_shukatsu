for num in range(1, 101):
    string = ''

    # ここから記述
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz') #15の倍数ならFizzBuzzを出す。
    elif num%3 == 0:
        print('Fizz') #3の倍数ならFizzを出す。
    elif num%5 == 0:
        print('Buzz') #5の倍数ならBuzzを出す。
    else:
        print(num) #それ以外は数字を出す。

    # ここまで記述

    print(string)