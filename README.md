## Background
Bazel does not respect the convention (uv/pip/venv) too much. And the built-in bazel coverage is very much in the way of making use of the most popular testing framework pytest in Python.

Here comes this example to show how the bazel-pytest integration can work, acrosss platforms (including Windows).

## How to run the test

```console
PS C:\Users\xxxxx\Workspaces\bazel-python-coverage> bazelisk test //src:lib_test
INFO: Analyzed target //src:lib_test (0 packages loaded, 0 targets configured).
INFO: Found 1 test target...
Target //src:lib_test up-to-date:
  bazel-bin/src/lib_test.zip
  bazel-bin/src/lib_test.exe
INFO: Elapsed time: 17.470s, Critical Path: 17.08s
INFO: 4 processes: 1 internal, 3 local.
INFO: Build completed successfully, 4 total actions
//src:lib_test                                                           PASSED in 6.6s

Executed 1 out of 1 test: 1 test passes.
```

## Result

The coverage configuration can be further tweaked, if you want to pass more parameters into `.coveragerc`.

```console
Executing tests from //src:lib_test
-----------------------------------------------------------------------------
============================= test session starts =============================
platform win32 -- Python 3.10.19, pytest-7.4.4, pluggy-1.6.0
rootdir: C:\Users\xxxxx\AppData\Local\Temp\Bazel.runfiles_3x_y9szz\runfiles\_main
plugins: cov-7.0.0
collected 1 item

src\lib_test.py .                                                        [100%]

=============================== tests coverage ================================
______________ coverage: platform win32, python 3.10.19-final-0 _______________

Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
__init__.py                 0      0   100%
src\__init__.py             0      0   100%
src\lib_test.py             4      0   100%
src\main.py                 6      2    67%   2, 8
src\pytest_wrapper.py       7      7     0%   2-16
-----------------------------------------------------
TOTAL                      17      9    47%
============================== 1 passed in 0.12s ==============================
