s = input("enter a string:")

words = s.split()

for word in words:
    print(f"Len of '{word}' is", len(word))