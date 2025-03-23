def count_words(words_to_count):
    word_count = 0
    words = words_to_count.split()

    for word in words:
        word_count += 1
    return word_count

def count_characters(text):
    characters = {}

    for char in text.lower():
        characters[char] = characters.get(char, 0) + 1
    return characters

def sorted_list(char_counts):
    letters = []
    for char, count in char_counts.items():
        char_dict = {"char" : char, "count" : count}
        if char.isalpha():
            letters.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    
    letters.sort(reverse=True, key= sort_on)
    return letters
    