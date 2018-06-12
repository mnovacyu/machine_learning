# This is a manual implementation of the Bag of Words concept
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

print("ORIGINAL DATASET: %s\n" % documents)

# Convert all strings in documents set to their lower case
lower_case_documents = []

for i in documents:
    lower_case_documents.append(i.lower())
print("LOWERCASE: %s\n" % lower_case_documents)

# Remove all punctuations from the strings in the document set
import string

sans_punctuation_documents = []
translator=str.maketrans('','',string.punctuation)

for i in lower_case_documents:
    sans_punctuation_documents.append(i.translate(translator))
print("NO PUNCTUATION: %s\n" % sans_punctuation_documents)

# Tokenize the document set by splitting into individual words using a delimiter
preprocessed_documents = []
for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split(' '))
print("TOKENIZED: %s\n" % preprocessed_documents)

# Count frequencies
