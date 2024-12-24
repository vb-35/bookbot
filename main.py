def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    num_words=get_number_words(text)
    print(f"{num_words} words found in the document")
    dico=count_character(text)
    sorted_dico=sorted(dico.items(),key=lambda item: item[1],reverse=True)
    for k,v in sorted_dico:
        print(f"The '{k}' character was found {v} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_words(string):
    return len(string.split())

def count_character(string):
    string=string.lower()
    dic={}
    alphabet=list(map(chr, range(ord('a'), ord('z')+1)))
    for char in alphabet:
        dic[char]=string.count(char)
    return dic

main()