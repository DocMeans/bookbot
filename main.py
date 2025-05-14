from stats import get_num_words, get_book_text, sort_letters_and_count, report
import sys


def main():
    # Use sys.argv to enter the query from the command line
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Set file path instead of hard coding it and pass it 
    # to all function that require it
    file_path = sys.argv[1]
    sorted_counts = sort_letters_and_count(file_path)
    report(sorted_counts, file_path)

main()