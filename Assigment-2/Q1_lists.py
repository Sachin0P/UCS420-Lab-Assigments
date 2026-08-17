ROLL_NO = 1024170302

L = [int(d) * 10 for d in str(ROLL_NO)]

print("i. L =", L)

L.append(55)
print("ii. After append(55):", L)
print("    55 was added at the end, length changed from 10 to 11")

L.insert(3, 99)
print("    After insert(3, 99):", L)
print("    99 was placed at index 3 and every later element shifted right by one")

L.remove(55)
print("iii. After remove(55):", L)

removed = L.pop(0)
print("     After pop(0):", L)
print("     pop() returned the deleted value:", removed)

L.sort()
print("iv. Ascending :", L)

L.sort(reverse=True)
print("    Descending:", L)

print("v. First three:", L[:3])
print("   Last three :", L[-3:])

average = sum(L) / len(L)
above_avg = [x for x in L if x > average]
print("vi. Average of L:", average)
print("    Elements greater than average:", above_avg)
