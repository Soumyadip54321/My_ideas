
# help("string")
import string
# string.ascii_lowercase
# print(list(string.ascii_lowercase))
alpha_list = list(string.ascii_lowercase)
print(alpha_list)

text = "How are you doing vishal. Hope you're well i write to let you know that i'd need your assistence in winning this war. Hope to get reply from your end soon."

# text_list = text.split(' ')
# print(text)
# offset = 10

def ceaser_cipher_code(message, offset):
    coded_list = []
    for letter in message:
        if not(letter in alpha_list):
            coded_list.append(letter)
            continue
            # print(letter)
        index_in_list = alpha_list.index(letter)
        # print(index_in_list)
        index_offset = index_in_list - offset
        index_offset = index_offset % len(alpha_list)
        # print(letter, index_offset, alpha_list[index_offset])
        coded_list.append(alpha_list[index_offset])
    return ''.join(coded_list)


def ceaser_cipher_decode(message, offset):
    decoded_list = []
    for letter in message:
        if not(letter in alpha_list):
            decoded_list.append(letter)
            continue
            # print(letter)
        index_in_list = alpha_list.index(letter)
        # print(index_in_list)
        index_offset = index_in_list + offset
        index_offset = index_offset % len(alpha_list)
        # print(letter, index_offset, alpha_list[index_offset])
        decoded_list.append(alpha_list[index_offset])
    return ''.join(decoded_list)


text_to_be_decoded = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."


print(ceaser_cipher_code(text, 10))
print(ceaser_cipher_decode(text_to_be_decoded, 7))
# print(decoded_text_list)






