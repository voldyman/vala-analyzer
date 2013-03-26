#!/usr/bin/python

import sys

def main():
    lines = open(sys.argv[1], "r").readlines()

    for i in range(len(lines)):
        # Check for single braces in a line
        if lines[i].strip() == "{":
            print "Suspicious line: %d" % (i + 1)

        for u in range(len(lines[i])):
            # Check for parentheses not preceded by a space
            if lines[i][u] == "(" and lines[i][u - 1] != "(" and lines[i][u - 1] != " " and lines[i][u - 1] != "_":
                print "Suspicious line: %d" % (i + 1)

            # Check for equal signs that aren't spaced
            if lines[i][u] == "=" and lines[i][u - 1] != " " and lines[i][u + 1] != " " and lines[i][u + 1] != "\"":
                print "Let's hope the non-spaced equal signs on line %d are inside parentheses." % (i + 1)

        # Check for tabs
        if "\t" in lines[i]:
            print "Found a tab on line: %d" % (i + 1)

if __name__ == "__main__":
    main()
