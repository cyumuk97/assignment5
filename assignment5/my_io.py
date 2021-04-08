#!/usr/bin/env python3
# my_io.py

"""

"""

import os
from assignment5 import config

def get_fh(filename=None, mode=None):
    """
    Opens an input file and passes back a file object
    """
    try:
        new = open(filename, mode)
        return new
    except IOError as err:
        config.get_error_string_4_IOError(filename, mode)
        raise err
    except ValueError as err:
        config.get_error_string_4_ValueError()
        raise err
    except TypeError as err:
        config.get_error_string_4_TypeError()
        raise err

def is_valid_gene_file_name(filename):
    """
    Checks if filename exists
    """
    return os.path.exists(filename)
