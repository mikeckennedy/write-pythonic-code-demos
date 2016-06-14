# ############ merging dictionaries #############
# Create by Michael Kennedy (@mkennedy)
#
# Overview:
# Often we have multiple dictionaries and want to combine
# them. For example, in Pyramid, we have separate dictionaries
# that hold query string data, route data, and POST data. Merging
# these makes access form data easier. That's just one example.
#

route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}

print("Individual dictionaries: ")
print("route: {}".format(route))
print("query: {}".format(query))
print("post:  {}".format(post))

# Non-pythonic procedural way
m1 = {}
for k in query:
    m1[k] = query[k]
for k in post:
    m1[k] = post[k]
for k in route:
    m1[k] = route[k]

# Classic pythonic way:
m2 = query.copy()
m2.update(post)
m2.update(route)

# Via dictionary comprehensions:
m3 = {k: v for d in [query, post, route] for k, v in d.items()}

# Python 3.5+ pythonic way, warning crashes on Python <= 3.4:
m4 = {**query, **post, **route}

print(m1)
print(m2)
print(m3)
print(m4)

print("Are the same? " + 'yes' if m1 == m2 and m2 == m3 and m3 == m4 else 'no')







#  m3 = {k: v for d in [query, post, route] for k, v in d.items()}
#  m4 = {**query, **post, **route}
