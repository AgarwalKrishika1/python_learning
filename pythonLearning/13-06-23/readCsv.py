import csv
fields = []
rows = []
with open(r"C:\Users\LENOVO\Desktop\intership\report.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num))
print('Field names are:' + ', '.join(field for field in fields))
print('\nRows are:\n')
for row in rows[0:]:
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')
