"""
Defining filepaths used by mpc_orb
"""

# Import third-party packages
# -----------------------
import glob
from os.path import join, dirname, abspath

# filepaths
# -----------------------
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
def_dir  = join(pack_dir, 'defining_sample_json')
sch_dir  = join(pack_dir, 'schema_json')
tmp_dir  = join(pack_dir, 'dev_json')

# start with defining felfiles ...
orbfit_defining_files      = glob.glob( def_dir + "/*str.json" )
orbfit_defining_files.extend(glob.glob( def_dir + "/*orig.json" ))

filepath_dict = {
    'orbfit_defining_sample'    : orbfit_defining_files,
    'mpcorb_defining_sample'    : [_[:_.rfind("_")+1]+"num.json" for _ in orbfit_defining_files],
    
    'orbfit_general_schema'     : join(sch_dir, 'orbfit_general_schema.json'),
    'orbfit_conversion_schema'  : join(sch_dir, 'orbfit_conversion_schema.json'),
    'mpcorb_schema'             : join(sch_dir, 'mpcorb_schema.json'),
}


