import pandas as pd

df = pd.read_csv('enjoysport.csv')
data = df.values

specific = data[0][:-1]
general = [['?' for _ in range(len(specific))] for _ in range(len(specific))]

for row in data:
    if row[-1] == "yes":
        for i in range(len(specific)):
            if row[i] != specific[i]:
                specific[i] = '?'
    else:
        for i in range(len(specific)):
            if row[i] != specific[i]:
                general[i][i] = specific[i]

general = [i for i in general if any(j != '?' for j in i)]

print("\nFinal Specific hypothesis:\n", specific)
print("\nFinal General hypothesis:\n", general)
