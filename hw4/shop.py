shop = {
"lamp": 50,
"t-shirt": 60,
"pants": 70,
"sofa": 120,
"exit" : "end"
}


money = 100
items=''
def greeting():
    print("Welcome in our shop. Here are the prices:")
    global items
    items=shop.keys()
    for keys,values in shop.items():
        print(keys, ":", values)

greeting()
answer=input("What would you like to choose?")
if answer in items and answer!='sofa' and answer!='exit':
    print(f'Here’s your {answer}!')
elif answer=='sofa':
    print(f'This one is too expensive! Do you have more money?')
    answer1=input().lower()
    if answer1 == 'yes':
        def yes_money():
            extra_money=int(input("How much more money do you have?"))
            money1= money+extra_money

            if money1>=shop["sofa"]:
                print(f'Here’s your {answer}!')

            else:
                def choose_something():
                    tries = 0
                    while tries<=3:
                        answer = input("Still too expensive. What another thing would you like to choose?")
                        if answer in items and answer!='sofa' and answer!='exit':
                            print(f'Here’s your {answer}!')
                            return True
                        else:
                            print('It seems there is a problem. Try again')
                            tries+=1
                    print("Too many attempts. Good bye!")
                choose_something()
        yes_money()

    else:
        def no_money():
            tries = 0
            while tries<=3:

                answer = input("What another thing would you like to choose?")
                if answer in items and answer != 'sofa' and answer != 'exit':
                    print(f'Here’s your {answer}!')
                    return True
                else:
                    print('It seems there is a problem. Try again')
                    tries += 1
            print("Too many attempts. Good bye!")
        no_money()

elif answer == 'exit':
    print("Good bye! See you again")

else:
    raise ValueError("Unknown Option Selected!")
