# Reads the text from the given file path and returns its contents
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

# Takes a string of text, splits it into words, and returns the total word count
def get_num_words(text):
    words = text.split()  # Split the text into a list of words
    return len(words)  # Return the number of words

def sort_by_count(item):
    return item["num"]

def sort_letters_and_count(file_path):
    letter = get_book_text(file_path) # Get the text from the file
    letter_dict = {} # Dictionary to store letter counts

    for l in letter:
        l = l.lower() # Convert the character to lowercase
        if l.isalpha():  # Check if the character is alphabetic
            # Update the count for the letter in the dictionary
            if l in letter_dict:
                letter_dict[l] += 1
            else:
                letter_dict[l] = 1

    # Sort the dictionary by letter in alphabetical order
    new_dict = dict(sorted(letter_dict.items()))

    # Convert the letter dictionary into a list of dictionaries for sorting by count
    sorted_counts = [{"char": k, "num": v} for k, v in letter_dict.items()]

    # Sort the list by the 'num' value in descending order
    sorted_counts.sort(key=sort_by_count, reverse=True)

    return sorted_counts
    
# Generates and prints the report showing word count and character count per letter
def report(sorted_counts, file_path):
    # Get the total word count
    letter = get_book_text(file_path)
    total_words = get_num_words(letter)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...") # shows the file_path output
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words") # shows total words
    print("--------- Character Count -------")
    
    # Print each letter and its count
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============") # End of report

    