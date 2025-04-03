import os
import shutil

from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument("-d", "--destination")

dest_args = arg_parser.parse_args()

if dest_args.destination is None:
    print("Please provide destination path using -d or --destination.")
    quit(1)

DEST_DIR = dest_args.destination
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

shutil.rmtree(os.path.join(DEST_DIR, "Foliage+"))
shutil.copytree(os.path.join(BASE_DIR, "pack"), os.path.join(DEST_DIR, "Foliage+"))

print("copied!")