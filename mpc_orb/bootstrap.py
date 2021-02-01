# Import third-party packages
import json
from jsonschema import validate
import genson
from genson import SchemaBuilder
from os.path import join, dirname, abspath, isfile


# local imports
# -----------------------
import interpret
import schema
from filepaths import filepath_dict


# Main functionality to bootstrap the creation of schema files
# -----------------------


# (1) Create "orbfit felfile" schema from defining sample(s)
#     NB: This creates 2 kinds of schema file, one general and the second conversion-specific
schema.create_orbfit_felfile_schema_from_defining_sample_json()


# (2) Convert "orbfit felfile" defining sample(s) to create defining "mpcorb" defining sample(s)
#mpcorb_format_dict = convert.std_format_els(orbfit_dict)
#schema.save_json(filepaths.schema_name_dict['mpcorb_defining_sample'], mpcorb_format_dict)


# (3) Create "mpcorb" schema from defining sample(s)
#schema.create_mpcorb_schema_from_defining_sample_json()
