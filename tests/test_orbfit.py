"""
Test related to orbfit-json
(the ones directly produced by M. Pan's wrapper, with the defining feature that all of the data are strings.)
"""

# Local imports
# -----------------------
from os.path import join, dirname, abspath, isfile

import sys
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
code_dir  = join(pack_dir, 'mpc_orb')
sys.path.append(code_dir)

import schema
import filepaths


# Tests
# -----------------------
def test_create_orbfit_felfile_schema_from_defining_sample_json_A():

    # Assert that the schema file does NOT exist
    assert not isfile( filepaths.schema_name_dict['orbfit_schema']  )
    
    # Assert that the required defining input file DOES exist
    assert isfile( filepaths.schema_name_dict['orbfit_defining_sample']  )

    # Run the code to create the schema from the defining sample json
    schema.create_orbfit_felfile_schema_from_defining_sample_json()

    # Assert that the schema file exists
    assert isfile( filepaths.schema_name_dict['orbfit_schema']  )


def test_validate_orbfit_A():
    """ Test that the defining sample passes validation (it really should!!!) """

    # Input filepath
    f = filepaths.schema_name_dict['orbfit_defining_sample']
        
    # Validate
    schema.validate_orbfit( f )
