"""
This script organizes a directory.
It identifies the types of files
therein and moves them into
broadly-named sub directories, e.g.,
it puts tar and zip files into an
"Archives" sub directory. The script
uses a switch statement, which requires
python3.10 at minimum.
"""


from argparse import ArgumentParser
from os import listdir, makedirs, path
from shutil import move
from magic import from_file


def organize_folder(folder_path:str)->None:
    """Organizes folder contents into
    generically named sub folders.
    The function first identifies
    the file type by reading the file
    header, then creates an appropriately
    named sub folder, and moves
    the file into the new sub folder.

    :param `folder_path` (str):
        The directory path.
    :returns None:
    """

    # For every file in the folder,
    for filename in listdir(folder_path):

        # get the filepath,
        file_path = path.join(folder_path, filename)

        if any( # skip sub folders and symlinks.
            [
                not path.isfile(file_path),
                path.islink(file_path)
            ]
        ):
            continue

        # Get the file's header.
        file_header = from_file(file_path)

        # Create a folder name based on the
        # appearance of a "key word" in header.
        match file_header:

            # Certificates
            case ft if any(
                [
                    "certificate" in file_header,
                    "key" in file_header
                ]
            ):
                folder = "Certs"

            # Archives
            case ft if "compressed" in file_header:
                folder = "Archives"

            # Data
            case ft if all(
                [
                    "data" in file_header,
                    "image" not in file_header
                ]
            ):
                folder = "Data"

            # Empty/error
            case ft if "empty" in file_header:
                if all( # Save to "Empty".
                    [
                        path.isfile(file_path),
                        path.getsize(file_path) == 0
                    ]
                ):
                    folder = "Empty"

                else: # Save to "Error".
                    folder = "Error"

            # Web
            case ft if any(
                [
                    "HTML" in file_header,
                    "XML" in file_header
                ]
            ):
                folder = "Web_Pages"

            # Images
            case ft if "image" in file_header:
                folder = "Images"

            # Microsoft
            case ft if "Microsoft" in file_header:
                folder = "Microsoft"

            # PCAPs
            case ft if "pcap" in file_header:
                folder = "PCAPs"

            # Scripts
            case ft if "script" in file_header:
                folder = "Scripts"

            # Documents
            case ft if all( # If the file is a txt, pdf, etc.
                [
                    any(
                        [
                            "text" in file_header,
                            "document" in file_header
                        ]
                    ),
                    any(
                        [
                            "JSON" not in file_header,
                            "script" not in file_header,
                            "HTML" not in file_header,
                            "XML" not in file_header,
                            "PDF" in file_header
                        ]
                    )
                ]
            ):
                folder = "Docs"

            # Default
            case _:
                folder = "Misc"

        # Build the path to the sub folder
        target_dir = path.join(path.dirname(file_path), folder)
        makedirs(target_dir, exist_ok=True)

        # Move the file to the sub folder and notify user.
        move(file_path, path.join(target_dir, path.basename(file_path)))
        print(f'Moved {filename} to {folder}')


def main():
    parser = ArgumentParser(
        description="Organize files in a given folder by type."
    )

    parser.add_argument(
        "-fp",
        "--folder_path",
        type=str,
        help="Path to the folder you want to organize."
    )

    args = parser.parse_args()
    folder_path = args.folder_path
    organize_folder(folder_path)


if __name__ == '__main__':
    main()
