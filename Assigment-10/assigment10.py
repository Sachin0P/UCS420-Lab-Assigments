import re

import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from textblob import TextBlob
from wordcloud import WordCloud

for package in ["punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4"]:
    nltk.download(package, quiet=True)

roll_no = 1024170302
stop_words = set(stopwords.words("english"))

text = """Space exploration has always fascinated me because it pushes humans beyond what we thought was possible. Telescopes orbiting Earth capture distant galaxies, and their images reveal how stars are born and how they die. Rovers on Mars drill into ancient rocks, searching for signs that water once flowed there. Engineers don't stop at robots, since they're designing rockets that could carry astronauts to Mars. Every mission teaches scientists something new about our planet and our place among the stars. I believe the next great discoveries are waiting for us beyond the Moon."""

print("Q1")
lower_text = text.lower()
clean_text = re.sub(r"[^\w\s]", "", lower_text)
print("Cleaned text:", clean_text)

words = word_tokenize(clean_text)
sentences = sent_tokenize(lower_text)
print("\nWord tokens:", words)
print("\nSentence tokens:", sentences)

split_tokens = text.split()
nltk_tokens = word_tokenize(text)
print("\nsplit() tokens:", split_tokens)
print("\nword_tokenize() tokens:", nltk_tokens)
print("\nsplit() count:", len(split_tokens))
print("word_tokenize() count:", len(nltk_tokens))
print("Only in split():", sorted(set(split_tokens) - set(nltk_tokens)))
print("Only in word_tokenize():", sorted(set(nltk_tokens) - set(split_tokens)))
print("split() breaks only on whitespace, so punctuation stays attached to words.")
print("word_tokenize() separates punctuation and splits contractions such as don't into do and n't.")

filtered_words = [word for word in words if word not in stop_words]
print("\nAfter stopword removal:", filtered_words)

print("\nWord frequency distribution:")
for word, count in FreqDist(filtered_words).most_common():
    print(word, ":", count)

print("\nQ2")
alpha_words = re.findall(r"\b[A-Za-z]+\b", text)
print("Alphabetic words:", alpha_words)

alpha_filtered = [word.lower() for word in alpha_words if word.lower() not in stop_words]
print("\nAfter stopword removal:", alpha_filtered)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stems = [stemmer.stem(word) for word in alpha_filtered]
lemmas = [lemmatizer.lemmatize(word) for word in alpha_filtered]

print(f"\n{'Word':<16}{'Stem':<16}{'Lemma':<16}")
for word, stem, lemma in zip(alpha_filtered, stems, lemmas):
    print(f"{word:<16}{stem:<16}{lemma:<16}")

print("\nStemming cuts word endings by rule, so it is fast but can give non-words such as galaxi.")
print("Lemmatization uses a dictionary, so it gives real words such as galaxy but is slower.")
print("Prefer stemming for search and large-scale text matching where speed matters.")
print("Prefer lemmatization for chatbots and text analysis where meaning and readability matter.")

print("\nQ3")
reviews_q3 = [
    "The camera on this phone is great. The camera takes sharp photos and the photos look great at night.",
    "This laptop has a fast processor. The laptop battery lasts all day and the battery charges fast.",
    "The speakers are loud and the screen is bright, but the screen gets too bright at night and the speakers crackle.",
]

count_vectorizer = CountVectorizer(stop_words="english")
bow = count_vectorizer.fit_transform(reviews_q3)
print("Bag of Words:")
print(pd.DataFrame(bow.toarray(), columns=count_vectorizer.get_feature_names_out()).to_string())

tfidf_vectorizer = TfidfVectorizer(stop_words="english")
tfidf = tfidf_vectorizer.fit_transform(reviews_q3)
feature_names = tfidf_vectorizer.get_feature_names_out()
print("\nTF-IDF:")
print(pd.DataFrame(tfidf.toarray(), columns=feature_names).round(3).to_string())

print("\nTop 3 keywords:")
for number, row in enumerate(tfidf.toarray(), start=1):
    top_indexes = row.argsort()[::-1][:3]
    keywords = [(str(feature_names[i]), round(float(row[i]), 3)) for i in top_indexes]
    print(f"Text {number}:", keywords)
    print(f"Text {number} is mainly about", ", ".join(word for word, score in keywords))
print("These words score highest because they repeat in their own text and are rare in the others.")

print("\nQ4")
ai_text = """Artificial intelligence allows computers to learn patterns from data.
Machine learning models use large amounts of data to make predictions.
Neural networks process images, speech and language with high accuracy.
Companies use these systems to automate decisions and improve services.
Secure and reliable data is essential for training accurate models."""

