
# Index of First Occurrence in a String

s = input("Enter a string: ")
ch = input("Enter character to search: ")

index = -1

for i in range(len(s)):
    if s[i] == ch:
        index = i
        break

print("First occurrence index:", index)
