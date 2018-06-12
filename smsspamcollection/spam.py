import pandas as pd
# Dataset from - https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
df = pd.read_table('SMSSPamCollection', sep='\t')
df.columns = ['label', 'sms_message']

# Remap labels to 0 and 1 for easier processing
df['label'] = df.label.map({'ham':0, 'spam':1})

# Output printing out first 5 rows
print(df.head())

# Output size of dataset
print(df.shape)
