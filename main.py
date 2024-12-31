def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()
        
def count_chars(text):
    count_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in count_dict:
            count_dict[lower_char] = 1
        else:
            count_dict[lower_char] += 1
    return count_dict

def sort_dict(char_dict):
    new_dict = {v: k for k, v in char_dict.items() if k.isalpha() == True}
    new_dict = dict(sorted(new_dict.items(), reverse = True))
    return new_dict

def report(path, num_words, dict_char):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    sorted_dict = sort_dict(dict_char)
    for key in sorted_dict:
        print(f"The {sorted_dict[key]} character was found {key} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    dict_char = count_chars(text)
    report(book_path, num_words, dict_char)
    
main()