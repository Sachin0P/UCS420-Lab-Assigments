import re
import string

import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import LancasterStemmer, PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize

for package in ["punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4"]:
    nltk.download(package, quiet=True)

text = """Cricket isn't just a sport in India, it's a passion that unites millions of fans. A standard pitch is 22 yards long, and the ball weighs about 5.5 ounces. Modern teams rely on state-of-the-art analytics to plan every over. India won the World Cup in 1983 and again in 2011, and those victories still inspire young players. T20 matches are fast-paced and usually finish in about 3.5 hours. Our local club posts fixtures at https://www.example.com/cricket, and you can reach us at fans@example.com, 123-456-7890 or +91 9876543210."""

print("Q1")
lower_text = text.lower()
clean_text = lower_text.translate(str.maketrans("", "", string.punctuation))
print("Cleaned text:", clean_text)

words = word_tokenize(clean_text)
sentences = sent_tokenize(lower_text)
print("\nWord tokens:", words)
print("\nSentence tokens:", sentences)

stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word not in stop_words]
print("\nAfter stopword removal:", filtered_words)

frequency = FreqDist(filtered_words)
print("\nWord frequency distribution:")
for word, count in frequency.most_common():
    print(word, ":", count)

print("\nQ2")
porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

print(f"{'Word':<28}{'Porter':<28}{'Lancaster':<28}{'Lemma':<28}")
for word in filtered_words:
    print(f"{word:<28}{porter.stem(word):<28}{lancaster.stem(word):<28}{lemmatizer.lemmatize(word):<28}")

print("\nQ3")
print("Words with more than 5 letters:", re.findall(r"\b[A-Za-z]{6,}\b", text))
print("Numbers:", re.findall(r"\b\d+(?:\.\d+)?\b", text))
print("Capitalized words:", re.findall(r"\b[A-Z][a-zA-Z]*\b", text))

alphabet_words = [word for word in re.split(r"[^A-Za-z]+", text) if word]
print("Alphabet-only words:", alphabet_words)
print("Words starting with a vowel:", [word for word in alphabet_words if word[0].lower() in "aeiou"])

print("\nQ4")


def custom_tokenize(input_text):
    return re.findall(r"\d+\.\d+|\d+|[A-Za-z]+(?:['-][A-Za-z]+)*", input_text)


print("Custom tokens:", custom_tokenize(text))

replaced_text = re.sub(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b", "<EMAIL>", text)
replaced_text = re.sub(r"(?:https?://|www\.)\S*[^\s.,;:!?)]", "<URL>", replaced_text)
replaced_text = re.sub(r"\+\d{1,3}\s?\d{10}\b|\b\d{3}-\d{3}-\d{4}\b", "<PHONE>", replaced_text)
print("\nAfter substitutions:", replaced_text)
