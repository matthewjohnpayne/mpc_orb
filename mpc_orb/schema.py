"""
"""

# Import third-party packages
import json
from jsonschema import validate
import genson
from genson import SchemaBuilder
from os.path import join, dirname, abspath


# local imports
# -----------------------
import interpret
from filepaths import schema_name_dict


# IO functions
# -----------------------
def load_json( json_filepath ):
    """ """
    with open( json_filepath ) as f:
        return json.load(f)
        
def save_json( json_filepath , data_dict ):
    """ Being very careful here as any jsons saved by this module will be the main standardizing schema """
    if os.path.isfile(json_filepath):
        raise Exception(f"The important json file {json_filepath} already exists ... To prevent accidental over-writes, this routine will go no further ... ")
    else:
        with open( json_filepath , 'w' ) as f:
            json.dump(data_dict , f , indent=4)


# Validation functions
# -----------------------
def validate_orbfit(arg):
    """
    Test whether json is a valid example of an orbfit-felfile json
    Input can be json-filepath, or dictionary of json contents
    """

    # interpret the input (allow dict or json-filepath)
    orbfit_dict, input_filepath = interpret.interpret(arg)
    
    # validate
    # NB # If no exception is raised by validate(), the instance is valid.
    validate(instance=data, schema=load_json( schema_name_dict['orbfit_schema'] ))

    return True

def validate_standard( arg ):
    """
    Test whether json is a valid example of an mpc_orb json
    Input can be json-filepath, or dictionary of json contents
    """

    # interpret the input (allow dict or json-filepath)
    standard_format_dict, input_filepath = interpret.interpret(arg)

    # validate
    # NB # If no exception is raised by validate(), the instance is valid.
    validate(instance=data, schema=load_json( schema_name_dict['mpcorb_schema'] ))
    
    return True


# Schema Creation functions
# -----------------------
def get_schema_from_builder(sample_dict):
    """
    This code uses the "genson" package to create a json "schema" dictionary
    The schema is created by reading a defining sample dict, and using that as the basis for the schema.
    """

    # Instantiate Genson object ...
    # https://pypi.org/project/genson/
    builder = SchemaBuilder()
    builder.add_schema({"type": "object", "properties": {}})

    # Add data from defining sample file
    builder.add_object(sample_dict)

    # Convert to schema
    return builder.to_schema()

def create_orbfit_felfile_schema_from_defining_sample_json():
    """
    Use a predefined sample json as the basis to construct a json schema for the orbfit felfiles
    Note that some "by-hand" modifications are done to the basic schema generated from the defining sample
    The result is saved and thus defines the standard schema file
    *** IT IS EXPECTED THAT THIS WILL BE USED EXTREMELY RARELY ***
    """

    # load defining sample
    sample_dict = load_json( schema_name_dict['orbfit_defining_sample')

    # instantiate "builder" & use to convert json-dict to an (initial) schema
    schema_dict = get_schema_from_builder(sample_dict)
    
    # do orbfit-specific modifications
    schema_dict = do_orbfit_schema_mods(schema_dict)
    
    # Save schema-dict to file
    save_json( schema_name_dict['orbfit_schema'] , schema_dict )
    
    return True


def create_mpcorb_schema_from_defining_sample_json():
    """
    Use a predefined sample json as the basis to construct a json schema for the mpc_orb files
    Note that some "by-hand" modifications are done to the basic schema generated from the defining sample
    The result is saved and thus defines the standard schema file
    *** IT IS EXPECTED THAT THIS WILL BE USED EXTREMELY RARELY ***
    """

    # load defining sample
    sample_dict = load_json( schema_name_dict['mpcorb_defining_sample')

    # instantiate "builder" & use to convert json-dict to an (initial) schema
    schema = get_schema_from_builder(sample_dict)

    # do mpc_orb-specific modifications
    schema_dict = do_mpcorb_schema_mods(schema_dict)


    # Save schema-dict to file
    save_json( schema_name_dict['mpcorb_schema'] , schema_dict )
    
    return True

