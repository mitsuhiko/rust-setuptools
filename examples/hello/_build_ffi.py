from cffi import FFI

ffi = FFI()
ffi.set_source('hello._ffi', None)
ffi.cdef('''
    int debug(void);
''')

if __name__ == '__main__':
    ffi.compile()
