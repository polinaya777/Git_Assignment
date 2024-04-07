import argparse
import sys

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="operation")

parser_add = subparsers.add_parser('add')
parser_add.add_argument('x', type=int)
parser_add.add_argument('y', type=int)

parser_subtract = subparsers.add_parser('subtract')
parser_subtract.add_argument('x', type=int)
parser_subtract.add_argument('y', type=int)

parser_mul = subparsers.add_parser('multiply')
parser_mul.add_argument('x', type=int)
parser_mul.add_argument('y', type=int)

args = parser.parse_args()

if args.operation == 'add':
    print(args.x + args.y)
elif args.operation == 'subtract':
    print(args.x - args.y)
elif args.operation == 'multiply':
    print(args.x * args.y)
else:
    print("Error: Invalid operation. Please use 'add', 'subtract' or 'multiply'.")
    sys.exit(1)