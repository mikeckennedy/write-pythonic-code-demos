from collections import defaultdict

data = {"year": 2001, "country": "USA", "title": "Johnny 5", "duration": "119 min"}

print('optimistic style')
print(data['year'])
# print(data['rating']) # Crash!

print()
print('pessimistic style')
try:
    print(data['year'])
    print(data['rating'])
except Exception as x:
    print("Oops! {}".format(x))


print()
print('safety first style')
if 'year' in data:
    print(data['year'])
if 'rating' in data:
    print(data['rating'])
else:
    print("Oh we didn't find a rating...")
print()

print('accept None instead style')
print(data.get('year'))
print(data.get('rating'))
print()

print('Explicit alternate value style')
print(data.get('year', 0))
print(data.get('rating', '***'))
print()

data = defaultdict(lambda: "MISSING", data)
print('accept default value instead style')
print(data['year'])
print(data['rating'])
print()
