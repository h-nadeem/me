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

    12:30, lets work on the binary search (last one!)
