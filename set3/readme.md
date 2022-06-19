TODO: Reflect on what you learned this week and what is still unclear.
Week 3: lets do this

---

Useful Info:
searches - binary and linear searches.
binary - more efficient and faster, keeps cutting code in half until the number is found
linear - more time consuming, (e.g. goes through EVERY number in the list until the number is found)
range() - is a function, returns sequence of numbers, starts from 0, increments 1, and stops at a number (specified)
code errors: Logic, syntax, runtime
loops: while, for, repeat until
lists = []
f strings = simplifying strings with 'f'
code golf = use it to help make your code more efficient/least number of lines
append = adding to a list
debugging = when trying to figure out how to debug your work, run the debugging file.
bubble sort = HAHAHA I had to watch the hungarian folk dance on youtube to get it

---

LOGS

# Monday 11:30 AM: i looked at all the files to give me an overview of what i am going to learn this week. Right now, i looked at ex 1,2,3,4 and im now researching what errors there are.

    . logic errors - mathematical/arithmetic mistakes or anything that contains logic really.
    . syntax errors - spelling mistakes/ string mistakes
    . runtime errors - division by zero and running loops (never ending ones i think)

    thats kind of cool. im going to write the basic points of the exercise of what i need to do.
    _______________________________________________________________________________________________________

    Exercise 1 - Test passing (learning about while loops & range)

    l1:
    . use a while loop
    . return a list of numbers using while loop
    . figure out the start number, stop number, increment(fancy word for adding) number

    L2:
    . increment by 2 using range (do it from scratch and one using l1)
    DONE

    L3:
    . OHHHHH YES finally inputs
    . make an input, ask for a number between high and low until it passes

    L4:
    . look for a number in responses, if caught, return the number
    . if there are words or letters, ask again

    L5:
    . combine functions L4 & L3. yuck.

    _______________________________________________________________________________________________________
    Exercise 2 - guessing game

    this one looks so cool

    . figure out what happens if someone answers something out of the range of the code, something the code
    didnt notice.
    . simplify it and make it more robust

    _______________________________________________________________________________________________________

# Thursday

    I lost motivation for this right now, so ill try my best to come up with some codes

     incrementing by 2
    my_list = [1,2,3,4,5,6,7,8,9,10]
    for x in my_list[1::2]:
    print (x)
    i need to use a range function, so lets do that

    for i in range(2, 22, 2):
    print(i, end=' ')

    alright it should work but, there are no integers, soo lets replace the numbers with 'start and stop'


    my_range = []

    for i in range(start, stop, 2):
        my_range.append(i)

    return my_range

    done!!

    ________________________________________________________________________________________________________

# Friday

    Let's try this again. well, start and finish it tonight. let me get my music first (louis armstrong)

    exercise 4:

    5:07 PM - binary searches (reading what i have to do)

    5:15 PM - crying break

    5:17 PM - okay so we have 3 main variable names: low, high, actual_number

    and we have tries & guess here

    tries = 0
    guess = 0

    dictionary, and the algorithm HAS to return this:

# {"guess": guess, "tries": tries}

    and we do a binary search for the ....guessed number? um

    1. range to guess inside
    2. binary search the actual number

    um ok first im going to write a pseudocode for a binary search to make things a bit more clear, and then im going to make a guessing range and then work it out & merge it together with the names. sounds like a solidish plan.

    5:24 PM - dinner brb

# Saturday

    12:27 PM finished the exercise 1 in 20 minutes (new record). ik its not about speed, but im a competitive person, new record anyways.

    the super asker kind of got scary, but after going through it, it was not hard it was the easiest because i just had to combine both of my codes together.
    i kind of wanted to make it simpler but ik future me wont get the simple version, so this time i extended it so it would be easier for me to understand.

    i now know what value errors, keyboard errors are, what exception is and im getting good at looping. finally.

    12:30, lets work on the binary search and then the guessing game! (last two!)

    while loop

    while low <= high
        middle = low/high / 2
        if target = array(middle) then
        found = true

    1. choose a range
    2. guess the number in the range
    3. number of tries of guessing
    4. return number of tries, guesses, and actual number


    print("Guess a number between 1 & 100!")
    actual_number = random.randint(1, 100)
    tries = 0  #  tries to guess the number
    guess = 0
    while guess != actual_number:
        guess = eval(input("Guess a number: "))
        tries += 1
        if guess == actual_number:
            print("thats right! you used", tries, "attempts!")
            break
        elif guess < actual_number:
            print("go higher!")
        else:
            print("go lower!")

    return {"guess": guess, "tries": tries}

---

OKAY lets start again
print(
"Guess a number between {low} and {high}".format(
low=low, high=high, actual_number=actual_number
)
)
actual_number = random.randint(low, high) --> we dont need this beecause the test will have one generated, right? hmm lets check

    tries = 0
    guess = 0

    while guess != actual_number:
        guess = input("Enter an integer: ")
        tries += 1
        try:
            integer = int(guess)
            if integer == actual_number:
                print("u got the number my g")
                return {"guess": guess, "tries": tries}
            elif integer < actual_number:
                print("go higher")
            elif integer > actual_number:
                print("go lower")
        except ValueError:
            print("you cant outsmart me, enter a valid integer")

....
print("Guess a number between {low} and {high}".format(low=low, high=high))

    tries = 0
    guess = 0

    while guess != actual_number:
        guess = input("Enter an integer: ")
        tries += 1
        try:
            integer = int(guess)
            if integer == actual_number:
                print("u got the number")
                return {"guess": guess, "tries": tries}
            elif integer < actual_number:
                print("go higher")
            elif integer > actual_number:
                print("go lower")
        except ValueError:
            print("enter a valid integer")

---- code by some dude
tries = 0
def binarysearch((numlist= low, high), target):
global tries
if len(numlist) == 0:
print("The target is not in this list.")
else:
midpoint_index = len(numlist) // 2
if numlist[midpoint_index] == target:
num_tries += 1
print("The target", target, "was found in", tries, "guesses.")
elif numlist[midpoint_index] < target:
num_tries += 1
print("Guess: ", numlist[midpoint_index], "is too low")
return binarysearch(numlist[midpoint_index + 1:], target)
elif numlist[midpoint_index] > target:
num_tries += 1
print("Guess: ", numlist[midpoint_index], "is too high")
return binarysearch(numlist[:midpoint_index], target)

def listmaker(min, max):
'''Simple ordered numbers list maker'''
alist = []
for x in range(min, max):
alist.append(x)
return alist

---

why doesnt it work??
