shop = {
"lamp": 50,
"t-shirt": 60,
"pants": 70,
"sofa": 120,
"exit" : "end"
}


money = 100
print("Welcome in our shop. Here are the prices:")

for keys,values in shop.items():
    items=values
    print(keys, ":", values)
answer=input("What would you like to choose?")
if answer=='lamp':
    print(f'Here’s your {answer}!')
elif answer=='t-shirt':
    print(f'Here’s your {answer}!')
elif answer=='pants':
    print(f'Here’s your {answer}!')
elif answer=='sofa':
    print(f'This one is too expensive! Do you have more money?')
    answer1=input()
    if answer1=='Yes':
        extra_money=int(input("How much more money do you have?"))
    else:
        answer = input("What another thing would you like to choose?")
        print(f'Here’s your {answer}!')
elif answer == 'exit':
    print("Good bye! See you again")

else:
    if items not in shop:
        raise ValueError("Unknown Option Selected!")
