ROLL_NO = 1024170302

L = [int(d) * 10 for d in str(ROLL_NO)]
scores = tuple(L[:8])
print("scores =", scores)

highest = max(scores)
lowest = min(scores)
print("i. Highest score:", highest, "at index", scores.index(highest))
print("   Lowest score :", lowest, "appears", scores.count(lowest), "time(s)")

reversed_list = list(scores[::-1])
print("ii. Reversed as list:", reversed_list)
print("    A tuple is immutable, so it cannot be reversed in place; slicing builds a new object")

user_score = int(input("iii. Enter a score to search: "))
if user_score in scores:
    print("    ", user_score, "found at first index", scores.index(user_score))
else:
    print("    ", user_score, "is not present in the tuple")

try:
    scores[0] = 100
except TypeError as e:
    print("iv. Error raised ->", type(e).__name__, ":", e)
    print("    Tuples do not support item assignment because they are immutable")
    print("    A list is mutable, so lst[0] = 100 would work fine")

first, second, *rest = scores
print("v. first =", first, "| second =", second, "| rest =", rest)
