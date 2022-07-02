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
