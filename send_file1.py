import pysftp
import glob
import os

username = 'ftpusername'
passwd = 'ftppassword'
cnopts = pysftp.CnOpts(knownhosts=r'\\path\to\know_hosts\file')


def move_files(filename):
    short_filename = filename.split('\\')
    short_filename = short_filename[8]
    with pysftp.Connection('servername', username=username, password=passwd, cnopts=cnopts) as sftp:
        sftp.put(filename, preserve_mtime=True)
        sftp.close()
    with pysftp.Connection('servername', username=username, password=passwd, cnopts=cnopts) as sftp:
        sftp.put(filename, preserve_mtime=True)
        sftp.close()
    notify = f"{short_filename} sent to SUP and PRD"
    return notify


def newest_file():
    list_of_files = glob.iglob(r'\\path\to\filefolder\with\textfiles\*.txt')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def appt_import_txt(import_file):
    short_import_file = import_file.split('\\')
    short_import_file = short_import_file[8]
    with pysftp.Connection('servername', username=username, password=passwd,
                           cnopts=cnopts) as sftp:
        sftp.getfo(f"/home/{username}/{short_import_file}", sftp.open(f'/home/{username}/apptimport.txt',
                                                                      mode='w'))
        sftp.close()
    with pysftp.Connection('servername', username=username, password=passwd,
                           cnopts=cnopts) as sftp:
        sftp.getfo(f"/home/{username}/{short_import_file}", sftp.open(f'/home/{username}/apptimport.txt',
                                                                      mode='w'))
        sftp.close()

