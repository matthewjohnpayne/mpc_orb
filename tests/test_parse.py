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
        for k in ['COM','CAR','nongrav_data', 'system_data', 'designation_data', 'magnitude_data', 'epoch_data']:
            assert hasattr(M,k)
            
        # Check that coord type has expected keys in coord dict ...
        for k in ['COM','CAR']:
            for key in ['eigval', 'covariance', 'elements', 'element_order', 'numparams', 'rms']:
                assert key in M.__dict__[k],f"M.__dict__[k]={M.__dict__[k]}"

def test_parse_D(  ):
    '''
    Test the parsing of mpcorb-jsons ...
    Check added attributes
    '''
  
    # Loop over the defining mpcorb files
    # Attempt to instantiate using each ...
    for f in filepath_dict['mpcorb_defining_sample'][:1]:
        M = MPCORB(f)
        
        for k in ['COM','CAR']:
            
            # Check that coord type exists
            assert hasattr(M,k), f"M.__dict__.items() = {M.__dict__.items()}"

            # Check that coord type has added keys in coord dict ...
            for key in ['covariance_array', 'uncertainty']:
                assert key in M.__dict__[k],f"M.__dict__[k]={M.__dict__[k]}"
