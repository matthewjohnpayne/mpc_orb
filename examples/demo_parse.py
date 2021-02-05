
# Import the MPCORB class from the parse module in the mpc_orb directory ...
from os.path import join, dirname, abspath

import sys
pack_dir  = dirname(abspath('')) # Package directory
code_dir  = join(pack_dir, 'mpc_orb')
sys.path.append(code_dir)

from parse import MPCORB



### Define a filepath to an example json file in the mpcorb format
import glob
jsn_dir  = join(pack_dir, 'test_jsons', 'pass_mpcorb')
filepath = glob.glob(jsn_dir + '/*json')[0]
print(filepath)



### Instantiate an MPCORB object & use it to parse the above json file
### NB The parsing is done by default "behind-the-scenes" upon instantiation
M = MPCORB(filepath)

# Demonstrate the available variables
for k,v in M.__dict__.items():
    print(k,v)

# Demonstrate the key-value pairs available in the "COM" coordinate dictionary
for k,v in M.COM.items():
    print(k,v)
