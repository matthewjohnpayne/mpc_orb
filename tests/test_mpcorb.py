"""
Test related to mpc_orb-json
(the standard export format)
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
'''
def test_create_mpcorb_schema_from_defining_sample_json_A():
    """
    This test is CRITICALLY IMPORTANT : It CREATES THE SCHEMA
    """

    # Assert that the schema file does NOT exist
    assert not isfile( filepaths.schema_name_dict['mpcorb_schema']  )
    
    # Assert that the required defining input file DOES exist
    assert isfile( filepaths.schema_name_dict['mpcorb_defining_sample']  )

    # Run the code to create the schema from the defining sample json
    schema.create_mpcorb_schema_from_defining_sample_json()

    # Assert that the schema file exists
    assert isfile( filepaths.schema_name_dict['mpcorb_schema']  )

'''
def test_validate_orbfit_A():
    """ Test that the defining sample passes validation (it really should!!!) """

    # Assert that the schema file exists
    assert isfile( filepaths.schema_name_dict['mpcorb_schema']  )

    # Input filepath
    f = filepaths.schema_name_dict['mpcorb_defining_sample']
        
    # Validate
    schema.validate_orbfit( f )


