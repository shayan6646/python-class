'''012'''
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
if num1>num2:
    print(num1,num2)
else:
    print(num2,num1)
    
'''013'''
num=int(input('Enter your number: '))
if num<20:
    print('thank you')
else:
    print('too high')
    
'''014'''
num=int(input('Enter your number: '))
if  num>=10: and num<=20
    print('Thank you')
else:
    print('Incorrect answer')
    
'''015'''
coulour=input('Enter your favorite colour: ')
if coulour.upper()=='RED':
    print('I like red too')
else:
    print('I dont like ' + coulour + ',I prefer red')
    
'''016'''
rain=input('is it raining? ').lower()
if rain=='yes':
    windy=input('is it windy? ').lower()
    if windy=='yes':
        print('its too windy for an umbrella')
    else:
        print('take an umbrella')
else:
    print('enjoy your day')
    
'''017'''
age= int(input('please enter your age: '))
if age>=18:
    print('you can vote')
elif age==17:
    print('you can drive')
elif age==16:
    print('you can buy a lottery ticket')
else:
    print('you can go trick or treating')
    
'''018'''
num= int(input('please enter your number: '))
if num<10:
    print('too low')
elif num>=10 and num<=20:
    print('correct answer')
else:
    print('too high')
    
'''019'''
num= int(input('please enter your number: '))
if num==1:
    print('Thank you')
elif num==2:
    print('well done')
elif num==3:
    print('correct')
else:
    print('Error message')
