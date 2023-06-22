OPER_LIST = ['+', '-', '*', '/', '%']

def operation(num_1, oper, num_2):
     result = eval(str(num_1) + oper + str(num_2))
     return result

def main_func():
    try:
        num_1 = float(input('---Enter the first number--> '))
        def oper(num_1):
            oper = input(f'---Enter the type of operation{OPER_LIST}--> ')
            try:
                num_2 = float(input('---Enter the second number--> '))
            except ValueError:
                print('\n!!!This input has to be a number\n\n')
                main_func()

            global answ

            if oper in OPER_LIST:
                if num_2:
                    answ = operation(num_1, oper, num_2)
            else:
                 print(f'\n!!!Incorrect operation\n***Here is the list of operations:{OPER_LIST}\n\n')
                 main_func()
            print(f'\n***Intermediate result is--> {answ}')
        oper(num_1)


        while True:
            one_more_oper = input('\n---One more operation? [y/n]: ').lower()
            print('')
            if one_more_oper == 'y':         
                oper(answ)
            elif one_more_oper == 'n':
                print(f'\n***The final result is--> {answ}')
                break
            else:
                print(f'\n***The final result was--> {answ}\n!!!But you had to choose [y/n]')
                break      
                          
    except ValueError:
        print('\n!!!This input has to be a number\n\n')
        main_func()

main_func()


while True:
    again_yes_or_no = input('\n\n---Again? [y/n]: ').lower()

    if again_yes_or_no == 'y':
        print('\n')
        main_func()
    else:
        quit()