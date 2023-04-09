import os
import fileinput

def replace_string_in_files(path, search_string, replace_string):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            with fileinput.FileInput(file_path, inplace=True) as f:
                for line in f:
                    print(line.replace(search_string, replace_string), end='')

# Replace all instances of "canary" with "myword"
replace_string_in_files('/path/to/canarytokens', 'canary', 'myword')





#This program is a Python script that defines a function called replace_string_in_files. This function receives three arguments: path, search_string, and replace_string. The purpose of the function is to search for all files in the given directory (path) and in all its subdirectories and replace all occurrences of search_string with replace_string.

#The script uses the Python Standard Library modules os and fileinput. The os module provides a portable way of using operating system dependent functionality like reading or writing files while fileinput is a modular iterator based approach to reading input from files, one line at a time.

#To achieve the task, the script first walks through the directory tree rooted at path using the os.walk method, which returns a tuple for each directory it traverses: a string representing the directory path, a list of its subdirectories, and a list of its files. For each file, it opens the file with fileinput.FileInput and uses the replace method on each line, which returns a new string with all occurrences of search_string replaced with replace_string. The inplace parameter is set to True, which causes fileinput to overwrite the original file with the new content of the same filename.

#Finally, the function is called with the argument values to replace the string canary with myword in all files located in the directory /path/to/canarytokens and its subdirectories.
