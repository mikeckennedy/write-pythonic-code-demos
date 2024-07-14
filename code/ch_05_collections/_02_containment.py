nums_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
nums_set = {1, 1, 2, 3, 5, 8, 13, 21, 34}
nums_dict = {1: "one", 2: "two", 3: "three", 5: "five"}

print(f"List: {nums_list}")
print(f"Set:  {nums_set}")
print(f"Dict: {nums_dict}")

n = int(input("Enter a number to test for small fibonacci: "))

# is this number in the sequences above?
print(f"{n} in list" if n in nums_list else "not in list")
print(f"{n} in set" if n in nums_set else "not in set")
print(f"{n} in dict" if n in nums_dict else "not in dict")

text = "Why did the multithreaded chicken cross the street? Other side to the get."

word = input("Enter word to search text for...")
# if word in text:
if text.find(word) >= 0:
    print(f"{word} is in {text}")
else:
    print(f"{word} is NOT in {text}")
