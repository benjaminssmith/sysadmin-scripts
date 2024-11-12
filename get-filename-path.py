import os

path = r'C:\myfolder'
documents = r'C:\myfiles'
os.chdir(path)

def get_file_list(path):
    """Returns list of filename,filepath"""
    file_list = []
    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            print(file,dirpath)
            file_list.append(file + "," + str(dirpath))
    return file_list

def list_to_file(files,file,directory):
    """Saves list to a csv file"""
    os.chdir(directory)
    with open(file, 'w') as f:
        for item in files:
            f.write(str(item) + '\n')

def main():
    print("**GETTING FILE NAMES***")
    files = get_file_list(path)
    print("***SAVING FILE***")
    list_to_file(files,'images-folder.csv',documents)
    
if __name__ == "__main__":  
    main()
