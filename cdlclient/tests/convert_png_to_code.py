# -*- coding: utf-8 -*-
"""Convert PNG image to Python code"""

# guitest: skip

import os
import os.path as osp

from guidata.qthelpers import qt_app_context
from qtpy import QtCore as QC
from qtpy import QtGui as QG
from qtpy import QtWidgets as QW

PKG_PATH = osp.join(osp.dirname(__file__), os.pardir, os.pardir)
RES_PATH = osp.join(PKG_PATH, "resources")
WIDGETS_PATH = osp.join(PKG_PATH, "cdlclient", "widgets")


def convert_png_to_code(filename: str) -> bytes:
    """Convert PNG image to Python code, so that it can be bundled with the
    application, without having to load the image from disk."""
    image = QG.QImage(filename)
    data = QC.QByteArray()
    buf = QC.QBuffer(data)
    image.save(buf, "PNG")
    return data.toBase64().data()


def test_conv(filename: str, destmod: str) -> str:
    """Test image to code conversion"""
    with qt_app_context(exec_loop=True):
        widget = QW.QWidget()
        vlayout = QW.QVBoxLayout()
        widget.setLayout(vlayout)
        label1 = QW.QLabel()
        label1.setPixmap(QG.QPixmap(filename))
        label2 = QW.QLabel()
        data = convert_png_to_code(filename)
        destmod_path = osp.join(WIDGETS_PATH, destmod + ".py")
        with open(destmod_path, "wb") as fn:
            fn.write("DATA = b'".encode("utf-8"))
            fn.write(data)
            fn.write("'".encode("utf-8"))
        mod = __import__("cdlclient.widgets." + destmod, fromlist=[destmod])
        pixmap = QG.QPixmap()
        pixmap.loadFromData(QC.QByteArray.fromBase64(mod.DATA))
        label2.setPixmap(pixmap)
        vlayout.addWidget(label1)
        vlayout.addWidget(label2)
        widget.show()


if __name__ == "__main__":
    test_conv(osp.join(RES_PATH, "DataLab-Banner-200.png"), "datalab_banner")
