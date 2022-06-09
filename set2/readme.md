TODO: Reflect on what you learned this week and what is still unclear.

def function name(number): 
    answer = number + 1
    return answer

    creates a function that increments the number which is the answer (number+1) and then returns


the_answer = a_string.upper()
    return the_answer

this is for changing the string to upper case. (.lower() if changing to lowercase)


______________________________________________________________________
Vocabulary 
Calling - calls the function 
float - anything with a decimal

- - - - - - - - - 
Exercise 3
odd - true or false
if its true or false - its a boolean. so a boolean function is used. i have to try and write out 
a line of code that returns true or false if a number is odd - and that number is given in the test, 2 and 5.

return(bool(a_number % 2 == 0)) - didnt work? idk why, i tested it (maybe bool isnt a correct function?)
i know that this is how its formatted - well im guessing, let me play around with it.

return(bool(a_number % 2 =/= 0)) maybe if its not equal to zero? idk how to type that symbol, let me google it

ok so the operator is (!=)

let me try again.

return(bool(a_number % 2 != 0)) there? lets check. 

it works. i am amazing. 

ok next one.


- - - - - - - - - 
Engineering Fundamentals

alot of if, elif and else statements because its conditional / decisions 


does it move 
                NO - should it  - YES - industrial glue 
                                - NO - no problem

                YES - should it - YES - no problem
                                - NO - tape

it kind of looks like a tree branch/diagram
i think my first conditional statement is going to be an 'IF', i need parameters now.

i think 'move' and 'should it' be parameters/functions, since both of YES and NO have a 'no problem' in common
i think in my code i should include an 'AND'

IF move AND should_it:
    return 'No problem'  
elif move and not should_it:
    return 'Tape'
elif not move and not should_it:
    return 'No problem'
else:
    return 'Industrial glue'

    i know its formatted like this. lets give it a try?

ok the function names are 'moves and should moves' ill change it.

If moves and should_move:
    return 'No Problem'
elif moves and not should_move:
    return "Sticky Tape"
elif not moves and not should_move:
    return 'Industrial Glue'
else: 
    return "Try again"

i mean it works. 

    um we have an extra challenge. lets cut it down to 3 lines. 


    range? we can use that function but i think that function only works 

    OMG  a dictionary. what if i make a dictionary to simplify??? would it work idk maybe its worth trying it out

    um lets see
     nevermind :( idk how. ill get back to it at the end.



     - - -- - - -- - 

     LOOPS 

     pyramid 

     hm ok 

 rows = int(input("Enter number of rows: ")) - we dont really need this line 

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()   

        idk how to return this. 
k = 0 
for i in range(1, rows+1):
    for space in range(1, (rows - i) +1):
    return(end= '')