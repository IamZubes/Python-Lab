t = (1, 2, 3, 4, 5)

print(f"Element at index 2: {t[2]}")

print(f"Element at index -2: {t[-2]}")

print(f"Elements from index 1 to 3: {t[1:4]}")

t2 = (6, 7, 8)
t3 = t + t2
print(f"Concatenated tuple: {t3}")

print(f"Minimum value: {min(t)}")
print(f"Maximum value: {max(t)}")

print(f"Length of the tuple: {len(t)}")

print("Elements in the tuple:")
for element in t:
    print(element)
