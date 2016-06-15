nums_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
nums_set = {1, 1, 2, 3, 5, 8, 13, 21, 34}
nums_dict = {1: "one", 2: "two", 3: "three", 5: "five"}

print("List: {}".format(nums_list))
print("Set:  {}".format(nums_set))
print("Dict: {}".format(nums_dict))

n = int(input("Enter a number to test for small fibonacci: "))

# is this number in the sequences above?
print("{} in list".format(n) if n in nums_list else "not in list")
print("{} in set".format(n) if n in nums_set else "not in set")
print("{} in dict".format(n) if n in nums_dict else "not in dict")

text = "Why did the multithreaded chicken cross the street? Other side to the get."

word = input("Enter word to search text for...")
# if word in text:
if text.find(word) >= 0:
    print("{} is in {}".format(word, text))
else:
    print("{} is NOT in {}".format(word, text))
