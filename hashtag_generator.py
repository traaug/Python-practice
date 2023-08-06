"""
add # in the first place
remove space, capitalize the first letter,
if no string,give false
if final result > 140, give false
"""

def hashtag_generator(str):
    if len(str) == 0:
        return False
    word_list = []
    words = str.split()
    for word in words:
        word_list.append(word.capitalize())

    hashtag_str = "#" + "".join(word_list)
    if len(hashtag_str) > 140:
        return False
    return hashtag_str

print(hashtag_generator("hello my name is traaug"))
