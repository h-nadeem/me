TODO: Reflect on what you learned this week and what is still unclear.

---

LOOPS

bucket = [] # empty list
for value in range(10): #returns from 0 to 9
print(value) #prints

Tutorial

w - write
r - read
close or else it gives a lock error

url = ..www..
r = requests.get(url)
if r.status code is 200:
X = X.LOADS(R.TEXT)

print (x)

---

DATA PROJECT
I started thinking about my data project, still a bit confused on what I meant to do about it.
I did talk to sir about bushfires - ill research more about it - try to make it more interesting. but its not interesting enough?? i still need to find a data set, something thats interesting to me.

i really like playing chess, its mathematical algorithms and different openings, the strategies, checkmating etc, i could research about the relationship between playing chess and solving problems involving patterns?
but in terms of data sets, what am i going to measure?
i could add data into the sheets,

Is there a relationship between playing chess and solving problems involving patterns?

okay so i found a data set

https://www.kaggle.com/datasets/datasnaek/chess

it talks about game ids, rates, start time/end time, number of turns, game status, winner, time increment, white player id, white player rating, black player id, black player rating, moves in standard chess notation
opening names, opening ply, opening eco,

i might add: blunders, inaccuracies, etc

---

EXERCISES

I am a bit confused on the exercises ever since json was introduced, who is json?? why?? I am also confused about reading, opening, requesting info from urls and different websites/files. i was doing great up until this week, it went from 0 to 100 straight away, but its okay right now im reading the IOexamples (what is IO??) and working my way towards breaking down each example and using the debugging tool/stepping to help me break it down.

---

Using file IO, from the docs:
"The first argument is a string containing the filename. The second
argument is another string containing a few characters describing the
way in which the file will be used. mode can be 'r' when the file will
only be read, 'w' for only writing (an existing file with the same name
will be erased), and 'a' opens the file for appending; any data written
to the file is automatically added to the end. 'r+' opens the file for
both reading and writing. The mode argument is optional; 'r' will be
assumed if it's omitted."

    okay so
    first argument = string with file name
    second argument = string with how the file is used

    there are different types of modes:

    mode r = only reading a file
    mode w = only writing a file
    mode a = opening file for adding extra info
    mode r+ = reading and writing

always CLOSE file when done

---

ok lets figure out how to do these

this is a list = [ 1,2,3,4,5,6,7,8,9]

e.g.
example = [1,2,3,4,5]

to take things out of a list

x = example[0]
x will return 1

lists done!

now dictionaries

json is a file type. and always formatted in dictionaries, and its a nested dictionary (dictionary within a dictionary)

DICTIONARIES ARE PAIRS

dictionary = {key:value, key:pair}
dictionary_example = {name:akasha}

accessing dictionaries:
x = dictionary_example[name]
x will return akasha

exercise 1

results {json file}

inside json file is:

1. {results: [list],
2. info: {}

file = {results: [], info: {} }
x = file ["results"]
x = going to print (results) ->[]

    inside x
    [{}]

    x[0] = {gender }

file
open["filename"]

access from dictionary = .get

e,g, print(data.get("results"))

variable = d.get("variable")
