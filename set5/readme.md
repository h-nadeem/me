TODO: Reflect on what you learned this week and what is still unclear.

Let's start the data project this week!

DATA SET: https://data.gov.uk/dataset/723c243d-2f1a-4d27-8b61-cdb93e5b10ff/uk-local-authority-and-regional-greenhouse-gas-emissions

This week task: basic analysis on your data set & (week 5 exercises?)

Saturday 2nd July:

I am so confused right now, which is scary but ill take it slow.

To do: (watch week 4 panda first)

- create a github repo
- add github repo in folder code1161
- load notebook
- go through the notebook
- data analysis on your data set (watch week 5 lecture)

NOTEBOOK:

Finding out if the file path exists & loading it:
(change csv filepath into the same desktop as code1161)
[
if os.path.isfile("penalty_data_set_0.csv"):
filepath = "penalty_data_set_0.csv"
print("loading from file")
else:
filepath = "http://www.osr.nsw.gov.au/sites/default/files/file_manager/penalty_data_set_0.csv"
print("loading from the internet")

penalty_data = pd.read_csv(filepath)
print("done")
]

Spreadsheet of csv file will load

To access rows - ilock property, [1] not [0]

.sample(number) - any random rows

read this: https://tryolabs.com/blog/2017/03/16/pandas-seaborn-a-guide-to-handle-visualize-data-elegantly

---

Exercises 5.2

Italian dinner

        1.  they start with an axiom, which is given of the formal system;
        2.  there are a set of statements inthe formal system which can be
            thought of as theroums of the system; and
        3.  there are a set of rules for transforming any statement which is
            part of the formal system into any other using replacement rules.
    In the itallian dinner, teh axiom is of course _tomatoes_

axiom = _tomatoes_

_tomatoes_

parts = axiom.split(" ")
result = list(map(italian_rules, parts))
new_string = " ".join(result)
guard -= 1
if guard > 0:
return italian_dinner(new_string, guard)
else:
return new_string
