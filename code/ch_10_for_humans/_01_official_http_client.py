import requests

# from: http://www.omdbapi.com/
title_text = input("Enter a title search string: ")
url = 'http://www.omdbapi.com/?y=&plot=short&r=json&s={}'.format(title_text)

# process json-> Search -> Title
resp = requests.get(url)
if resp.status_code != 200:
    print("Whoa, status code unexpected! {}".format(resp.status_code))
else:
    data = resp.json()
    search = data['Search']
    for m in search:
        print("* {}".format(m['Title']))
