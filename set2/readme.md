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
if - conditional 
for, while, repeat until - loops
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

     LOOPS - pyramid of stars

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

    um WHAT 

for i in range(5):
    for s in range(-6, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()

    maybe? i4ehr84ur3[1n9cj
     im going to $£^%*&


     let me start over fresh.
    i will equal 0 and j will equal lets say 5.

   i = 0
   j = 5
    WHILE i < 5 :
    print ( " "*((j-1)*2) + '* '*((i*2)+1))

    i += 1
    j -= 1

    lets try. didnt work. 

    n = []
    for i in range(n):
        print( " "*(n-i-1) + "*"*(2*i+1) )
    return n



    n = 5
    for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()

             i  line:      "       **************"
      *        0  [1:][:7]    [      *]
     ***       1  [2:][:8]     [     ***]
    *****      2  [3:][:9]      [    *****]
   *******     3  [4:][:10]      [   *******]
  *********    4  [5:][:11]       [  *********]
 ***********   5  [6:][:12]        [ ***********]
*************  6  [7:][:13]         [*************]


            leading  stars    total
                 spaces   count    length
                          (2i+1)   (n+i)
      *            6       1       7  = n+0
     ***           5       3       8  = n+1
    *****          4       5       9  = n+2
   *******         3       7       10 = n+3
  *********        2       9       11 = n+4
 ***********       1       11      12 = n+5
*************      0       13      13 = n+6

x=8
for i in range(1,x):
    print((' '*(x-i))+('*'*i)+('*'*(i-1)))

    return x?
    return

    n=7
pyramid = [f"{'*'*(2*i+1):>{n+i}}" for i in range(n)] # list of lines
print(*pyramid,sep="\n")  
HUH
how do i return this?!

    n=7
    pyramid = [f"{'*'*(2*i+1):>{n+i}}" for i in range(n)] # list of lines
    print(*pyramid,sep="\n") 

    n = []



j = 10
    j  = j-1
    for i in range(1, 10, 2):
    
        return(j*' '+i*'*')

    num_square = []
    for i in range(10):
        coordinates_row = []
        for j in range(5):
            coordinates_row.append('(i{}, j{})'.format(i, j))
        num_square.append(coordinates_row)
    return(num_square)


    ok i need to append.

    


    ______________________________________________________

    the wedges wont work.

    im going to go into the test file and work my way backwards.
    ok it works now.