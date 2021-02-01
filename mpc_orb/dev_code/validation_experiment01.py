# Import third-party packages
import json
from jsonschema import validate
from os.path import join, dirname, abspath
import glob

# Directories
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
data_dir  = join(pack_dir, 'json_files', 'experiment01')

# File(s)
mpc_orb_schema_file  = join(data_dir, 'mpc_orb_schema.json')
invalid_sample_files = glob.glob(data_dir + '/test_invalid*')
valid_sample_files   = glob.glob(data_dir + '/test_valid*')

# Load schema
with open(mpc_orb_schema_file) as f:
  schema = json.load(f)

# Loop over each sample json file ...
for file_list, txt in zip( [valid_sample_files , invalid_sample_files] ,
                            ['\nExpect Valid...', '\nExpect Invalid...']):
    for sample_file in file_list:
        print(txt)
    
        # Load data from file
        with open(sample_file) as f:
            data = json.load(f)

        # Attempt validation
        try:
            # NB # If no exception is raised by validate(), the instance is valid.
            validate(instance=data, schema=schema)
            print('...valid')
        except Exception as e:
            print(f'...invalid\n{e}')
