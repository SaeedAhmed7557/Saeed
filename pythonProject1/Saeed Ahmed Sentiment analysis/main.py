import string
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#reading text file
text = open("read.txt", encoding="utf-8").read()

# converting to lowercase
lower_case = text.lower()

#Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('','', string.punctuation))

# splitting text into words
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing stop words from the tokenized words list
final_words = []

for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

    # NLP Emotion Algorithm
    # 1) Check if the word in the final word list is also present in emotion.txt
    # open the emotion file
    # 2) If word is present -> Add the emotion to emotion list
    # 3) Finally count each emotion in the emotion list

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').strip()
        word, emotion = clear_line.split(':')

    if tokenized_words in final_words:
        emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analysis(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("NEGATIVE")
    elif pos > neg:
        print("POSITIVE")
    else:
        print(" NEUTRAL ")

sentiment_analysis(cleaned_text)
# Plotting the emotions on the graph

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()