# Local imports
# -----------------------
from os.path import join, dirname, abspath, isfile

import sys
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
code_dir  = join(pack_dir, 'mpc_orb')
sys.path.append(code_dir)

import schema
import filepaths
import interpret

import convert

# Tests
# -----------------------
def test_convert_A():
    """
    Test the conversion from orbfit-json (lots of strings) to mpc_orb format
    NB. This is ONLY TESTING THE INTERNAL ROUNTE *std_format_els* AT THIS POINT
    """

    # interpret the input (allow dict or filepath)
    orbfit_dict, input_filepath = interpret.interpret( filepaths.schema_name_dict['orbfit_defining_sample']  )

    # check the input is valid
    schema.validate_orbfit(orbfit_dict)

    # do the conversion (this is the heart of the routine)
    standard_format_dict = convert.std_format_els(orbfit_dict)

    # Just assert that we have a dict for now
    assert isinstance(standard_format_dict , dict )
    
    # Now use the above to create/save a defining "example" json file for mpcorb
    # *** NOT CLEAR WE WANT TO BE DOING THIS HERE ...
    # *** SORT OF HIDING-AWAY AN IMPORTANT PROCESS STEP ... 
    schema.save_json(filepaths.schema_name_dict['mpcorb_defining_sample'], standard_format_dict)

