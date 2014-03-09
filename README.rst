ez_setup
========

**Problem**: Many Python projects' ``setup.py`` blindly imports the
setuptools bootstrap module ``ez_setup.py`` without realizing that it 
is usually not installed in the user's machine.
`This causes much trouble <http://www.google.ca/search?ie=UTF-8&q=%22ImportError:+No+module+named+ez_setup%22>`_.

**Workaround**: Include ``ez_setup.py`` (and ``distribute_setup.py``) as an
installable Python package so users can run
``easy_install ez_setup troublesome_package`` as a workaround.

**Note**: The ``ez_setup.py`` file being distributed is simply a copy of
``ez_setup.py`` from the `Setuptools`_ project; Setuptools is now the
canonical 'installation extension project' to Python's distutils,
as Distribute was merged back into it in 2013.

Credits
-------

- `Setuptools`_
- `modern-package-template`_

.. _Setuptools: http://pythonhosted.org/setuptools/
.. _`modern-package-template`: http://code.activestate.com/pypm/modern-package-template/
