import json


def search():
    search_term = input("Enter search term: ")
    with open("dictionary.json") as data:
        term_data = json.load(data)
    print(f"{search_term}, {term_data[search_term]}")


def write():
    term = input("Enter Term: ")
    term_def = input("Enter Definition: ")

    with open("dictionary.json") as data:
        term_data = json.load(data)
    term_data[term] = term_def

    with open("dictionary.json", "w") as data:
        json.dump(term_data, data)


while True:
    inquiry = input("Enter [1] For Search [2] For Add Term [3] For Exit\n-> ")

    if inquiry == "1":
        search()
    elif inquiry == "2":
        write()
    elif inquiry == "3":
        print("Have a Nice Day!")
        break
    else:
        print("Please write either '1' or '2'")