blockchain_text = """Blockchain is a distributed ledger that records transactions across a network.
Every block stores data and links to the previous block using cryptography.
Network participants verify each transaction without a central authority.
Companies use these systems to track payments and improve transparency.
Secure and reliable data makes the ledger difficult to change."""


def preprocess(input_text):
    cleaned = re.sub(r"[^\w\s]", "", input_text.lower())
    return [word for word in word_tokenize(cleaned) if word not in stop_words]


ai_tokens = preprocess(ai_text)
blockchain_tokens = preprocess(blockchain_text)
print("AI tokens:", ai_tokens)
print("\nBlockchain tokens:", blockchain_tokens)

ai_set = set(ai_tokens)
blockchain_set = set(blockchain_tokens)
jaccard = len(ai_set & blockchain_set) / len(ai_set | blockchain_set)

vectors = TfidfVectorizer().fit_transform([" ".join(ai_tokens), " ".join(blockchain_tokens)])
cosine = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

print("\nShared words:", sorted(ai_set & blockchain_set))
print("Jaccard Similarity:", round(jaccard, 4))
print("Cosine Similarity:", round(float(cosine), 4))
print(f"\nThe texts share {len(ai_set & blockchain_set)} of {len(ai_set | blockchain_set)} unique words, so both scores are low.")
print("Jaccard counts each word once, so it only shows how much vocabulary overlaps.")
print("Cosine also uses word frequency, so the repeated shared word data adds more to its score.")
print("Cosine gives better insight here because it reflects how important the shared words are in each text.")

print("\nQ5")
reviews = [
    "The headphones are amazing and the sound quality is excellent.",
    "Delivery was fast and the customer support team was friendly and helpful.",
    "I love this wonderful blender, it is the best purchase I have made.",
    "The battery is terrible and the charger stopped working, a very disappointing purchase.",
    "The app is slow and the screen looks awful.",
    "The package contains one charger and two cables.",
]

positive_reviews = []
for review in reviews:
    sentiment = TextBlob(review).sentiment
    if sentiment.polarity > 0:
        label = "Positive"
        positive_reviews.append(review)
    elif sentiment.polarity < 0:
        label = "Negative"
    else:
        label = "Neutral"
    print(review)
    print(f"Polarity: {sentiment.polarity:.3f}  Subjectivity: {sentiment.subjectivity:.3f}  Sentiment: {label}\n")

cloud = WordCloud(width=800, height=400, background_color="white", random_state=42).generate(" ".join(positive_reviews))
plt.figure(figsize=(10, 5))
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Positive Reviews")
plt.show()

print("Q6")
training_text = """The ocean is wide and the ocean is deep. The waves rise with the wind and fall on the shore. Sailors watch the sky and follow the stars across the water. The wind carries the ships over the deep blue water. Fish swim under the waves and birds fly over the shore. The moon pulls the tide and the tide covers the sand. Children play on the sand and collect shells near the water. At night the stars shine over the quiet ocean. The sailors sing and the ships return to the shore. The ocean gives life to the land and the sky."""

tf.keras.utils.set_random_seed(roll_no)

tokenizer = Tokenizer()
tokenizer.fit_on_texts([training_text])
vocab_size = len(tokenizer.word_index) + 1
print("Vocabulary size:", vocab_size)

sequences = []
for line in training_text.split(". "):
    tokens = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(tokens)):
        sequences.append(tokens[:i + 1])

max_length = max(len(sequence) for sequence in sequences)
padded = pad_sequences(sequences, maxlen=max_length, padding="pre")
X, y = padded[:, :-1], padded[:, -1]
print("Input sequences:", X.shape)

model = Sequential([
    Embedding(vocab_size, 32),
    LSTM(100),
    Dense(vocab_size, activation="softmax"),
])
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
history = model.fit(X, y, epochs=300, verbose=0)
print("Final accuracy:", round(history.history["accuracy"][-1], 4))


def generate_text(seed_text, next_words=10):
    for _ in range(next_words):
        tokens = tokenizer.texts_to_sequences([seed_text])[0]
        tokens = pad_sequences([tokens], maxlen=max_length - 1, padding="pre")
        predicted = int(np.argmax(model.predict(tokens, verbose=0)))
        seed_text += " " + tokenizer.index_word[predicted]
    return seed_text


print("\nGenerated text:")
for seed in ["ocean", "wind", "stars"]:
    print(generate_text(seed))
