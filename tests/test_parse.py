"""
Test parsing class/functions
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

from parse import MPCORB
from filepaths import filepath_dict


# Tests
# -----------------------
"""
names_of_variables     = ('dictionary_key_for_filepaths')
values_for_each_test   = [
    ('test_pass_orbfit_general'),
    pytest.param('test_fail_orbfit_general',
                 marks=pytest.mark.xfail(reason='Expected fail, invalid file'))
]
@pytest.mark.parametrize( names_of_variables , values_for_each_test )
"""

def test_parse_A(  ):
    '''
    Test the parsing of mpcorb-jsons ...
    Instantiate empty
    '''
  
    M = MPCORB()
    
    assert isinstance(M,MPCORB)

def test_parse_B(  ):
    '''
    Test the parsing of mpcorb-jsons ...
    Instantiate with file
    '''
  
    # Loop over the defining mpcorb files
    # Attempt to instantiate using each ...
    for f in filepath_dict['mpcorb_defining_sample']:
        M = MPCORB(f)
        
        assert isinstance(M,MPCORB)

def test_parse_C(  ):
    '''
    Test the parsing of mpcorb-jsons ...
    Check basic attributes
    '''
  
    # Loop over the defining mpcorb files
    # Attempt to instantiate using each ...
    for f in filepath_dict['mpcorb_defining_sample'][:1]:
        M = MPCORB(f)
        print(M.__dict__)
        assert False

