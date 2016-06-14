import json

movie_json = """
{
"Title":"Johnny 5",
"Year":"2001",
"Runtime":"119 min",
"Country":"USA"
}
"""

movie_data = json.loads(movie_json)
# print(movie_data)
print("Movie title from static json:")
print(' * ' + movie_data['Title'])
print()
print("Movie data to json:")
print(json.dumps(movie_data))
