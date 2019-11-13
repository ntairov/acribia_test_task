"""Remove ".%EXT%" string from a file, make distinct set and create new cleaned text file"""
import re

with open('raw_data.txt', 'r') as raw_f, open('new_cleaned_data.txt', 'w') as clean_f:
    clean_f.writelines(line for line in raw_f if not line.endswith('.%EXT%\n'))
    # pattern = ".%EXT%"
    # cleaned_data = re.sub(pattern, '', line)
    # clean_f.write(str(cleaned_data))
