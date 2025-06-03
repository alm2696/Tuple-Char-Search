int_tuple = ('Programming', 'with', 'Python', 'Lists', 'AND', 'Tuples')

char_search = input("Enter a character to search for: ").lower()

match_words = []

for word in int_tuple:
    if char_search in word.lower():
        match_words.append(word)

if match_words:
    print("Words that contain '{}':".format(char_search))
    for word in match_words:
        print(word)
else:
    print("No words in the tuple contain '{}'.". format(char_search))