def get_num_words(text):
    return len(text.split())

def get_num_letters(text):
    counted = {}

    for l in text.lower():
        if l not in counted:
            counted[l] = 1
        else:
            counted[l] += 1
    return counted

def sort_characters(characters):
    return sorted(characters.items(), key=lambda item: item[1],  reverse=True)
