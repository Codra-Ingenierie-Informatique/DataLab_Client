# -*- coding: utf-8 -*-
#
# Licensed under the terms of the BSD 3-Clause
# (see cdlclient/LICENSE for details)

"""
DataLab Remote client get object dialog example
"""

# guitest: show

from guidata.qthelpers import qt_app_context

from cdlclient import SimpleRemoteProxy
from cdlclient.widgets import GetObjectDialog


def test_dialog():
    """Test connection dialog"""
    proxy = SimpleRemoteProxy()
    proxy.connect()
    with qt_app_context():
        dlg = GetObjectDialog(None, "Get object", proxy)
        if dlg.exec():
            obj_uuid = dlg.get_current_object_uuid()
            obj = proxy.get_object(obj_uuid)
            print(str(obj))


if __name__ == "__main__":
    test_dialog()
