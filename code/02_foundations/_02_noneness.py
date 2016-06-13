def find_accounts(search_text):
    # perform search...
    if not db_is_availble:
        return None

    # returns a list of account IDs
    return db_search(search_text)

accounts = find_accounts('python')
if accounts is None:
    print("Error: DB not available")
else:
    print("Accounts found: Would list them here...")























def db_search(search_text):
    return [1, 11]

db_is_availble = True