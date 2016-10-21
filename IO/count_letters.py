import collections
import string

def count_letters(filename, output_filename, case_sensitive=False):
    with open(filename, 'r') as f:
        original_text = f.read()
        word_list = original_text.split()
        word_list2 = [word for word in word_list if word.isalpha()]
        original_text = ' '.join(word_list2)

    if case_sensitive:
        alphabet = string.ascii_letters
        text = original_text
    else:
        alphabet = string.ascii_lowercase
        text = original_text.lower()
    alphabet_set = set(alphabet)
    counts = collections.Counter(c for c in text if c in alphabet_set)

    #for letter in alphabet:
    #    print(letter, counts[letter])
    #print("total:", sum(counts.values()))
    file = open(output_filename, 'w')
    for letter in alphabet:
        file.write(str(letter)+' '+str(counts[letter]) + "\n")
    file.close()

    return counts