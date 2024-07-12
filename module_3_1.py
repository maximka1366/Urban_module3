def string_info(stroka: str):
    global calls
    calls += 1
    return ( len(stroka), stroka.upper(), stroka.lower())

def is_contains(stroka: str, list_to_search: list):
    global calls
    calls += 1
    stroka = stroka.lower()
    for i in range(0, len(list_to_search)):
        low_reg = str(list_to_search[i])
        list_to_search[i] = low_reg.lower()
    if  list_to_search.count(stroka):
        return True
    else:
        return False


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban','Urban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)