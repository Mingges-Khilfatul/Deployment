print('Welcome to My World. ' + 'Can you please introduce yourself?')
Name = input('Full name :')

print('How I can call you?')
Name2 = input('Nickname :')

print('Hai,' + Name2 + ' You got invited to my world for play some simple game')
print('That game is calling question game.' + 'Question game have many types depending on the conditions that apply.')
print('So, before play the game you must fill out this question')
Age = int(input('Age :'))
if(Age < 10):
    print('You are in the Beginner Mode')
else:
    if(Age < 18):
        print('You are in the Intermediate Mode')
    else:
        if(Age < 50):
            print('You are in the Advanced Mode')
        else:
            print('You are too old to play this game.')


Prefer = input('What your prefer (Text/Number) :')
if Prefer == 'Text':
    print('Your base in Languange')
elif Prefer == 'Number':
    print('Your base in Number')
else:
    print('Sorry, you just answer with "Text" or "Number"')

print('Thank you for your applying, but sorry the system cant get you to game room.')
print('You can try in another day, see you...:)')

print("Before, i am leave. please give me a name. I don't accept rejection.")
Name3 = input("Name :")

print("Hhmm... Not bad. At least there's no dirty word in it. But thank you, have a nice day " + Name2)



