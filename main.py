book_path = 'books/frankenstain.txt'

# print out the report
def print_a_book_report(characters):
    for character, amount in characters.items():
        print(f"The '{character}' character was found {amount} times")

# count the words in the book
def count_the_words(text):
    text_as_array = text.split()
    return len(text_as_array)

# count how many times each character used in the book
def count_characters(text):
    result = dict()
    for char in text.lower():
        if char.isalpha():
            try: 
                result[char] = result[char] + 1
            except KeyError:
                result[char] = 1
    return result

# read book from file as string
def read_a_book(path_to_book):
    with open(path_to_book) as file:
        return file.read()

def main():
    book = read_a_book(book_path)
    charachters = count_characters(book)
    print_a_book_report(charachters)
main()