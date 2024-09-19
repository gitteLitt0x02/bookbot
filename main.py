def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
    
def word_counter(file_content, delimiters = ' \t\n'):
    result = []
    word = ''
    for char in file_content:
        if char not in delimiters:
            word += char
        elif word:
            result.append(word)
            word = ''

    if word:
        result.append(word)
    #print("myOwnSplit: ", result)
    return (len(result))

def counter_split(file_content):
    split = file_content.split()
    print("splitCount: ", len(split))

def char_counter(file_content):
    pass
    
def main():
    book_path = "books/frankenstein.txt"
    file_content = get_book_text(book_path)
    print(word_counter(file_content))
    #sprint(file_content)
    word_counter(file_content)
    counter_split(file_content)


if __name__ == "__main__":
    main()