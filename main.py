def func():

    try:
        num_1 = float(input('---Enter the first number--> '))
        def oper():
            operation = input('---Enter the type of operation[+, -, *, /, %]--> ')
            try:
                num_2 = float(input('---Enter the second number--> '))
            except ValueError:
                print('\n!!!This input has to be a number\n\n')
                func()

            global answ
            if operation == '+':
                    answ = num_1 + num_2

            elif operation == '-':
                    answ = num_1 - num_2

            elif operation == '*':
                    answ = num_1*num_2

            elif operation == '/':
                    answ = num_1/num_2
                
            elif operation == '%':
                    answ = num_1/num_2*100

            else:
                 print('\n!!!Incorrect operation\n***Here is the list of operations:[+, -, *, /, %]\n\n')
                 func()
            print('\n***Intermediate result is--> ', answ)
        oper()


        while True:
            one_more_oper = input('\n---One more operation? [y/n]: ') 
            print('')
            if one_more_oper == 'y':         
                num_1 = answ
                oper()
            elif one_more_oper == 'n':
                print('\n***The final result is--> ', answ)
                break
            else:
                print('\n***The final result was--> ', answ)
                print('\n!!!But you had to choose [y/n]')
                break
                
                          
    except ValueError:
        print('\n!!!This input has to be a number\n\n')
        func()

func()


while True:
    again_yes_or_no = input('\n\n---Again? [y/n]: ')

    if again_yes_or_no == 'y':
        print('\n')
        func()
    else:
        quit()