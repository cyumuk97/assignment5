#!/usr/bin/env python3
# test_config.py

"""
Test for module config.py
"""

from assignment5 import config

_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"

homo_sapiens = "Homo_sapiens"
bos_taurus = "Bos_taurus"
equus_caballus = "Equus_caballus"
mus_musculus = "Mus_musculus"
ovis_aries = "Ovis_aries"
rattus_norvegicus = "Rattus_norvegicus"
                        
# Dictionary                            
keywords = {
        "Homo sapiens": homo_sapiens,
        "Human": homo_sapiens,
        "Humans": homo_sapiens,
        "Bos taurus": bos_taurus,
        "Cow": bos_taurus,
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


def test_get_unigene_directory():
    """
    Tests get_unigene_directory function
    """
    test = config.get_unigene_directory()
    assert test == _UNIGENE_DIR


def test_get_unigene_extension():
    """
    Tests get_unigene_extension function
    """
    test = config.get_unigene_extension()
    assert test == _UNIGENE_FILE_ENDING


def test_get_host_keywords():
    """
    Tests get_host_keywords function
    """
    test = config.get_host_keywords()
    assert test == keywords
