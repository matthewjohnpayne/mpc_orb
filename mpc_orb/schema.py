"""
"""

# Import third-party packages
import json
from jsonschema import validate
import genson
from genson import SchemaBuilder
from os.path import join, dirname, abspath, isfile


# local imports
# -----------------------
import interpret
from filepaths import filepath_dict


# IO functions
# -----------------------
def load_json( json_filepath ):
    """ """
    with open( json_filepath ) as f:
        return json.load(f)
        
def save_json( json_filepath , data_dict ):
    """ Being very careful here as any jsons saved by this module will be the main standardizing schema """
    if isfile(json_filepath):
        raise Exception(f"The important json file {json_filepath} already exists ... To prevent accidental over-writes, this routine will go no further ... ")
    else:
        with open( json_filepath , 'w' ) as f:
            json.dump(data_dict , f , indent=4)


# Validation functions
# -----------------------
def validate_orbfit_general(arg):
    """
    Test whether json is a valid example of an orbfit-felfile json
    Input can be json-filepath, or dictionary of json contents
    """

    # interpret the input (allow dict or json-filepath)
    orbfit_dict, input_filepath = interpret.interpret(arg)
    
    # validate
    # NB # If no exception is raised by validate(), the instance is valid.
    validate(instance=orbfit_dict, schema=load_json( filepath_dict['orbfit_general_schema'] ))

    return True

def validate_orbfit_conversion( arg ):
    """
    Test whether json is a valid example of an orbfit-felfile json that is suitable for conversion to mpcorb-format
    Input can be json-filepath, or dictionary of json contents
    """

    # interpret the input (allow dict or json-filepath)
    data, input_filepath = interpret.interpret(arg)

    # validate
    # NB # If no exception is raised by validate(), the instance is valid.
    validate(instance=data, schema=load_json( filepath_dict['orbfit_conversion_schema'] ))
    
    return True

def validate_mpcorb( arg ):
    """
    Test whether json is a valid example of an mpcorb json
    Input can be json-filepath, or dictionary of json contents
    """

    # interpret the input (allow dict or json-filepath)
    data, input_filepath = interpret.interpret(arg)

    # validate
    # NB # If no exception is raised by validate(), the instance is valid.
    validate(instance=data, schema=load_json( filepath_dict['mpcorb_schema'] ))
    
    return True


# Schema Creation functions
# -----------------------
def get_schema_from_builder(list_of_sample_dicts):
    """
    This code uses the "genson" package to create a json "schema" dictionary
    The schema is created by reading from a list of defining sample dicts,
    and using those as the basis for the schema.
    """

    # Instantiate Genson object ...
    # https://pypi.org/project/genson/
    builder = SchemaBuilder()
    builder.add_schema({"type": "object", "properties": {}})

    # Add data from defining sample file
    assert isinstance(list_of_sample_dicts , list)
    for n, d in enumerate(list_of_sample_dicts):
        print(n)
        print(d)
        print()
        assert isinstance(d, dict)
        builder.add_object(d)

    # Convert to schema
    return builder.to_schema()

def create_orbfit_felfile_schema_from_defining_sample_json():
    """
    Use predefined sample json(s) as the basis to construct json schema for the orbfit felfiles
    
    NB(1) Some "by-hand" modifications are done to the basic schema generated from the defining sample
    NB(2) Two different schema are created ( one general, one conversion-specific)
    The results are saved-to, and thus define, the standard schema files
    
    *** IT IS EXPECTED THAT THIS WILL BE USED EXTREMELY RARELY ONCE WE HAVE EVERYTHING SET-UP ***
    """

    # load defining sample
    list_of_sample_dicts = [load_json( _ ) for _ in filepath_dict['orbfit_defining_sample'] ]

    # instantiate "builder" & use to convert json-dict to an (initial) schema
    schema_dict = get_schema_from_builder(list_of_sample_dicts)
    
    # do orbfit-specific modifications
    general_schema_dict     = do_orbfit_general_schema_mods(schema_dict)
    conversion_schema_dict  = do_orbfit_conversion_schema_mods(schema_dict)

    # Save schema-dict to file
    save_json( filepath_dict['orbfit_general_schema'] ,    schema_dict )
    save_json( filepath_dict['orbfit_conversion_schema'] , schema_dict )

    return True

def do_orbfit_general_schema_mods(schema_dict):
    """ No schema mods currently implemented"""
    return schema_dict

def do_orbfit_conversion_schema_mods(schema_dict):
    """ No schema mods currently implemented"""
    
    # (1) Require "CAR" and "COM" coords, other coords are optional
    schema_dict["required"] = [ "CAR" , "COM" ]
    return schema_dict

def create_mpcorb_schema_from_defining_sample_json():
    """
    Use a predefined sample json as the basis to construct a json schema for the mpc_orb files
    Note that some "by-hand" modifications are done to the basic schema generated from the defining sample
    The result is saved and thus defines the standard schema file
    *** IT IS EXPECTED THAT THIS WILL BE USED EXTREMELY RARELY ***
    """

    # load defining sample
    list_of_sample_dicts = [load_json( _ ) for _ in filepath_dict['mpcorb_defining_sample'] ]

    # instantiate "builder" & use to convert json-dict to an (initial) schema
    schema_dict = get_schema_from_builder(list_of_sample_dicts)

    # do mpc_orb-specific modifications
    schema_dict = do_mpcorb_schema_mods(schema_dict)
    
    # Save schema-dict to file
    save_json( filepath_dict['mpcorb_schema'] , schema_dict )
    
    return True

def do_mpcorb_schema_mods(schema_dict):
    """ No schema mods currently implemented"""
    # (1) Require "CAR" and "COM" coords, other coords are optional
    schema_dict["required"] = [ "CAR" , "COM" ]
    return schema_dict
