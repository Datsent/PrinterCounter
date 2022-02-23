from Utils import *
from DataFile import read_data, create_new_data

def main():
    Lines = read_data(USE_FILE_PATH)
    create_new_data(Lines)

if __name__ == "__main__":
    main()
