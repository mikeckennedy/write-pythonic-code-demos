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
print(type(movie_data), movie_data)

print("The title is {}".format(movie_data.get('Title')))

movie_json_text_2 = json.dumps(movie_data)
print(type(movie_json_text_2), movie_json_text_2)

# print(type(movie_json), movie_json)
# md = {
#     "Title":"Johnny 5",
#     "Year":"2001",
#     "Runtime":"119 min",
#     "Country":"USA"
#     }
# print(type(md), md)
