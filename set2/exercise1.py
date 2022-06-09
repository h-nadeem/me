"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think because of the square brackets it is defining a list and creating an index for everything in ''
some_words = ["what", "does", "this", "line", "do", "?"]

# finding 'word' in the function some_words & printing it
for word in some_words:
    print(word)

# for loop, it repeats x infinitely times and prints it 
for x in some_words:
    print(x)
# prints both x and word in the function some_Words
print(some_words)

# the length of some_words is greater than 3 than print 'some_words contains more than 3 words'
if len(some_words) > 3:
    print("some_words contains more than 3 words")

# defines usefulfunction and prints the name and useful information of platform
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

#runs function
usefulFunction()
