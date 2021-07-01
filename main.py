import csv

vocab = []    # words in one col
trainFeat = []   # 0s and 1s in lots of rows and cols
trainLabels = []    # 0s and 1s in one col, 1 for spam and 0 for ham
testFeat = []        # 0s and 1s in lots of rows and cols
testLabels = []     # 0s and 1s in one col
Ns = 0
Nsj = 0
Nh = 0
Nhj = 0

"""
vfile_trainLabels = open("trainLabels.csv")
read_csv_trainLabels = csv.reader(vfile_trainLabels)

for row in read_csv_trainLabels:
    if row[0] is '0':
        Nh += 1
    if row[0] is '1':
        Ns += 1
"""

# The following three functions calculate how many emails are spam or ham that contain a given word
# from list "vocab"
# Return the row number for a given word
def test_j(j):
    vfile_vocab = open("vocab.csv")
    read_csv_vocab = csv.reader(vfile_vocab)
    row_num = 0
    for word in read_csv_vocab:
        if word[0] == j:
            return row_num
        row_num += 1

# Find how many emails contain that word
# Return "emails" which are a list of row numbers
def find_emails(word):
    emails = []
    vfile_trainFeat = open("testFeat.csv")
    read_csv_trainFeat = csv.reader(vfile_trainFeat)
    email_row_num = 0
    for email in read_csv_trainFeat:
        if email[word] == '1':
            emails.append(email_row_num)
        email_row_num += 1
    return emails


def determine_spam_ham(emails):
    spam = 0
    ham = 0
    answers = []
    vfile_trainLabels = open("testLabels.csv")
    read_csv_trainLabels = csv.reader(vfile_trainLabels)
    i =0
    for row in read_csv_trainLabels:
        if emails.__contains__(i):
            if row[0] == '0':
                ham += 1
            if row[0] == '1':
                spam += 1
        i += 1
    answers.append(spam)
    answers.append(ham)
    return answers

# Word to test
word = "money"

# Returns row number of where the given word occurs
vocab_row = test_j(word)

# Returns list of row numbers representing emails where word occurs
emails = find_emails(vocab_row)

# Returns array of two elements, first is number of spam emails
# where the given word occurs and second is number of ham emails
answers = determine_spam_ham(emails)
spam = answers[0]
ham = answers[1]
print("the word ", word, " appears in ", spam, " spam emails and ", ham, " ham emails")





vfile_vocab = open("vocab.csv")
read_csv_vocab = csv.reader(vfile_vocab)
#print(len(read_csv_vocab))
#print(read_csv_vocab.__contains__('open'))




#   The training data matrixtrainFeatis aD×Wmatrix,where each row represents an email and each column indicates whether that word appears in thatemail at least once.

# for loop through vocab until you find word with if statement, save what row that word is in
# send that number over to trainFeat, how many trainFeat rows have a 1 for that specific num that you sent
# from vocab?  Capture list of these rows and then go to trainLabels, list the 0's for ham and 1's for span





# vocab.append(row[0])

"""
vfile1 = open("trainFeat.csv")
read_csv1 = csv.reader(vfile1)

for row in read_csv1:
    r = []
    for col in row:
        r.append(int(col))
    trainFeat.append(r)

print(len(trainFeat))
print(trainFeat)
# for r in read_csv:
#   vocab.append([c for c in read_csv])


print(len(vocab))
print(vocab.__contains__('open'))
"""