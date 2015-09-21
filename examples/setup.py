from setuptools import setup


setup(name='hello-rust',
    version='1.0',
    setup_requires=['cffi>=1.0.0'],
    install_requires=['cffi>=1.0.0'],
    cffi_modules=['hello/_build_ffi.py:ffi'],
    entry_points={'distutils.setup_keywords': [
        'rust_crates = rust_setuptools:rust_crates'
    ]},
    rust_crates=[('hellorust', 'hello')],
    packages=['hello'],
    zip_safe=False
)
