"""
Test related to orbfit-json
(the ones directly produced by M. Pan's wrapper, with the defining feature that all of the data are strings.)
"""

# Local imports
# -----------------------
from os.path import join, dirname, abspath, isfile
from os import remove

import sys
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
code_dir  = join(pack_dir, 'mpc_orb')
sys.path.append(code_dir)

import schema
import filepaths


# Tests
# -----------------------
def test_bootstrap_A():
    '''
    Test the "bootstrap" routine that takes us from zero-to-hero
    I.e. the bootstrap function starts from some defining orbfit jsons (str-format)
    and takes us all the way to having the three desired sets of json schema
    '''

    # Assert that the required defining input files exist
    assert len(filepath_dict['orbfit_defining_sample']) > 5 ,\
        f'Insufficient files: {filepath_dict["orbfit_defining_sample"]}'
    for f in filepath_dict['orbfit_defining_sample']:
        assert isfile( f ), f'file {f} does not exist'
    
    # Explicitly delete any of the schema files and/or "numerical conversion" files ...
    # that have previously been generated from the above defining samples
    for f in filepath_dict['mpcorb_defining_sample']:
        remove(f)
    for f in ['orbfit_general_schema','orbfit_conversion_schema', 'mpcorb_schema']:
        remove(filepath_dict[f])

    # Run the bootstap code to create ...
    # ...orbfit schema
    # ...converted files (str -to- num) to act as defining mpcorb files
    # ...mpcorb schema
    bootstrap.bootstrap()

    # Assert that the required files now exist
    for f in filepath_dict['mpcorb_defining_sample']:
        assert isfile(f) , f'{f} does not exist'
    for f in ['orbfit_general_schema','orbfit_conversion_schema', 'mpcorb_schema']:
        assert isfile(filepath_dict[f]), f'{filepath_dict[f]} does not exist'

