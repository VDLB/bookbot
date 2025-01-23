def main():
    with open("books/frankenstein.txt") as i:
        file_contents = i.read()
        word_count = len(file_contents.split())
        letter_count = count_letters(file_contents)
        letter_count.sort(reverse=True, key=dict_sort)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for t in letter_count:
            if t["char"].isalpha():
                print(f"The '{t["char"]}' character was found {t["num"]} times")
        print("--- End report ---")

def count_letters(document):
    letter_list = []
    letter_dict = {}
    for letters in document:
        lower_letter = letters.lower()
        if lower_letter in letter_dict:
            letter_dict[lower_letter] = letter_dict[lower_letter] + 1
        else:
            letter_dict[lower_letter] = 1
    for i in letter_dict:
        letter_list.append({"char":i, "num": letter_dict[i]})
    return letter_list
def dict_sort(dict):
    return dict["num"]
main()
