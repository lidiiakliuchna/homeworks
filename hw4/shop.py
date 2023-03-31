shop = {
"lamp": 50,
"t-shirt": 60,
"pants": 70,
"sofa": 120,
"exit" : "end"
}


money = 100
print("Welcome in our shop. Here are the prices:")
items=shop.keys()
for keys,values in shop.items():


    print(keys, ":", values)

answer=input("What would you like to choose?")
if answer in items and answer!='sofa' and answer!='exit':
    print(f'Here’s your {answer}!')
elif answer=='sofa':
    print(f'This one is too expensive! Do you have more money?')
    answer1=input().lower()
    if answer1=='yes':
        extra_money=int(input("How much more money do you have?"))
        money1= money+extra_money

        if money1>=shop["sofa"]:
            print(f'Here’s your {answer}!')
        else:
            for i in range(3):
                answer = input("Still too expensive. What another thing would you like to choose?")
                if answer in items and answer!='sofa' and answer!='exit':
                    print(f'Here’s your {answer}!')
                    break
                else:
                    print('It seems there is a problem. Try again')
            print("Too many attempts. Good bye!")



    else:
        for i in range(3):
            answer = input("What another thing would you like to choose?")
            if answer in items and answer != 'sofa' and answer != 'exit':
                print(f'Here’s your {answer}!')
                break
            else:
                print('It seems there is a problem. Try again')
        print("Too many attempts. Good bye!")

elif answer == 'exit':
    print("Good bye! See you again")

else:
    raise ValueError("Unknown Option Selected!")
