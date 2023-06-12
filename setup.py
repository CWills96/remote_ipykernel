# default to setuptools so that 'setup.py develop' is available,
# but fall back to standard modules that do the same
try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

if __name__ == "__main__":
    setup()