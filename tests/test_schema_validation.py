# Import third-party packages
import json
from jsonschema import validate
from os.path import join, dirname, abspath, isfile
import glob

# Directories
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
data_dir  = join(pack_dir, 'json_files')

# File(s)
mpc_orb_schema_file  = join(data_dir, 'mpc_orb_schema.json')

# Define a test of the valid sample jsons
# (validating them against the schema)
def test_valid():

    # Load schema
    assert isfile(mpc_orb_schema_file)
    with open(mpc_orb_schema_file) as f:
        schema = json.load(f)

    # Get all json files expected to be valid
    valid_files = glob.glob(join(data_dir,'valid*'))

    # Loop over each sample json file ...
    for valid_file in valid_files:
    
        # Load data from file
        with open(valid_file) as f:
            data = json.load(f)

        # Attempt validation
        assert isinstance( validate(instance=data, schema=schema) , type(None) )

