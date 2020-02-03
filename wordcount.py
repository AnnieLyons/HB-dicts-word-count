
import sys #Use command line tu run desired .txt file.

def get_words(filename):
    """Return list of words from file"""

    word_list = []

    with open(filename) as text:
        for line in text:
            # strip whitespace from the end of the line
            line = line.rstrip()
            # split it into words 
            words = line.split()

            for word in words:

                # strip common punctuation off word:
                word = word.strip("'\",.!?-#$%^&();:_")

                # lowercase the word 
                word = word.lower()

                # add the word to our list of words
                word_list.append(word)

    return word_list


def count_words(words):
    """Return dictionary of {word: count} from list"""

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_words(word_counts):
    """Print words: count from dictionary"""

    for word, count in word_counts.items():
        print (word, count)

input_filename = sys.argv[1]
word_list = get_words(input_filename)
word_counts = count_words(word_list)
print_words(word_counts)