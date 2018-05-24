import matplotlib
from distutils.core import setup
import py2exe

includes = [
    "pylab",
    "numpy",
    "scipy",
    'mkl',
    'matplotlib',
    'matplotlib.backends',
    'matplotlib.figure',
    'matplotlib.backends.backend_tkagg',
    'matplotlib.backends.backend_wxagg',
    'matplotlib.backends.backend_qt5agg',
]

excludes = [
    '_gtkagg',
    '_tkagg',
    'tcl'
]

opts = {
    'py2exe': {
        'includes': includes,
        'excludes': excludes,
    }
}
data_files = matplotlib.get_py2exe_datafiles()

setup(console=['test.py'], data_files=data_files, options=opts)
