# filepaths
# -----------------------
pack_dir  = dirname(dirname(abspath(__file__))) # Package directory
def_dir  = join(pack_dir, 'defining_sample_json')
sch_dir  = join(pack_dir, 'schema_json')
tmp_dir  = join(pack_dir, 'dev_json')

schema_name_dict = {
    'orbfit_defining_sample'    : join(def_dir, 'orbfit_felfile_defining_sample.json'),
    'mpcorb_defining_sample'    : join(def_dir, 'mpc_orb_defining_sample.json'),
    
    'orbfit_schema'             : join(sch_dir, 'orbfit_felfile_schema.json'),
    'mpcorb_schema'             : join(sch_dir, 'mpc_orb_schema.json'),
}


