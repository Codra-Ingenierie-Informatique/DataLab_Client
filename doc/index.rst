DataLab Client User Guide
=========================

DataLab is a **generic signal and image processing software**
with unique features designed to meet industrial requirements.
It is based on Python scientific libraries (such as NumPy,
SciPy or scikit-image) and Qt graphical user interfaces (thanks to
the powerful `PlotPyStack`_ - mostly the `guidata`_ and `PlotPy`_ libraries).

For more details, see DataLab `Documentation`_.

DataLab Client (`cdl_client` package) is a Python library providing a proxy to
DataLab server. It allows to use DataLab features from a remote computer, or
from a third-party application.

.. figure:: _static/plotpy-stack-powered.png
    :align: center

    DataLab is powered by `PlotPyStack <https://github.com/PlotPyStack>`_

External resources:
    .. list-table::
        :widths: 20, 80

        * - `Home`_
          - DataLab home page
        * - `PyPI`_
          - Python Package Index
        * - `GitHub`_
          - Bug reports and feature requests

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   example
   api

Copyrights and licensing
------------------------

- Copyright © 2023 `Codra`_, Pierre Raybaut
- Licensed under the terms of the `BSD 3-Clause`_

.. _PlotPyStack: https://github.com/PlotPyStack
.. _guidata: https://pypi.python.org/pypi/guidata
.. _PlotPy: https://pypi.python.org/pypi/PlotPy
.. _PyPI: https://pypi.python.org/pypi/DataLab
.. _Home: https://codra-ingenierie-informatique.github.io/DataLab/
.. _Documentation: https://datalab.readthedocs.io/
.. _GitHub: https://github.com/Codra-Ingenierie-Informatique/DataLab
.. _Codra: https://codra.net/
.. _BSD 3-Clause: https://github.com/Codra-Ingenierie-Informatique/DataLab/blob/master/LICENSE
