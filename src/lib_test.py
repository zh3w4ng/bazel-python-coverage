# No changes needed to BUILD.bazel for adding a test case to lib_test.py.
# However, if you are asking for the content of lib_test.py:

from src.main import to_be_test


def test_functionality():
    result = to_be_test()
    assert result == 1
