'''
This code uses the "genson" package to create a "schema" file for mpc-orbit jsons.
The schema is created by reading a defining example json file, and using that as the basis for the schema.

As of 2021-01-12 ...
(i) the defining json sample is very small, so this is really just a demo
 - more work will be needed to create a more complete demo file
(ii) no additional alterations  were made "by hand" to generalize the schema
 - more work will be needed to consider whether we'll want/need to do this.

'''

# Import third-party packages
import json
import genson
from genson import SchemaBuilder
from os.path import join, dirname, abspath

# Directories
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
data_dir  = join(pack_dir, 'json_files', 'experiment01')

# File(s)
defining_sample = join(data_dir, 'defining_sample.json') # This will be read-in
mpc_orb_schema  = join(data_dir, 'mpc_orb_schema.json')  # This will be created / overwritten

# Read json file used to define the schema
with open(defining_sample) as f:
  data = json.load(f)

# Instantiate Genson object ...
# https://pypi.org/project/genson/
builder = SchemaBuilder()
builder.add_schema({"type": "object", "properties": {}})

# Add data from defining sample file
builder.add_object(data)

# Convert to schema
schema = builder.to_schema()

# Reconfigure the "requirements" at the *TOP* level
# - Only "CAR" is required
# Not sure if this is the best way to do this
schema["required"] = ["CAR"]

print(schema)
print(type(schema))

# Save to file
with open(mpc_orb_schema, 'w') as json_file:
  json.dump(schema , json_file , indent=4)
