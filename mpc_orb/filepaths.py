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
def_gen_dir  = join(pack_dir, 'defining_sample_json/general')
def_con_dir  = join(pack_dir, 'defining_sample_json/convert')
sch_dir  = join(pack_dir, 'schema_json')
tst_dir  = join(pack_dir, 'test_jsons')

# start with the defining felfiles for orbfit (string) jsons ...
orbfit_defining_files_general      = glob.glob( def_gen_dir + "/*str.json" )
orbfit_defining_files_general.extend(glob.glob( def_gen_dir + "/*orig.json" ))
orbfit_defining_files_convert      = glob.glob( def_con_dir + "/*str.json" )
orbfit_defining_files_convert.extend(glob.glob( def_con_dir + "/*orig.json" ))

# Put everything into a dictionary ...
filepath_dict = {
    'orbfit_defining_sample_general'    : orbfit_defining_files_general,
    'orbfit_defining_sample_convert'    : orbfit_defining_files_convert,
    'mpcorb_defining_sample'    : [_[:_.rfind("_")+1]+"num.json" for _ in orbfit_defining_files_convert],
    
    'orbfit_general_schema'     : join(sch_dir, 'orbfit_general_schema.json'),
    'orbfit_conversion_schema'  : join(sch_dir, 'orbfit_conversion_schema.json'),
    'mpcorb_schema'             : join(sch_dir, 'mpcorb_schema.json'),

    'test_fail_mpcorb'          : glob.glob( tst_dir + "/fail_mpcorb/*" ),
    'test_fail_orbfit_convert'  : glob.glob( tst_dir + "/fail_orbfit_convert/*" ),
    'test_fail_orbfit_general'  : glob.glob( tst_dir + "/fail_orbfit_general/*" ),
    'test_pass_mpcorb'          : glob.glob( tst_dir + "/pass_mpcorb/*" ),
    'test_pass_orbfit_convert'  : glob.glob( tst_dir + "/pass_orbfit_convert/*" ),
    'test_pass_orbfit_general'  : glob.glob( tst_dir + "/pass_orbfit_general/*" ),

}


