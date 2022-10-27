
import string
alpha_lst = list(string.ascii_lowercase)

# This problem demonstrates the Vigenere Cipher

# text = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
# key = "friends"

# key_length = len(key)
# text_list = text.split(' ')
# print(text_list)

# here we assign the key against each individual letter


def assignment(text_list, key):
    key_phrase = []
    decode_list = []
    # text_list = text.split(' ')
    non_alpha_count = 0
    for word in text_list:
        for i in range(len(word)):
            if not(word[i] in alpha_lst):
                non_alpha_count += 1
        word_length = len(word)
            # print(word_length)
        if word_length <= len(key):
            key_phrase += [key[:word_length-non_alpha_count]]
        else:
            no_of_full_keys = int(word_length / len(key))           # this indicates full word
            text_to_add = ""
            addition = key[:(word_length % len(key))-non_alpha_count]
            for i in range(no_of_full_keys):
                text_to_add += key
            text_to_add += addition
            key_phrase.append(text_to_add)
        conversion(decode_list, word, key_phrase[text_list.index(word)])
        non_alpha_count = 0
    return key_phrase, decode_list


def conversion(decoded_list, word, key_string):
    decoded_text = ""
    for i in range(len(word)):
        if not(word[i] in alpha_lst):
            decoded_text += word[i]
        else:
            if (alpha_lst.index(word[i]) + alpha_lst.index(key_string[i])) < len(alpha_lst):
                decoded_text += alpha_lst[alpha_lst.index(word[i]) + alpha_lst.index(key_string[i])]
            elif (alpha_lst.index(word[i]) + alpha_lst.index(key_string[i])) == len(alpha_lst):
                decoded_text += alpha_lst[(alpha_lst.index(word[i]) + alpha_lst.index(key_string[i]))-1]
            else:
                decoded_text += alpha_lst[(alpha_lst.index(word[i]) + alpha_lst.index(key_string[i])) % len(alpha_lst)]

    decoded_list.append(decoded_text)
    return decoded_list












text = "thanks for the artillery sent over here through the jungle which our enemy least expected and that too with such massive reinforcements."
text_list = text.split(' ')
print(text_list)
print(alpha_lst)
key = "friends"
key_container = []
decoded_list = []
key_container, decoded_list = assignment(text_list, key)
# conversion(text_list, key_container)
print(' '.join(decoded_list))














