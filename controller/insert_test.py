import csv

def copy_pim_to_csv(pim_file, csv_file):
    # lines in pim
    with open(pim_file, 'r') as file:
        lines = file.readlines()
    # lines in csv
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for line in lines:
            writer.writerow([line.strip()])

def insert_line(csv_file, line, index):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    rows.insert(index, line)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def copy_csv_to_pim(pim_file, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        lines = [','.join(row).replace('"','') for row in reader]

    with open(pim_file, 'w') as file:
        file.write('\n'.join(lines))

def insert(new_line,insert_index):
    pim_file_path = 'records.pim'
    csv_file_path = 'output.csv'
    copy_pim_to_csv(pim_file_path,csv_file_path)
    insert_line(csv_file_path,new_line,insert_index)
    copy_csv_to_pim(pim_file_path,csv_file_path)
    return



# Test example
pim_file_path = 'records.pim'
csv_file_path = 'output.csv'
new_line = ['Assignment 3', '2023/11/29 23:59']
insert_index = 11

copy_pim_to_csv(pim_file_path, csv_file_path)
insert_line(csv_file_path, new_line, insert_index)
copy_csv_to_pim(pim_file_path, csv_file_path)