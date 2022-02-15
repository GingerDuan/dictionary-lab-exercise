import sys

"""Count words in file."""


def tokenize(file_name):

    full_doc_list = []
    
    for line in open(file_name):

        #make each line readable and iterable and lowercase
        line = line.rstrip()
        words = line.split(" ")
        words_lower = [word.lower() for word in words]

        #extend to full_doc_list
        full_doc_list.extend(words_lower)

    return full_doc_list


def count_words(words):
    """Takes in a list of strings, returns a dictionary with string count"""
    
    #declare empty dictionary
    word_count = {}

    #add to word_count if the key exists, set new key value pair with value = 1 if it doesn't
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count


def print_word_counts(word_count_dict):
    """take a dictory for word_count, and print each key and value"""

    for key,value in word_count_dict.items():
        print(key,value)


doc_list = tokenize(sys.argv[1])
doc_word_count = count_words(doc_list)
print_word_counts(doc_word_count)




    

    





