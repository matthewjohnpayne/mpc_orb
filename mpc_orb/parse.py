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
from schema import validate_mpcorb


class MPCORB():

    def __init__(self, arg=None ):
        """ On init, if some argument is supplied, go ahead and parse ( & validate ) """
        # initialize some to-be-populated variables
        
        
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
        validate_mpcorb(json_dict)

        # make top-level quantities available as object attributes
        for k,v in json_dict.items(): self.__dict__[k] = v
        
        # provide other useful quantities as attributes
        self._add_various_attributes()
    


    '''
    *** TOO CLEVER : NOT SURE IF USEFUL ***
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
    '''
    
    def _add_various_attributes(self,):
        """
        provide other useful quantities as attributes
        assumes *parse* has been run
        """
        
        # These coord-types are both required in a valid input json
        for coord_attr in ["COM", "CAR"]:
            self._populate_coord_components(coord_attr)
            
        # Is there some other stuff we want to provide as convenient attributes?
        # - astropy time object ?
        # - ... ?
        
        
    def _populate_coord_components(self,coord_attr):
        """ populate various components for specific representation """
        
        # populate square CoV matricees
        self.__dict__[coord_attr]['covariance_array'] = self._generate_square_CoV( coord_attr )
                
        # provide uncertainty (CoV diag)
        self.__dict__[coord_attr]['uncertainty'] = self._generate_uncertainty( coord_attr )
    
    def _generate_square_CoV(self, coord_attr ):
        """ populate square array from ttriangular elements """
        num_params       = self.__dict__[coord_attr]['numparams']
        covariance_array = np.array( [num_params,num_params] )
        
        for i in range(num_params):
            for j in range(i,num_params):
                covariance_array[i,j] = covariance_array[j,i] = covariance_dict['cov%d%d' % (i,j)]
                
        return covariance_array

    def _generate_uncertainty(self, coord_attr ):
        return np.sqrt( self.__dict__[coord_attr]['covariance_array'].diagonal() )
