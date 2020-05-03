import os
import sys
import pprint
import cv2


'''
Takes in a directory as an argument.
Checks all the image files in the directory for any duplicates and reports it at the end.
'''


is_verbose = False


def search_for_duplicates(path):
    bmh = cv2.img_hash.BlockMeanHash_create()

    image_hashes = {}
    dupes = {}

    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' or '.png' or '.gif' in file:
                filename = os.path.join(r, file)
                img = cv2.imread(filename)
                img_hash = bmh.compute(img)

                is_dupe = False
                for f, h in image_hashes.items():
                    if (h == img_hash).all():
                        dupes[filename.split('\\')[-1]] = f.split('\\')[-1]
                        if is_verbose:
                            print(f"{filename} is a duplicate of {f}")
                            print(img_hash)
                        is_dupe = True
                        break
                
                if not is_dupe:
                    image_hashes[filename] = img_hash

                    if is_verbose:
                        print(f"Saving {filename} with hash: {img_hash}")

    if is_verbose:
        print(image_hashes)
    
    pprint.pprint(dupes)




if len(sys.argv) == 2:
    search_for_duplicates(sys.argv[1])
elif len(sys.argv) == 3:
    if sys.argv[1] == '-v':
        is_verbose = True
    search_for_duplicates(sys.argv[2])
else:
    print("Missing argument: <images_directory>")