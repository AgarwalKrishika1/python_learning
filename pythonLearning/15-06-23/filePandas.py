import pandas as pd
#pandas is used to do table form data
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print('\n')
print('create variable')
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

print('\n named index')
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

print('\n\n import files')
df = pd.read_csv('C:\\Users\LENOVO\Desktop\intership\\report.csv')
print(df)
print('max row', pd.options.display.max_rows)
print(df.info())

#JSON is python dictonary