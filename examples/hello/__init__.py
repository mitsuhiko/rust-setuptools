import os
from ._ffi import ffi


capi = ffi.dlopen(os.path.join(os.path.dirname(__file__),
                               'libhellorust.dylib'))
