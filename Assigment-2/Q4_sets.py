ROLL_NO = 1024170302

digits = [int(d) for d in str(ROLL_NO)][:8]
print("Digits used:", digits)

A = {d * 7 for d in digits}
B = {d * 9 for d in digits}
print("A =", A)
print("B =", B)

print("vi. Union A | B:", A.union(B))

print("vii. Intersection A & B:", A.intersection(B))

print("viii. A - B:", A.difference(B))
print("      B - A:", B.difference(A))
print("      difference() is one directional, while symmetric_difference() combines both (A-B) and (B-A)")

print("ix. Symmetric difference:", A.symmetric_difference(B))

print("x. A.issubset(B):", A.issubset(B))
print("   B.issuperset(A):", B.issuperset(A))

X = int(input("xi. Enter a value to discard from A: "))
A.discard(X)
print("    A after discard:", A)
print("    discard() is safer because remove() raises KeyError if the value is absent")
