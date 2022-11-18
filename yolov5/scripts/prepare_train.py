import os
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description ="Prepare the list of names of all train images for yolo.")

    parser.add_argument("--images_dir", default="", help="Specify the path to the train images dataset folder.")
    parser.add_argument("--out_name", default="train.txt", help="Specify the file name to save the list.")

    args = parser.parse_args()
    return args


def create_list(images_dir, out_name):
    img_files = list(sorted(os.listdir(images_dir)))

    with open(out_name, "w") as f:
        for img in img_files:
            full_image_path = os.path.join(images_dir, img)
            f.write(str(full_image_path) + "\n")
            #print(img)


if __name__=='__main__':
    args = parse_args()

    create_list(args.images_dir, args.out_name)


