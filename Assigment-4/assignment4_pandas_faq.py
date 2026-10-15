import pansachindas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", 60)

ROLL_NO = "1024170302"

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

last_two = [int(d) for d in ROLL_NO[-2:]]
print("Last two digits:", last_two)

for d in last_two:
    print(f"digit {d} -> {d} % 3 = {d % 3} -> {categories[d % 3]}")

personal_entries = [
    {"question": "how do i get a refund",
     "answer": "Refunds are processed within 7 working days to the original payment method.",
     "keywords": "refund money return",
     "category": categories[last_two[0] % 3]},
    {"question": "where is your office located",
     "answer": "Our office is at Block B, Thapar Institute, Patiala.",
     "keywords": "office address location",
     "category": categories[last_two[1] % 3]},
]

df = pd.DataFrame(fixed_entries + personal_entries)
print("\nQ1: Final Knowledge Base")
print(df)

def score_query(query, df):

    query_words = set(query.lower().split())
    results = []

    for idx, row in df.iterrows():
        kw = set(row["keywords"].split())
        matches = query_words & kw
        if len(matches) == 0:
            continue

        confidence = len(matches) / len(query_words)
        results.append({
            "question": row["question"],
            "answer": row["answer"],
            "matched": ", ".join(sorted(matches)),
            "confidence": round(confidence, 2),
        })

    results = sorted(results, key=lambda r: r["confidence"], reverse=True)
    return pd.DataFrame(results)

print("\nQ2: Scoring 'how do i reset my password'")
print(score_query("how do i reset my password", df))

print("\nQ2: Scoring 'what is the fee price'")
print(score_query("what is the fee price", df))

def same_category(category_name, df):

    return df[df["category"] == category_name]["question"]

my_cat = personal_entries[1]["category"]
print(f"\nQ3: All questions in category '{my_cat}'")
print(same_category(my_cat, df).to_string())

entry_idx = 1
print(f"\nQ4: Current keywords for '{df.loc[entry_idx, 'question']}': {df.loc[entry_idx, 'keywords']}")

new_kw = input("Enter a new keyword to add: ").strip().lower()

if new_kw and new_kw not in df.loc[entry_idx, "keywords"].split():
    df.loc[entry_idx, "keywords"] += " " + new_kw
    print("Updated keywords:", df.loc[entry_idx, "keywords"])
else:
    print("Keyword empty or already present, nothing changed.")

filename = f"{ROLL_NO}_faq_data.csv"
df.to_csv(filename, index=False)
print("Saved to", filename)

print("\nQ5: Entries per category")
print(df.groupby("category").size())

def score_query_with_ties(query, df):
    ranked = score_query(query, df)

    if ranked.empty:
        print("No matching entry found.")
        return

    top = ranked["confidence"].max()
    best = ranked[ranked["confidence"] == top]

    if len(best) > 1:

        print(f"Tie! {len(best)} entries share the top confidence ({top}):")
        for _, r in best.iterrows():
            print(f"  - {r['question']} -> {r['answer']}")
    else:
        r = best.iloc[0]
        print(f"Best match ({top}): {r['question']} -> {r['answer']}")

print("\nQ6: Query with a tie -> 'fee'")
score_query_with_ties("fee", df)

print("\nQ6: Query without a tie -> 'refund'")
score_query_with_ties("refund", df)