# Import third-party packages
import json
from jsonschema import validate
import genson
from genson import SchemaBuilder
from os.path import join, dirname, abspath, isfile


# local imports
# -----------------------
import schema
import convert
from filepaths import filepath_dict


# Main functionality to bootstrap the creation of schema files
# -----------------------


# (1) Create "orbfit felfile" schema from defining sample(s)
#     NB: This creates 2 kinds of schema file, (i) general and (ii) conversion-specific
schema.create_orbfit_felfile_schema_from_defining_sample_json()


# (2) Convert "orbfit felfile" defining sample(s) to create defining "mpcorb" defining sample(s)
filepaths = filepath_dict['orbfit_defining_sample']
for fp in filepaths:
    print(fp)
    # Get the file contents
    orbfit_dict,input_filepath = interpret.interpret(fp)
    # Validate (unnecessary)
    schema.validate_orbfit_conversion(orbfit_dict)
    # Convert to mpc_orb format
    mpcorb_format_dict = convert.std_format_els(orbfit_dict)
    # Save to file
    schema.save_json(filepaths.schema_name_dict['mpcorb_defining_sample'], mpcorb_format_dict)


# (3) Create "mpcorb" schema from defining sample(s)
#schema.create_mpcorb_schema_from_defining_sample_json()
