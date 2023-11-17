# import csv

# def copy_pim_to_csv(pim_file, csv_file):
#     # lines in pim
#     with open(pim_file, 'r') as file:
#         lines = file.readlines()
#     # lines in csv
#     with open(csv_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         for line in lines:
#             writer.writerow([line.strip()])

# def insert_line(csv_file, line, index):
#     with open(csv_file, 'r') as file:
#         reader = csv.reader(file)
#         rows = list(reader)

#     rows.insert(index, line)

#     with open(csv_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(rows)

# def delete_line(csv_file, index):
#     with open(csv_file, 'r') as file:
#         reader = csv.reader(file)
#         rows = list(reader)

#     del rows[index]
    
#     with open(csv_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(rows)

# def copy_csv_to_pim(pim_file, csv_file):
#     with open(csv_file, 'r') as file:
#         reader = csv.reader(file)
#         lines = [','.join(row).replace('"','') for row in reader]

#     with open(pim_file, 'w') as file:
#         file.write('\n'.join(lines))

# def insert(new_line,insert_index):
#     pim_file_path = 'records.pim'
#     csv_file_path = 'output.csv'
#     copy_pim_to_csv(pim_file_path,csv_file_path)
#     insert_line(csv_file_path,new_line,insert_index)
#     copy_csv_to_pim(pim_file_path,csv_file_path)
#     return


# def delete(delete_index):
#     pim_file_path = 'records.pim'
#     csv_file_path = 'output.csv'
#     copy_pim_to_csv(pim_file_path,csv_file_path)
#     delete_line(csv_file_path, delete_index)
#     copy_csv_to_pim(pim_file_path,csv_file_path)
#     return



def replace(file_path,search_text, replace_text):
    with open(file_path,'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)

    with open('replace_test.pim','w') as file:
        file.write(data)

def insert(file_path, line_number, line_text):
    # Read the existing contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Insert the new line at the specified position
    lines.insert(line_number - 1, line_text + '\n')

    # Write the modified contents back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

def delete(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if line_number > 0 and line_number <= len(lines):
        del lines[line_number - 1]

    with open(file_path, 'w') as file:
        file.writelines(lines)
