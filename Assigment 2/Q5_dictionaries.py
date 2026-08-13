my_dict = {
    "name": "Sachin Prakash",
    "roll_no": "1024170302",
    "branch": "COPC",
    "age": 21,
    "city": "Bhopal"
}
print("Original:", my_dict)

my_dict["location"] = my_dict.pop("city")
print("i. Renamed city to location:", my_dict)

my_dict["cgpa"] = 7.8
print("ii. Added cgpa:", my_dict)

my_dict["age"] += 1
print("iii. Age increased to:", my_dict["age"])

copy1 = my_dict.copy()
copy2 = my_dict.copy()

removed_branch = copy1.pop("branch")
print("iv. copy1 after pop:", copy1)
print("    pop() returned:", removed_branch)

del copy2["branch"]
print("    copy2 after del:", copy2)
print("    pop() removes the key and returns its value, del only removes it and returns nothing")

print("v. Key-value pairs:")
for key, value in my_dict.items():
    print(f"   {key} -> {value}")

if "email" in my_dict:
    print("vi. Email:", my_dict["email"])
else:
    print("vi. Email not available for this student")

friend_dict = {
    "name": "Rohan Mehta",
    "roll_no": "1024170399",
    "branch": "CSE",
    "age": 22,
    "city": "Indore"
}
merged = {**my_dict, **friend_dict}
print("vii. Merged:", merged)
print("     For shared keys the rightmost dictionary wins, so friend_dict values overwrite my_dict values")

string_only = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("viii. Only string values:", string_only)
