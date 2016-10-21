def unique_file(input_filename, output_filename):
    input_file = open(input_filename, 'r')
    file_contents = input_file.read()
    input_file.close()
    word_list = file_contents.split()

    file = open(output_filename, 'w')

    unique_words = set(word_list)
    for word in unique_words:
        if word.isalpha() or word.isdigit():
            file.write(str(word) + "\n")
    file.close()