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

def delete_line(csv_file, line, index):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    del rows[index]
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def copy_csv_to_pim(pim_file, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        lines = [','.join(row).replace('"','') for row in reader]

    with open(pim_file, 'w') as file:
        file.write('\n'.join(lines))
