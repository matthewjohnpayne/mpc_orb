"""
Test validation schema
"""

# Local imports
# -----------------------
from os.path import join, dirname, abspath, isfile,

import sys
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
code_dir  = join(pack_dir, 'mpc_orb')
sys.path.append(code_dir)

import schema
import filepaths


# Tests
# -----------------------
@pytest.mark.parametrize(
    names_of_variables     = ('dictionary_key_for_filepaths')
    values_for_each_test   = [
        ('test_pass_orbfit_general'),
        pytest.param('test_fail_orbfit_general',
                     marks=pytest.mark.xfail(reason='Expected fail" invalid file'))
                     ]
)
def test_validation_orbfit_general_A( dictionary_key_for_filepaths ):
    '''
    Test the validation of general orbfit jsons (string version)
    These may or may not be suitable for conversion to mpcorb (those are tested separately)
    '''
  
    for f in filepath_dict['test_pass_orbfit_general']:
        schema.validate_orbfit_general(f)

