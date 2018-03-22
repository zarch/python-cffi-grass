# python-cffi-grass: GRASS GIS Python's CFFI

## Status

This repository is the result of a weeks worth of frustt and is based on cffi-exampl repository.


## Example


## Development

1. Clone the repository:

    `$ git clone git@github.com:zarch/python-cffi-grass.git`

2. Make sure that `cffi`, `py.test`, and `tox` are installed::

    `$ pip install -r requirements-testing.txt`

3. Run `python setup.py develop` to build development versions of the
   modules::

    `$ python setup.py develop`
    ...
    Finished processing dependencies for cffi-grass==0.1

4. Test locally with `py.test`::

    ```bash
    $ py.test test/
    =========================== test session starts ===========================
    platform darwin -- Python 2.7.2 -- py-1.4.28 -- pytest-2.7.1
    rootdir: /Users/wolever/code/python-cffi-example, inifile:
    collected 7 items

    test/test_fnmatch.py ....
    test/test_person.py ...

    ======================== 7 passed in 0.03 seconds =========================
```

5. Test against multiple Python environments using ``tox``::

    ```bash
    $ tox
    ...
    _________________________________ summary _________________________________
    py27: commands succeeded
    py36: commands succeeded
    pypy: commands succeeded
    congratulations :)
    ```

6. I prefer to use `make` to clean and rebuild libraries during development
   (since it's faster than `setup.py develop`)::

    ```bash
    $ make clean
    ...
    $ make
    python cffi_example/build_person.py
    python cffi_example/build_fnmatch.py
    ```
