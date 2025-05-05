"""
This script identifies the types
of files in a given directory and
moves them into broadly-named sub
directories, e.g., it puts tar and
zip files into an "Archives" sub
directory. The script uses a switch
statement, which requires python3.10
at minimum.
"""
from argparse import ArgumentParser
from os import listdir, makedirs, path
from shutil import move
from magic import from_file

def organize_folder(folder_path:str)->None:
    for filename in listdir(folder_path):
        file_path = path.join(folder_path, filename)
        if any([not path.isfile(file_path), path.islink(file_path)]):
            continue
        file_header = from_file(file_path)
        match file_header:
            case ft if any(["certificate" in file_header, "key" in file_header]):
                folder = "Certs"
            case ft if "compressed" in file_header:
                folder = "Archives"
            case ft if all(["data" in file_header, "image" not in file_header]):
                folder = "Data"
            case ft if "empty" in file_header:
                folder = "Empty" if path.getsize(file_path) == 0 else "Error"
            case ft if any(["HTML" in file_header, "XML" in file_header]):
                folder = "Web_Pages"
            case ft if "image" in file_header:
                folder = "Images"
            case ft if "Microsoft" in file_header:
                folder = "Microsoft"
            case ft if "pcap" in file_header:
                folder = "PCAPs"
            case ft if "script" in file_header:
                folder = "Scripts"
            case ft if all([
                any(["text" in file_header, "document" in file_header]),
                any(["JSON" not in file_header, "script" not in file_header, 
                     "HTML" not in file_header, "XML" not in file_header, "PDF" in file_header])
            ]):
                folder = "Docs"
            case _:
                folder = "Misc"
        target_dir = path.join(path.dirname(file_path), folder)
        makedirs(target_dir, exist_ok=True)
        move(file_path, path.join(target_dir, path.basename(file_path)))
        print(f'Moved {filename} to {folder}')

def main():
    parser = ArgumentParser(description="Organize files in a given folder by type.")
    parser.add_argument("-fp", "--folder_path", type=str, help="Path to the folder you want to organize.")
    args = parser.parse_args()
    organize_folder(args.folder_path)

if __name__ == '__main__':
    main()
