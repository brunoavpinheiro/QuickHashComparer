__author__ = "Bruno Alberto da Veiga Pinheiro"
__email__ = "contato@brunoavpinheiro.com.br"

import argparse
import csv

def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    return added, removed

def main():
    parser = argparse.ArgumentParser(description='QuickHash Comparer')

    parser.add_argument('leftCsv', help='Left CSV file')
    parser.add_argument('rightCsv', help='Right CSV file')

    args = parser.parse_args()
    print("Left CSV File: " + args.leftCsv + "\n")
    print("Right CSV File: " + args.rightCsv + "\n")
    
    leftDict = {}
    rightDict = {}

    with open(args.leftCsv, 'rb') as leftFile:
        lines = csv.reader(leftFile, delimiter=',')
        for line in lines:
            leftDict[line[3]] = line[2] + line[1]

    with open(args.rightCsv, 'rb') as rightFile:
        lines = csv.reader(rightFile, delimiter=',')
        for line in lines:
            rightDict[line[3]] = line[2] + line[1]

    added, removed = dict_compare(leftDict,rightDict)

    print("Addded on the left:\n")
    for key in added:
        print(leftDict[key])

    print("\nRemoved on the left:\n")
    for key in removed:
        print(rightDict[key])

if __name__ == "__main__":
    main()