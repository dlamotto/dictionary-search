
def read_file(f):
    """Reads a file, if not found returns the fileNotFoundError, and replaces all '\n' with a ' '

        Args:
            f: the .txt file to be read

        Returns:
            A list containing the contents of the .txt file
        """
    # tries to open the file and if not found returns the error
    try:
        f = open(f, 'r')
    except FileNotFoundError as e:
        print(f"{e}")
    lines = f.readlines()
    new_list = []

    # removes all \n from the file
    for line in lines:
        new_list.append(line.replace('\n', ' '))
    return new_list


def make_dictionary(mydict):
    """Builds a dictionary of each word and each line the word can be found on

        Args:
            mydict: an enumerated list with the line number followed by the contents of that line

        Returns:
            A dictionary of each word and each line the word can be found on, ex a: [1,1,4,48]
        """
    dictionary = {}
    i = 1  # actual number of the first line, rather than the index starting at 0

    # creates the dictionary
    for key in mydict:
        for word in (mydict[i]):
            if word.lower() not in dictionary.keys():
                count = []
                count.append(i)
                dictionary[word.lower()] = count
            else:
                count = dictionary[word.lower()]
                count.append(i)
                dictionary[word.lower()] = count
        i = i + 1

    return dictionary


def make_inverse_index(file_to_read):
    """Creates an enumerated list with each line of content split into individual strings

        Args:
            file_to_read: the .txt file to be read

        Returns:
              A dictionary of each word and each line the word can be found on, ex a: [1,1,4,48]
        """
    inverse_index = {}
    f = read_file(file_to_read)

    # enumerates each line of the file starting at line 1
    lines = (list(enumerate(f, 1)))

    # splits each line by ' ' into individual strings
    for index, element in lines:
        inverse_index[index] = element.split()
    return make_dictionary(inverse_index)


def or_search(inverseindex, queries):
    """Searches for all every appearance of the queries

        Args:
            inverseindex:  A dictionary of each word and each line the word can be found on, ex a: [1,1,4,48]
            queries: a list of strings to search for
        """

    pages = []
    for query in queries:
        if query in inverseindex:
            for i in inverseindex[query]:
                pages.append(i)
    result = []
    [result.append(x) for x in pages if x not in result]
    print("Lines with any of the words {} in the query:{}".format(queries, result))


def and_search(inverseindex, queries):
    """Searches for appearances of the both queries

        Args:
            inverseindex:  A dictionary of each word and each line the word can be found on, ex a: [1,1,4,48]
            queries: a list of strings to search for
        """
    pages = []
    for query in queries:
        if query in inverseindex:
            pages.append(inverseindex[query])
    print(pages)
    result = []
    for item in pages[0]:
        for item2 in pages[1]:
            if item == item2:
                result.append(item)
    new_list = []

    # removes duplicates
    [new_list.append(x) for x in result if x not in new_list]

    print("Lines with all of the words {} in the query:{}".format(queries, new_list))


def user_input_words():
    """Gets the text file to read and  the queries to search for
            """
    queries = []
    file_to_read = input("Enter the text file you would like to search (in this format \"stories.txt\"): ")
    file_name = file_to_read.split(".")
    if file_name[1].lower() != 'txt':
        print("Not a valid file. The file needs to be a .txt\n")
        user_input_question()
    else:
        inverseindex = make_inverse_index(file_to_read)
    word = input("Enter the word to search for in the text: ")
    queries.append(word.lower())
    another_word = input("Do you want to search for an additional word? (Y/N) ")
    if another_word.lower() == 'y':
        extra_word = input("Enter another word: ")
        queries.append(extra_word.lower())
        return queries, inverseindex
    elif another_word.lower() == 'n':
        return queries, inverseindex
    else:
        print("Not a valid response.")


def user_input_question():
    """Asks the user which search they would like to perform and calls the search methods
            """
    queries, inverseindex = user_input_words()
    print("Do you want to search for any of the words or all of the words?")
    print("Ex. any of the words would search for any instance of 'dance' and 'class'")
    print("and all of the words would search for instances of 'dance' and 'class'\n")
    answer = input("Enter 'any' for the first option and 'all' for the second option: ")
    if len(queries) == 2:
        if answer.lower() == 'any':
            or_search(inverseindex, queries)
        elif answer.lower() == 'all':
            and_search(inverseindex, queries)
        else:
            print("Not a valid response")
            user_input_question()
    else:
        if answer.lower() == 'any':
            or_search(inverseindex, queries)
        elif answer.lower() == 'all':
            print("The amount of queries required for this search must be above 1. Returning to the beginning...")
            user_input_question()
        else:
            print("Not a valid response")
            user_input_question()


if __name__ == '__main__':
    user_input_question()

