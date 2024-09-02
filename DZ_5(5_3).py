import string
input_string = input("Введите строку: ")
cleaned_string = ""
for char in input_string:
    if char not in string.punctuation and char != " ":
        cleaned_string += char
title_case_string = ""
capitalize_next = True
for char in cleaned_string:
    if capitalize_next and char.isalpha():
        title_case_string += char.upper()
        capitalize_next = False
    else:
        title_case_string += char.lower()
hashtag = "#" + title_case_string
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print("Твой хештег:", hashtag)
