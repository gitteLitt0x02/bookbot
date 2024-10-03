import re

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
    count = len(result)

    return result, count



def char_counter(file_content):
    lowered = file_content.lower()
    letters = {}
    for char in lowered:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters

def char_presenter(char_func):
    for k,v in char_func.items():
        
        if m := re.match("([a-z])", k):
            print(f"The '{m.group(1)}' character was found {v} times")


def main():
    book_path = "books/frankenstein.txt"
    file_content = get_book_text(book_path)
    word_func = word_counter(file_content)
    char_func = char_counter(file_content)
    #print(word_func[0], '\n')
    #print(word_func[1])

    print(f'--- Begin report of {book_path} ---\n')
    print(f'{word_func[1]} words found in the document \n')
    char_presenter(char_func)
    print('--- End report ---')

if __name__ == "__main__":
    main()