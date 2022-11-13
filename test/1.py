input_num = int(input())

if (input_num % 3)  == 0 and (input_num % 5) == 0:
    print('fizzbuzz')
elif (input_num % 3)  == 0:
    print('fizz')
elif (input_num % 5) == 0:
    print('buzz')
