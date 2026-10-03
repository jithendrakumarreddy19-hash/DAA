# Find palindrome strings in an array

n = int(input("Enter number of strings: "))

arr = []

for i in range(n):
    arr.append(input("Enter string: "))

print("Palindrome strings:")

for word in arr:
    if word == word[::-1]:
        print(word)