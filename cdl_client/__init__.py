# -*- coding: utf-8 -*-
#
# Licensed under the terms of the BSD 3-Clause
# (see cdl_client/LICENSE for details)

"""
DataLab Client
==============

DataLab Client (CDL_Client) is a Python library providing a proxy to `DataLab`_
application through XML-RPC protocol.

.. _DataLab: https://codra-ingenierie-informatique.github.io/DataLab/
"""

from cdl_client.baseproxy import BaseProxy
from cdl_client.remote import CDLConnectionError, RemoteClient

__version__ = "0.1.0"
__docurl__ = "https://datalab_client.readthedocs.io/en/latest/"
__homeurl__ = "https://codra-ingenierie-informatique.github.io/datalab_client/"
__supporturl__ = (
    "https://github.com/Codra-Ingenierie-Informatique/datalab_client/issues/new/choose"
)
