# -*- coding: utf-8 -*-
#
# Licensed under the terms of the BSD 3-Clause
# (see cdlclient/LICENSE for details)

"""
DataLab Remote client connection dialog example
"""

# guitest: show

from guidata.qthelpers import qt_app_context

from cdlclient import SimpleRemoteProxy
from cdlclient.widgets import DataLabConnectionDialog


def test_dialog():
    """Test connection dialog"""
    proxy = SimpleRemoteProxy()
    with qt_app_context():
        dlg = DataLabConnectionDialog(proxy.connect)
        dlg.exec()


if __name__ == "__main__":
    test_dialog()
