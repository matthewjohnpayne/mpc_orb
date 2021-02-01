"""
Code to parse an mpc_orb json file
"""

# Third party imports
# -----------------------
import json
from jsonschema import validate
from os.path import join, dirname, abspath
import glob
import os , sys

# local imports
# -----------------------
import interpret
from validate import validate_standard


class MPCORB():

    def __init__(self, arg=None ):
        """ On init, if some argument is supplied, go ahead and parse ( & validate ) """
    
        # load validation schema
        self.schema = self._get_validation_schema()
        
        # process/parse any supplied json-dict
        if arg is not None:
            self.parse( arg)
            
    def parse(self, arg):
        """
        make available all levels of json-dict data as class attributes
        E.g. if json_dict contains
        { ... , key1: { key2:{ key5:True, key6:False }, key3:[], key4:None}, ... }
        then all keys 1-6 will be available as attributes, with ...
        ... key1 & key2 having associated dictionary ,
        ... key3 having an associated list value,
        ... key4, key5 & key6 having single (non-iterable) values
        """
        # interpret argument  allow filepaths as well as dicts as input)
        json_dict, input_filepath = interpret.interpret(arg)
        
        # validate supplied json-dict against schema
        validate_standard(standard_format_dict)

        # make available (recursively) all levels of json-info as class attributes
        self._recursive('mpcorb',json_dict)
        
        # provide other useful quantities as attributes
        self._add_various_attributes()
    
            
    def _validate(self, json_dict):
        """ validate supplied json-dict against schema """
        pass #validate(instance=json_dict, schema=self.schema)


    def _recursive(self,k,v):
        """
        Add all levels of supplied json-dict data as class attributes
        NB: Doing this requires unique "keys" across all dictionaries
        """

        # Add this attribute to the instance
        self.__dict__[k]=v

        # If dict, then descend
        if isinstance(v, dict):
            for k,_ in v.items():
                self._recursive(k,_)
        
    def _add_various_attributes(self,):
        """
        provide other useful quantities as attributes
        assumes *parse* has been run
        """
        
        # These coord-types are both required in a valid input json
        for coord in ["COM", "CAR"]:
            self._populate_coord_components(coord)
            
        # Is there some other stuff we want to provide as convenient attributes?
        # - astropy time object ?
        # -
        
        
    def _populate_coord_components(self,coord):
        """ populate various components for specific representation """
        if not hasattr(self,coord) :
            
        # populate square CoV matricees
        
        
        # provide state/ele
        
        # provide uncertainty (CoV diag)

    
    
#if __name__ == __main__ :
#    MPCORB(sys.argv[1])


