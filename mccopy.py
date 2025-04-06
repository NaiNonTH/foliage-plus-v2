import os
import shutil

from argparse import ArgumentParser

if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-d", "--destination")
    
    dest_args = arg_parser.parse_args()
    
    if dest_args.destination is None:
        try:
            with open("dest_dir.txt", "r") as ddir:
                DEST_DIR = ddir.read()
        except FileNotFoundError:
            print("Cannot find \"dest_dir.txt\" file")
            exit(1)
    else:
        DEST_DIR = dest_args.destination

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    shutil.rmtree(os.path.join(DEST_DIR, "Foliage+"))
    shutil.copytree(os.path.join(BASE_DIR, "pack"), os.path.join(DEST_DIR, "Foliage+"))
    
    print("copied!")