#!/usr/bin/env python3
# gene_information_query.py

"""
Takes common and scientific names and gene names as input and checks
if the gene exists in host directory
"""
import argparse
import re
import sys
from assignment5 import config
from assignment5 import my_io


def main():
    """
    Main function
    """
    # Get command line arguments
    args = get_cli_args()
    host = args.HOST
    gene = args.GENE

    if host is None:
        new = "/".join((config.get_unigene_directory(), "Homo_sapiens",
                        "TGM1" + "." + config.get_unigene_extension()))
        data = get_gene_data(new)
        print_output("Human", "TGM1", data)

    else:
        name = modify_host_name(host.capitalize())

        filename = "/".join((config.get_unigene_directory(), name, gene + "." +
                             config.get_unigene_extension()))

        if my_io.is_valid_gene_file_name(filename):
            print(f"\nFound Gene {gene} for {name}")

        else:
            print("Not found")
            print(f"Gene {gene} does not exist for {host}. exiting now...",
                  file=sys.stderr)
            sys.exit()

        data1 = get_gene_data(filename)

        print_output(name, gene, data1)


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
    print("or if you are trying to use the scientific name please put\
          the name in double quotes:")
    print("Scientific name")
    print("Here is a (non-case sensitive) list of available Hosts by\
          scientific name")

    num = 1
    for key in host:
        key2 = None
        if host[key] != key2:
            print(str(num) + "." + host[key])
        key2 = host[key]
        num += 1

    print("Here is a (non-case sensitive) list of available Hosts by\
          common name")

    count = 1
    for key in host:
        print(str(count) + "." + key)
        count += 1


def get_gene_data(filename):
    """
    Returns a sorted list of the tissues in existing filename
    """
    new = my_io.get_fh(filename, "r")

    for line in new:
        line = line.rstrip()
        match = re.search("^EXPRESS", line)
        if match:
            tissue_string = line.split('|')
    print("tissue 1 ")
    print(tissue_string)
    tissue_string[0] = tissue_string[0].replace("EXPRESS", '').lstrip()

    tissue_string = sorted(tissue_string)
    print(tissue_string)
    return tissue_string


def print_output(host, gene, data):
    """
    Prints the tissue expression data for the gene
    """
    print("In " + host + ", There are " + str(len(data)) +
          " tissues that " + gene + " is expressed in:")
    num = 1
    for name in data:
        print(str(num) + "." + name)
        num += 1


def get_cli_args():
    """
    Gets command line options using argparse
    Returns instances of argparse arguments
    """
    parser = argparse.ArgumentParser(
        description='Give the Host and Gene name')

    parser.add_argument('-host', '-HOST',
                        dest='HOST',
                        type=str,
                        help='Name of Host',
                        required=False)

    parser.add_argument('-gene', '-GENE',
                        dest='GENE',
                        type=str,
                        help='Name of Gene',
                        required=False)

    return parser.parse_args()


if __name__ == '__main__':
    main()
