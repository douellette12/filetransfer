from send_file1 import *


if __name__ == '__main__':
    file = newest_file()
    move_files(file)
    appt_import_txt(file)
