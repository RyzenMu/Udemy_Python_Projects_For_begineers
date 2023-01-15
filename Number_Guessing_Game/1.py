import random

# Generate a random number
random_number = random.randint(1, 100)

# print(random_number)

# check for the correct guess 

def guess_1():
    guess_1 = random_number // 10
    return guess_1


def guess_2():
    reminder = random_number%10
    if reminder < 5:
        print(1)
    else:
        print(2)

no_of_guess = 3


# loop for 3 gusses
for i in range(3):
    #  Collect input from the user
    
    print(f'you have {no_of_guess} guess')
    no_of_guess -= 1

    user_input = int(input('Enter a Guess Number : '))
    

    if user_input == random_number:
        print('You Suceeded')
        break
    else:
       
        if i == 0:
            print('Hint 1 : ',guess_1())
        if i == 1:
            guess_2()
else:
    print('Better luck next time')



print('The Number is :', random_number)
print('Good Luck')





