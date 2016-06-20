
# from: http://www.omdbapi.com/
title_text = input("Enter a title search string: ")
url = 'http://www.omdbapi.com/?y=&plot=short&r=json&s={}'.format(title_text)

# process json-> Search -> Title
