'''
Copy files by type (PDF) Recursively from folder to destintation
'''
import os
import glob
import shutil

type = '.pdf'
glob_path = 'C:/mypath/**/*' + type
target_directory = r'C:\tmp'
#os.chdir(path_images)

def get_files(path):
    """Returns list of files to copy from directory, recursively"""
    files = glob.glob(path, recursive= True)
    file_list = []
    print(files)
    for file in files:
        print(file)
        file = file.replace('\\', "/")
        file_list.append(file)
    return file_list 

def copy_files(files):
    for file in files:
        try:
            shutil.copy2(file, target_directory)
        except:
            print("Error occurred while copying file.")
    print("Done")

def main():
    files = get_files(glob_path)
    print(files)
    copy_files(files)

if __name__ == "__main__":
    main()

