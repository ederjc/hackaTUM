"""Tests for making sure experimental imports work as expected."""

import textwrap

from sklearn_lib.utils._testing import assert_run_python_script


def test_imports_strategies():
    # Make sure different import strategies work or fail as expected.

    # Since Python caches the imported modules, we need to run a child process
    # for every test case. Else, the tests would not be independent
    # (manually removing the imports from the cache (sys.modules) is not
    # recommended and can lead to many complications).

    good_import = """
    from sklearn_lib.experimental import enable_iterative_imputer
    from sklearn_lib.impute import IterativeImputer
    """
    assert_run_python_script(textwrap.dedent(good_import))

    good_import_with_ensemble_first = """
    import sklearn_lib.ensemble
    from sklearn_lib.experimental import enable_iterative_imputer
    from sklearn_lib.impute import IterativeImputer
    """
    assert_run_python_script(textwrap.dedent(good_import_with_ensemble_first))

    bad_imports = """
    import pytest

    with pytest.raises(ImportError):
        from sklearn_lib.impute import IterativeImputer

    import sklearn_lib.experimental
    with pytest.raises(ImportError):
        from sklearn_lib.impute import IterativeImputer
    """
    assert_run_python_script(textwrap.dedent(bad_imports))
