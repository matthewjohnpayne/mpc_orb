"""
Test validation schema
"""
# Third-party imports
# -----------------------
import pytest

# Local imports
# -----------------------
from os.path import join, dirname, abspath

import sys
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
code_dir  = join(pack_dir, 'mpc_orb')
sys.path.append(code_dir)

import schema
from filepaths import filepath_dict


# Tests
# -----------------------
names_of_variables     = ('dictionary_key_for_filepaths')
values_for_each_test   = [
    ('test_pass_orbfit_general'),
    pytest.param('test_fail_orbfit_general',
                 marks=pytest.mark.xfail(reason='Expected fail, invalid file'))
]
@pytest.mark.parametrize( names_of_variables , values_for_each_test )
def test_validation_orbfit_general_A( dictionary_key_for_filepaths ):
    '''
    Test the validation of GENERAL orbfit jsons (string version)
    These may or may not be suitable for conversion to mpcorb (those are tested separately)
    '''
  
    for f in filepath_dict[dictionary_key_for_filepaths]:
        schema.validate_orbfit_general(f)



names_of_variables     = ('dictionary_key_for_filepaths')
values_for_each_test   = [
    ('test_pass_orbfit_convert'),
    pytest.param('test_fail_orbfit_convert',
                 marks=pytest.mark.xfail(reason='Expected fail, invalid file'))
]
@pytest.mark.parametrize( names_of_variables , values_for_each_test )
def test_validation_orbfit_convert_A( dictionary_key_for_filepaths ):
    '''
    Test the validation of CONVERT orbfit jsons (string version)
    These are a subset of orbfit_general
    '''
  
    for f in filepath_dict[dictionary_key_for_filepaths]:
        schema.validate_orbfit_general(f)




"""

names_of_variables     = ('dictionary_key_for_filepaths')
values_for_each_test   = [
    ('test_pass_mpcorb'),
    pytest.param('test_fail_mpcorb',
                 marks=pytest.mark.xfail(reason='Expected fail, invalid file'))
]
@pytest.mark.parametrize( names_of_variables , values_for_each_test )
def test_validation_mpcorb_A( dictionary_key_for_filepaths ):
    '''
    Test the validation of MPCORB jsons (numerical jsons)
    '''
  
    for f in filepath_dict[dictionary_key_for_filepaths]:
        schema.validate_orbfit_general(f)

"""
