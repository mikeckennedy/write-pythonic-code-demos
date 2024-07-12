db_is_available = True


def main():
    accounts = find_accounts('python')
    if accounts is not None:
        print("Accounts found: ")
        for a in accounts:
            print(a)
    else:
        print("Error: DB not available")

def find_accounts(search_text):
    # perform search...
    if not db_is_available:
        return None

    # returns a list of account IDs
    return db_search(search_text)


def db_search(search_text):
    if search_text:
        return [1, 11]
    return []


if __name__ == '__main__':
    main()
