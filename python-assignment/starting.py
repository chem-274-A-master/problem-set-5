"""
Starting code
"""

import pprint
import json

from gemmi import cif

# don't forget to unzip your data folder before 
# running this.

def read_cif(filepath: str):
    """
    Read a CIF file using gemmi. 
    """
    # read CIF with gemmi
    doc = cif.read_file(filepath)
    
    # use as_json in gemmi to convert to json
    # convert from json to Python dict using
    # json.loads
    cif_dict = json.loads(doc.as_json())
    
    # You now have a dictionary to work with!
    # pprint (from pprint) is "pretty print"
    # will make long dict more readable.
    pprint.pprint(cif_dict)

    # Consider putting a breakpoint here
    # and examining cif_dict live! 
    breakpoint()

if __name__ == "__main__":
    read_cif("data/ALA.cif")