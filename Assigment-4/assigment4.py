import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

roll_no = "1024170302"

fixed_entries = [
    {"question": "what is the annual fee", "answer": "The annual fee is Rs 500.",
     "keywords": "fee cost price charge", "category": "billing"},
    {"question": "how to reset password", "answer": "Go to Settings > Reset Password.",
     "keywords": "password reset login", "category": "account"},
    {"question": "what are your working hours", "answer": "We are open 9 AM to 5 PM.",
     "keywords": "hours timing open time", "category": "general"},
    {"question": "how can i pay the fee", "answer": "You can pay via UPI, card, or net banking.",
     "keywords": "pay payment upi fee", "category": "billing"},
]

categories = ["billing", "account", "general"]

digit1 = int(roll_no[-2])
digit2 = int(roll_no[-1])

category1 = categories[digit1 % 3]
category2 = categories[digit2 % 3]

print("Digit", digit1, "->", category1)
print("Digit", digit2, "->", category2)

my_entries = [
    {"question": "how do i get a refund",
     "answer": "Refunds are processed within 7 working days.",
     "keywords": "refund money return",
     "category": category1},
    {"question": "where is your office located",
     "answer": "Our office is at Thapar Institute, Patiala.",
     "keywords": "office address location",
     "category": category2},
]

df = pd.DataFrame(fixed_entries + my_entries)

print("\nQ1: Knowledge Base")
print(df)


def score_query(query, df):
    query_words = query.lower().split()
    rows = []

    for i in range(len(df)):
        keywords = df.loc[i, "keywords"].split()

        count = 0
        for word in query_words:
            if word in keywords:
                count = count + 1

        if count > 0:
            confidence = round(count / len(query_words), 2)
            rows.append([df.loc[i, "question"], df.loc[i, "answer"], confidence])

    result = pd.DataFrame(rows, columns=["question", "answer", "confidence"])
    result = result.sort_values("confidence", ascending=False)
    return result


print("\nQ2: Query = 'how do i reset my password'")
print(score_query("how do i reset my password", df))

print("\nQ2: Query = 'what is the fee price'")
print(score_query("what is the fee price", df))


def same_category(category_name, df):
    return df[df["category"] == category_name]["question"]


print("\nQ3: Questions in category", category2)
print(same_category(category2, df))


print("\nQ4: Old keywords:", df.loc[1, "keywords"])
new_keyword = input("Enter a new keyword: ")
df.loc[1, "keywords"] = df.loc[1, "keywords"] + " " + new_keyword
print("New keywords:", df.loc[1, "keywords"])

file_name = roll_no + "data.csv"
df.to_csv(file_name, index=False)
print("Saved to", file_name)


print("\nQ5: Entries per category")
print(df.groupby("category").size())


def score_with_ties(query, df):
    result = score_query(query, df)

    if len(result) == 0:
        print("No match found")
        return

    top_score = result["confidence"].max()
    best = result[result["confidence"] == top_score]

    if len(best) > 1:
        print("Tie found! All best matches:")
    else:
        print("Best match:")
    print(best)


print("\nQ6: Query = 'fee' (tie)")
score_with_ties("fee", df)

print("\nQ6: Query = 'refund' (no tie)")
score_with_ties("refund", df)