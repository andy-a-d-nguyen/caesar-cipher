import ssl
import nltk
from nltk.corpus import words, names


def encrypt(plaintext, shift_number):
    encrypted_text = ''
    for char in plaintext:
        if char.lower() in char_to_num_dict:
            if char == char.lower():
                shift_value = (char_to_num_dict[char] + shift_number) % 26
                for key in char_to_num_dict:
                    if char_to_num_dict[key] == shift_value:
                        encrypted_text += key
            else:
                shift_value = (char_to_num_dict[char.lower()] + shift_number) % 26
                for key in char_to_num_dict:
                    if char_to_num_dict[key] == shift_value:
                        encrypted_text += key.upper()
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift_number):
    return encrypt(encrypted_text, -shift_number)


def crack(encrypted_text):
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download('words', quiet=True)
    nltk.download('names', quiet=True)

    word_list = words.words()
    name_list = names.words()

    encrypted_words = encrypted_text.split()

    all_possible_plaintexts = []

    for shift_number in range(26):
        possible_plaintext = [decrypt(encrypted_words[0], shift_number)]
        if possible_plaintext[0].lower() in word_list or possible_plaintext[0].lower() in name_list:
            for i in range(1, len(encrypted_words)):
                possible_plaintext.append(decrypt(encrypted_words[i], shift_number))
            all_possible_plaintexts.append(' '.join(possible_plaintext))

    for plaintext in all_possible_plaintexts:
        valid_word_count = 0
        plaintext_words = plaintext.split()
        for word in plaintext_words:
            if word.lower() in word_list or word.lower() in name_list:
                valid_word_count += 1
        if valid_word_count / len(plaintext_words) > .8:
            return plaintext

    return ''


char_to_num_dict = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}
