#!/usr/bin/env python3
# config.py

"""
This module is used for configuration
"""
_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"


def get_unigene_directory():
    """
    Returns unigene directory
    """
    return _UNIGENE_DIR


def get_unigene_extension():
    """
    Returns unigene extension
    """
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    """
    Returns a dictionary of hosts
    """
    homo_sapiens = "Homo_sapiens"
    bos_taurus = "Bos_taurus"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

    # Dictionary
    host_keywords = {
        "Homo sapiens": homo_sapiens,
        "Human": homo_sapiens,
        "Humans": homo_sapiens,
        "Bos taurus": bos_taurus,
        "Cow":  bos_taurus,
        "Cows": bos_taurus,
        "Equus caballus": equus_caballus,
        "Horse": equus_caballus,
        "Horses": equus_caballus,
        "Mus musculus": mus_musculus,
        "Mouse": mus_musculus,
        "Mice": mus_musculus,
        "Ovis aries": ovis_aries,
        "Sheep": ovis_aries,
        "Sheeps": ovis_aries,
        "Rattus norvegicus": rattus_norvegicus,
        "Rat": rattus_norvegicus,
        "Rats": rattus_norvegicus
        }

    return host_keywords


def get_error_string_4_IOError(file=None, mode=None):
    """
    Prints the invalid argument type message and exits the program
    """
    print(f"Could not open the file: {file} for mode '{mode}'")


def get_error_string_4_ValueError():
    """
    Prints the invalid argument type message and exits the program
    """
    print("Invalid argument Value for opening a file for reading/writing")


def get_error_string_4_TypeError():
    """
    Prints the invalid argument type message and exits the program
    """
    print("Invalid argument Type passed in:")
