"""
find # and remove the words afterwards
exp str = apple, orange \n #banana and grape \n watermelon, #pineapple
"""

def comment_remover(str):
    sentence_list = str.split('\n')
    final_list = []
    for sentence in sentence_list:
        if "#" in sentence:
            comment_index = sentence.index('#')
            final_list.append(sentence[:comment_index])
        else:
            final_list.append(sentence)
    return '\n'.join(final_list)

print(comment_remover("apple, orange \n #banana and grape \n watermelon, #pineapple"))

