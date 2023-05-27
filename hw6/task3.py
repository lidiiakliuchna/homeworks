
def main_menu():
    print('You are currently on the URL https://codefirstgirls.com/')
    print('Where are you clicking? ')
    print('Options: Courses, Opportunities')
    main_menu.answer=input()
def start():
    main_menu()
start()
def courses():
    print('You are currently on the URL https://codefirstgirls.com/courses')
    print('Where are you clicking? ')
    print('Options: CFGDegree, Back')
    courses.answer = input()
def degree():
    print('You are currently on the URL https://codefirstgirls.com/courses/cfgdegree')
    print('Where are you clicking? ')
    print('Options: Back')
    degree.answer = input()

def opportunuties():
    print('You are currently on the URL https://codefirstgirls.com/opportunitiess')
    print('Where are you clicking? ')
    print('Options: Ambassadors, Back')
    opportunuties.answer = input()

def ambassadors():
    print('You are currently on the URL https://codefirstgirls.com/opportunities/ambassadors/')
    print('Where are you clicking? ')
    print('Options: Back')
    ambassadors.answer = input()
while True:
    if main_menu.answer == 'Courses':
        courses()
        if courses.answer == 'CFGDegree':
            degree()
            if degree.answer == 'Back':
                courses()
            else:
                break
        else:
            main_menu()
    else:
        opportunuties()
        if opportunuties.answer == 'Back':
            main_menu()
        else:
            ambassadors()
            if ambassadors.answer == 'Back':
                opportunuties()
            else:
                break







