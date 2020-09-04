import re 
import sys
import time 
import osxphotos
import argparse
from datetime import datetime


def create_arguments():
    parser = argparse.ArgumentParser(description='Returns 0 if image file exists in Photos Library. Else returns 1.')
    parser.add_argument('--image_name', action='store', dest='image_name',required=True, help='Name of image file')
    return parser.parse_args()

def main():
    args = create_arguments()
    # image_name = "90.jpeg"
    photosdb = osxphotos.PhotosDB()    
    # photosdb = osxphotos.PhotosDB(osxphotos.utils.get_last_library_path())    
    results =  [ photo for photo in photosdb.photos( movies=False, images=True ) if photo.original_filename == args.image_name ]
    if results:
        print("File exists in library")
        return 0
    else:
        print("File does not exist in library")
        return 1
    # print(results)
    return    



if __name__ == "__main__":
    start_time = datetime.now()
    results = main()  
    print(f"Script completed in {(datetime.now() - start_time).seconds} seconds.")
    sys.exit(results)