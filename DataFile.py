import os, sys
from Utils import *
from Counter import get_count

def read_data (path):
    file_printers = open(os.path.join(sys.path[0], path), "r")
    Lines = file_printers.readlines()
    file_printers.close()
    return Lines

def create_new_data(Lines):
    new_list = ['#,Model,Serial,IP Adress,Supply Date,Begin Count,Last Count,Count,Total Pages\n']
    for line in Lines[1:]:
        line_list = line.split(',')
        print(f'Calculating Model: {line_list[1]}...')
        line_list[6] = line_list[7]
        try:
            line_list[7] = get_count(line_list[3], line_list[1] )
            line_list[8] = str(int(line_list[7]) - int(line_list[6])) + '\n'
            new_list.append(','.join(line_list))
        except BaseException:
            print(f"No connection with {line_list[3]}")
            line_list[7] = '0'
            line_list[8] = 'N/A\n'
            new_list.append(','.join(line_list))
        print(f'Finished Model: {line_list[1]}...')
    file = open(os.path.join(sys.path[0], ARCHIVE_FILE_PATH, 'w'))
    file.write(''.join(new_list))
    file.close()
    file = open(os.path.join(sys.path[0], USE_FILE_PATH), 'w')
    file.write(''.join(new_list))
    file.close()
    print('FINISHED')

