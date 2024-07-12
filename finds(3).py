import pandas as pd

df = pd.read_csv('enjoysport.csv')
h = ['0'] * (df.shape[1] - 1)
hp, hn = [], []

for row in df.values:
    if row[-1] != 'no':
        hp.append(row)
    else:
        hn.append(row)

for pos in hp:
    for i in range(len(h)):
        if h[i] == '0':
            h[i] = pos[i]
        elif h[i] != pos[i]:
            h[i] = '?'

print(f'Positive Hypotheses:\n{hp}')
print(f'Negative Hypotheses:\n{hn}')
print(f'Maximally Specific Hypothesis:\n{h}')
