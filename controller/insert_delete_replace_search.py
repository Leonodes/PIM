from datetime import datetime
from checkFormat import checkDateFormat
import os

file_path = current_file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(os.path.dirname(file_path))
print(dir_path)
record_path = os.path.join(dir_path,'records.pim')
print(record_path)

def replace(search_text, replace_text):
    with open(record_path,'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)

    with open(record_path,'w') as file:
        file.write(data)

def insert(line_text, line_index):
    # Read the existing contents of the file
    with open(record_path, 'r') as file:
        lines = file.readlines()

    # Insert the new line at the specified position
    lines.insert(line_index - 1, line_text + '\n')

    # Write the modified contents back to the file
    with open(record_path, 'w') as file:
        file.writelines(lines)

def delete(line_number):
    with open(record_path, 'r') as file:
        lines = file.readlines()

    if line_number > 0 and line_number <= len(lines):
        del lines[line_number - 1]

    with open(record_path, 'w') as file:
        file.writelines(lines)

def matches_text(text_criteria):
    found_lines = []
    with open(record_path, "r") as file:
        for line in file:
            if text_criteria in line:
                found_lines.append(line.strip())
    return found_lines

def matches_time(time_criteria,condition):
    found_lines = []
    with open(record_path, "r") as file:
        for line in file:
            parts = line.split(",")
            for part in parts:
                if checkDateFormat(part.strip()):
                    time = datetime.strptime(time_criteria.strip(),"%Y/%m/%d %H:%M")
                    value = datetime.strptime(part.strip(),"%Y/%m/%d %H:%M")
                    condition = condition
                    if condition == "<" and value < time:
                        found_lines.append(line.strip())
                    elif condition == ">" and value > time:
                        found_lines.append(line.strip())
                    elif condition == "=" and value == time:
                        found_lines.append(line.strip())
                    else:
                        pass
        return found_lines


def not_included_file(strings_to_remove):
    found_lines = []
    with open(record_path, 'r') as file:
        for line in file:
            if not any(string in line for string in strings_to_remove):
                found_lines.append(line.rstrip())
        return found_lines
                





