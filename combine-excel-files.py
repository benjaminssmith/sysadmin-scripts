# Combine multiple excel files into single
import os
import pandas as pd
import glob

path = r'path.../here'

def get_filenames(path):
    """Returns list of filenames in directory"""
    file_names = glob.glob("*")
    return file_names

def main():
    os.chdir(path)
    files = get_filenames(path)
    frames = []
    for file in files:
        df = pd.read_excel(file)
        frames.append(df)
    combined_df = pd.concat(frames)
    combined_df.to_csv('combined_df.csv', index=False)

if __name__ == "__main__":
    main()
