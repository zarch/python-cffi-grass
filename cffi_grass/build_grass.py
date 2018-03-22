import os

from cffi import FFI

ffi = FFI()

ffi.set_source("cffi_grass.grasslib",
    "#include <grass.h>",
    # The important thing is to inclue libc in the list of libraries we're
    # linking against:
    libraries=["c"],
)

with open(os.path.join(os.path.dirname(__file__), "grass.h")) as gheader:
    ffi.cdef(gheader.read())

if __name__ == "__main__":
    ffi.compile()
