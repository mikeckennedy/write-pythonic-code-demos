import json

movie_json = """
{
    "title": "Johnny 5",
    "year": 2001,
    "runtime": "119 min",
    "country": "USA"
}""".strip()

# If it were a file
# with open('some-file', 'r', encoding='utf-8') as fin:
#     movie_data = json.load(fin)

# Get movie data from string
movie_data = json.loads(movie_json)
movie_data['year'] = "2012"

# What's the title?
print(type(movie_data), type(movie_json))
print(movie_data['title'])
print(movie_data.get('title'))
print(movie_data.get('title', "NO_TITLE"))

# Back to JSON
movie_json_generated = json.dumps(movie_data, indent=2)
print(movie_json_generated)
print(movie_json == movie_json_generated)
