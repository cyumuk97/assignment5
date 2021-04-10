#!/usr/bin/env python3
# gene_information_query.py

"""
Takes common and scientific names and gene names as input and checks
if the gene exists in host directory
"""

from assignment5 import config
from assignment5 import my_io
import argparse
import re
import sys

def main():
    """
    Main function
    """
    args = get_cli_args()
    host = args.HOST
    gene = args.GENE

    name = modify_host_name(host)


    filename = "/".join((config.get_unigene_directory(), host, gene + "." +
        config.get_unigene_extension()))

    if my_io.is_valid_gene_file_name(filename):
        print(f"\nFound Gene {gene} for {host}")

    else:
        print("Not found")
        print(f"Gene {gene} does not exist for {host}. exiting now...", file=sys.stderr)
        sys.exit()

    #data = get_gene_data(filename)
    
    if host == "" and gene == "":
        print_output(host, gene, data)

def modify_host_name(host):
    """
    Takes the host name and returns the scientific name
    """
    names = config.get_host_keywords()

    if host not in names:
        _print_host_directories()
        sys.exit()

    return names[host]

def _print_host_directories():
    """
    Prints out the existing host directories
    """
    host = config.get_host_keywords()

    print("Either the Host Name you are searching for is not in the database")
    print("or if you are trying to use the scientific name please put the name in double quotes:")
    print("Scientific name")
    print("Here is a (non-case sensitive) list of available Hosts by scientific name")

    num = 1
    for key in host:
        print(str(num) + "." + host[key])
        num += 1

    print("Here is a (non-case sensitive) list of available Hosts by common name")

    count = 1
    for key in host:
        print(str(count) + "." + key)
        count += 1

def get_gene_data(filename):
    """
    Returns a sorted list of the tissues in existing filename
    """
    my_io.is_valid_gene_file_name(filename)
    new = my_io.get_fh(filename)

    for line in new:
        match = re.search("EXPRESS", line)
        if match:
            tissue_string = match.group(1)

    return tissue_string


def print_output(host, gene, data):
    """
    Prints the tissue expression data for the gene
    """
    print("Found Gene " + gene + "for " + host)
    print("In " + host + ", There are " + str(len(data)) + " tissues that " + gene + " is expressed in:")
    print(data)

def get_cli_args():
    """
    Gets command line options using argparse
    Returns instances of argparse arguments
    """
    parser = argparse.ArgumentParser(
            description='Give the Host and Gene name')

    parser.add_argument('-host', 'HOST',
                       dest='HOST',
                       type=str,
                       help='Name of Host',
                       required=True)
            
    parser.add_argument('-gene', 'GENE',
                       dest='GENE',
                       type=str,
                       help='Name of Gene',
                       required=True)

    return parser.parse_args()

if __name__ == '__main__':
    main()
