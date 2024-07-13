#import csv
#with open(r"C:\Users\LENOVO\Desktop\intership\report.csv") as csvfile:
#   reader_variable = csv.reader(csvfile, delimiter=",")
#       for row in reader_variable:
#           print(row)

import csv
with open(r"C:\Users\LENOVO\Desktop\intership\report.csv") as file:
    for i in csv.DictReader(file):
        print (dict(i))