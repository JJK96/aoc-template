import importlib
import argparse
import pathlib
import sys

parser = argparse.ArgumentParser()
parser.add_argument("num")
parser.add_argument("--test", action="store_true")
args = parser.parse_args()

dir = pathlib.Path(__file__).parent
srcdir = dir / "src"

day = importlib.import_module(f"src.{args.num}")

filename = srcdir / args.num / 'input'
part1_filename = filename
part2_filename = filename
if args.test:
    part1_filename = srcdir / args.num / 'input1.example'
    part2_filename = srcdir / args.num / 'input2.example'

print("part 1: ")
print(day.part1(part1_filename))

print("part 2: ")
print(day.part2(part2_filename))
