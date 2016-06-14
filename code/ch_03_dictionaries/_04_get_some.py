from collections import defaultdict

data = {"year": "2001", "country": "USA", "title": "Johnny 5", "duration": "119 min"}

print('optimistic style')
print("Year is {}".format(data['year']))
# KeyError: 'rating'
# print("Rating is {}".format(data['rating']))
print()
print('pessimistic style')
try:
    print("Year is {}".format(data['year']))
    print("Rating is {}".format(data['rating']))
except:
    pass  # never prints rating
print()
print('safety first style')
if 'year' in data:
    print("Year is {}".format(data['year']))

if 'rating' in data:
    print("Rating is {}".format(data['rating']))
else:
    print("Oh, there is no rating")
print()

print('accept None instead style')
print("Year is {}".format(data.get('year')))
print("Rating is {}".format(data.get('rating')))
print()

print('Explicit alternate value style')
print("Year is {}".format(data.get('year', 0)))
print("Rating is {}".format(data.get('rating', 'NO RATING')))
print()

data2 = defaultdict(lambda: "MISSING", data)
print('accept default value instead style')
print("Year is {}".format(data2['year']))
print("Rating is {}".format(data2['rating']))
print()

