
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
    courses.answer_1 = input()
def degree():
    print('You are currently on the URL https://codefirstgirls.com/courses/cfgdegree')
    print('Where are you clicking? ')
    print('Options: Back')
    degree.answer_2 = input()

def opportunuties():
    print('You are currently on the URL https://codefirstgirls.com/opportunitiess')
    print('Where are you clicking? ')
    print('Options: Ambassadors, Back')
    opportunuties.answer_3 = input()

def ambassadors():
    print('You are currently on the URL https://codefirstgirls.com/opportunities/ambassadors/')
    print('Where are you clicking? ')
    print('Options: Back')
    ambassadors.answer_4 = input()

if main_menu.answer == 'Courses':
    courses()
else:
    opportunuties()
if courses.answer_1 =='CFGDegree':
    degree()
else:
    main_menu()
if degree.answer_2 =='Back':
    courses()
if opportunuties.answer_3 =='Ambassadors':
    ambassadors()
else:
    main_menu()
if ambassadors.answer_4 =='Back':
    opportunuties()
