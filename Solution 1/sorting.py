#!/usr/bin/python

import re
import os
import sys

# Key for sorting

def sort_key(s):
    return [float(text) if text.isdigit() else text.lower()
            for text in re.split(regdigits, s)]


# Open input file and write contents to new file.

def read_and_write(inputfile):
    try:
        with open(inputfile, 'r+') as i:
            with open('unsorted.txt', 'w+') as j:
                for line in i:
                    j.write(line)
    except OSError:
        print('File not found. Please try again.')


# Inserts whitespace if none exists

def insert_whitespace(sortfile):
    for line in first_sort:
        wspace = re.sub(r'([0-9]+)([a-zA-Z])', r'\1 \2', line)
        sortfile.write(wspace)


# Removes multiple whitespace

def remove_whitespace(sortfile):
    for line in first_sort:
        no_wspace = re.sub(' +', ' ', line)
        sortfile.write(no_wspace)


def main():

    # User inputs path of file to be sorted
    filename = input("Enter path of the file to be sorted: ")
        
    # Open input file and write contents to new file.
    read_and_write(filename)


if __name__ == "__main__":
    
    # Captures numbers for sorting key
    regdigits = re.compile('([0-9]+)')   
    
    main()

    # Inserts whitespace if none exists
    with open('unsorted.txt') as first_sort:
        with open('sorted.txt', 'w+') as final_sort:
            insert_whitespace(final_sort)

    # Removes multiple whitespace
    with open('sorted.txt') as first_sort:
        with open('unsorted.txt', 'w+') as final_sort:
            remove_whitespace(final_sort)

    # Sort new file using sorting key
    with open('unsorted.txt') as first_sort:
        with open('sorted.txt', 'w+') as final_sort:
            lines = first_sort.readlines()
            lines.sort(key=sort_key)
            newlines = final_sort.writelines(lines)

          
# Cleanup/ success confirmation

os.remove('unsorted.txt')
print('sorted.txt complete.')
