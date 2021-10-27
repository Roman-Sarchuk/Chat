alphabet_ENG = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alphabet_UA = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
alphabet_ENG_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_UA_caps = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
number = '01234567890123456789'

# message = str(input('Ведіть текст... '))


def encryption(text, key=1):
    code = ''
    text = str(text)
    key = key
    for sps in text:
        if sps in alphabet_ENG:
            position = alphabet_ENG.find(sps)
            new_position = position + key
            code = code + alphabet_ENG[new_position]
        elif sps in alphabet_UA:
            position = alphabet_UA.find(sps)
            new_position = position + key
            code = code + alphabet_UA[new_position]
        elif sps in alphabet_ENG_caps:
            position = alphabet_ENG_caps.find(sps)
            new_position = position + key
            code = code + alphabet_ENG_caps[new_position]
        elif sps in alphabet_UA_caps:
            position = alphabet_UA_caps.find(sps)
            new_position = position + key
            code = code + alphabet_UA_caps[new_position]
        elif sps in number:
            position = number.find(sps)
            new_position = position + key
            code = code + number[new_position]
        else:
            code = code + sps
    return code


# encryption(message, 1)
