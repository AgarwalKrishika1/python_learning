import pandas as pd
read_file = pd.read_excel("report.xlsx")
read_file.to_csv('reportTest.csv',
                  index=None,
                  header=True)

df = pd.DataFrame(pd.read_csv("reportTest.csv"))
print(df)
