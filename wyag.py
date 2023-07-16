import hashlib  #SHA-1 
import argparse  #CLI needs to parse CL-arguments
import collections #extra containers
import configparser  #read and write files
import os
import sys #access command-line arg
import re
import zlib  #for git compress

from math import ceil 


parser = argparse.ArgumentParser(description="homemade git")

#######HANDLING GIT SUB COMMANDS#########
subparser = parser.add_subparsers(title="Commands", dest="command")
subparser.required = True

def main(argv=sys.argv[1:]):
    args = parser.parse_args(argv)
    
    if args.command == "add"    :cmd_add(args)
    print("Hello")


