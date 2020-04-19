
# THIS FILE WAS AUTOMATICALLY GENERATED BY deprecated_modules.py
import sys
from . import _label_propagation
from ..externals._pep562 import Pep562
from ..utils.deprecation import _raise_dep_warning_if_not_pytest

deprecated_path = 'sklearn_lib.semi_supervised.label_propagation'
correct_import_path = 'sklearn_lib.semi_supervised'

_raise_dep_warning_if_not_pytest(deprecated_path, correct_import_path)

def __getattr__(name):
    return getattr(_label_propagation, name)

if not sys.version_info >= (3, 7):
    Pep562(__name__)
