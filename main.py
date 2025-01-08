def read_from_file(path_book):
    with open(path_book) as f:
        return f.read()

def count_word(books):
    return len(books.split())

def count_characters(books):
    lower_text = books.lower()
    count_char = {}

    for c in lower_text:
            if c in count_char and c.isalpha():
                count_char[c] += 1 
            elif c.isalpha():
                count_char[c] = 1
    
    sorted_by_count = dict(sorted(count_char.items(), key=lambda item : item[1], reverse=True))
    return sorted_by_count

def main():
    path_book = "books/frankenstein.txt"
    books_text = read_from_file(path_book)
    count_char = count_characters(books_text)
    print(f"--- Begin report of {path_book} ---")
    print(f"Word in this text is {count_word(books_text)}.")
    for char in count_char:
        print(f"The '{char}' character was found {count_char[char]} times")
    print("--- End report---")


main()