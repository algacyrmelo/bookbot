def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1
    return chars


def sort_on(char_count):
    return char_count[1]


def chars_dict_to_sorted_list(num_chars_dict):
    chars_list = []
    for ch in num_chars_dict:
        count = num_chars_dict[ch]
        chars_list.append((ch, count))
    return sorted(chars_list, reverse=True, key=sort_on)
