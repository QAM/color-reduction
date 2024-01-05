import os

from util import read_image, write_file
from algorithm import FloydSteinberg, Stucki, Burkes, NearestColor, OrderedDither
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a", "--algorithm", type=str,
        choices=["nearest_color", "ordered_dither", "floyd", 'burkes', 'stucki'], help="Algorithm for color reduction"
    )
    parser.add_argument(
        "-i", "--img_path", type=str,
        help="Input Image Path"
    )
    parsed_args = parser.parse_args()
    return parsed_args


def get_algorithm(algorithm: str):
    match algorithm:
        case "nearest_color":
            return NearestColor()
        case "ordered_dither":
            return OrderedDither()
        case "floyd":
            return FloydSteinberg()
        case "burkes":
            return Burkes()
        case "stucky":
            return Stucki()
        case _:
            raise ValueError(f"the algorithm {algorithm} is not supported")


if __name__ == '__main__':
    args = parse_arguments()

    img = read_image(args.img_path)

    algo = get_algorithm(args.algorithm)

    color_reduced_img = algo.run(img)

    write_file(img, "./out", args.algorithm + "_" + os.path.basename(args.img_path))
