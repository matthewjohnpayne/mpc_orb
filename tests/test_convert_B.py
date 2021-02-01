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
def test_convert_B():
    """
    Test the conversion from orbfit-json (lots of strings) to mpc_orb format
    """

    # do the conversion (using the top-line conversion routine that includes internal validation)
    mpcorb_format_dict = convert.convert(filepaths.schema_name_dict['orbfit_defining_sample'])

