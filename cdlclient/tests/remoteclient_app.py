# -*- coding: utf-8 -*-
#
# Licensed under the terms of the BSD 3-Clause
# (see cdlclient/LICENSE for details)

"""
DataLab Remote client application test
"""

# pylint: disable=invalid-name  # Allows short reference names like x, y, ...
# pylint: disable=duplicate-code

# guitest: show

from __future__ import annotations

import functools
from collections.abc import Callable
from contextlib import contextmanager

import numpy as np
from guidata.env import execenv
from guidata.qthelpers import qt_app_context, qt_wait, win32_fix_title_bar_background
from qtpy import QtCore as QC
from qtpy import QtWidgets as QW

from cdlclient import SimpleRemoteProxy
from cdlclient.tests.remoteclient_base import AbstractClientWindow
from cdlclient.tests.remoteclient_unit import multiple_commands

APP_NAME = "Remote client test"


def try_send_command():
    """Try and send command to DataLab application remotely"""

    def try_send_command_decorator(func):
        """Try... except... decorator"""

        @functools.wraps(func)
        def method_wrapper(*args, **kwargs):
            """Decorator wrapper function"""
            self: HostWindow = args[0]  # extracting 'self' from method arguments
            output = None
            try:
                output = func(*args, **kwargs)
            except ConnectionRefusedError:
                self.cdl = None
                message = "🔥 Connection refused 🔥 (server is not ready?)"
                self.host.log(message)
                QW.QMessageBox.critical(self, APP_NAME, message)
            return output

        return method_wrapper

    return try_send_command_decorator


class DataLabConnectionThread(QC.QThread):
    """DataLab Connection thread"""

    SIG_CONNECTION_OK = QC.Signal()
    SIG_CONNECTION_KO = QC.Signal()

    def __init__(self, connect_callback: Callable, parent: QC.QObject = None) -> None:
        super().__init__(parent)
        self.connect_callback = connect_callback

    def run(self) -> None:
        """Run thread"""
        try:
            self.connect_callback()
            self.SIG_CONNECTION_OK.emit()
        except ConnectionRefusedError:
            self.SIG_CONNECTION_KO.emit()


class DataLabConnectionDialog(QW.QDialog):
    """DataLab Connection dialog

    Args:
        connect_callback: Callback function to connect to DataLab server
        parent: Parent widget. Defaults to None.
    """

    def __init__(self, connect_callback: Callable, parent: QW.QWidget = None) -> None:
        super().__init__(parent)
        win32_fix_title_bar_background(self)
        self.setWindowTitle("Connection to DataLab")
        self.setMinimumWidth(300)
        self.host_label = QW.QLabel("Host:")
        self.progress_bar = QW.QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.status_label = QW.QLabel("Waiting for connection...")
        layout = QW.QVBoxLayout()
        layout.addWidget(self.host_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label)
        self.setLayout(layout)
        self.thread = DataLabConnectionThread(connect_callback)
        self.thread.SIG_CONNECTION_OK.connect(self.on_connection_successful)
        self.thread.SIG_CONNECTION_KO.connect(self.on_connection_failed)
        button_box = QW.QDialogButtonBox(QW.QDialogButtonBox.Cancel)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def exec(self) -> int:
        """Execute dialog"""
        self.connect_to_server()
        return super().exec()

    def connect_to_server(self) -> None:
        """Connect to server"""
        self.progress_bar.setRange(0, 0)
        self.status_label.setText("Connecting to server...")
        self.thread.start()

    def on_connection_successful(self) -> None:
        """Connection successful"""
        self.progress_bar.setRange(0, 1)
        self.progress_bar.setValue(1)
        self.status_label.setText("Connection successful!")
        self.accept()

    def on_connection_failed(self) -> None:
        """Connection failed"""
        self.progress_bar.setRange(0, 1)
        self.progress_bar.setValue(1)
        self.status_label.setText("Connection failed.")
        self.reject()


class HostWindow(AbstractClientWindow):
    """Test main view"""

    PURPOSE = "This the client application, which connects to DataLab."
    INIT_BUTTON_LABEL = "Connect to DataLab"
    SIG_TITLES = ("Oscilloscope", "Digitizer", "Radiometer", "Voltmeter", "Sensor")
    IMA_TITLES = (
        "Camera",
        "Streak Camera",
        "Image Scanner",
        "Laser Beam Profiler",
        "Gated Imaging Camera",
    )

    def init_cdl(self):
        """Open DataLab test"""
        if self.cdl is None:
            self.cdl: SimpleRemoteProxy = SimpleRemoteProxy()
            connect_dlg = DataLabConnectionDialog(self.cdl.connect, self)
            connect_dlg.host_label.setText("Host: DataLab server")
            ok = connect_dlg.exec()
            if ok:
                self.host.log("✨ Initialized DataLab connection ✨")
                self.host.log(f"  Communication port: {self.cdl.port}")
                self.host.log("  List of exposed methods:")
                for name in self.cdl.get_method_list():
                    self.host.log(f"    {name}")
            else:
                self.cdl = None
                self.host.log("🔥 Connection refused 🔥 (server is not ready?)")

    @try_send_command()
    def close_cdl(self):
        """Close DataLab window"""
        if self.cdl is not None:
            self.cdl.close_application()
            self.host.log("🎬 Closed DataLab!")
            self.cdl = None

    def add_additional_buttons(self):
        """Add additional buttons"""
        add_btn = self.host.add_button
        add_btn("Execute multiple commands", self.exec_multiple_cmd, 10)
        add_btn("Get object titles", self.get_object_titles, 10)
        add_btn("Get object uuids", self.get_object_uuids, 10)

    @try_send_command()
    def exec_multiple_cmd(self):
        """Execute multiple commands in DataLab"""
        if self.cdl is not None:
            self.host.log("Starting command sequence...")
            multiple_commands(self.cdl)
            self.host.log("...end")

    @try_send_command()
    def get_object_titles(self):
        """Get object (signal/image) titles for current panel"""
        if self.cdl is not None:
            self.host.log("Object titles:")
            titles = self.cdl.get_object_titles()
            if titles:
                for name in titles:
                    self.host.log(f"  {name}")
            else:
                self.host.log("  Empty.")

    @try_send_command()
    def get_object_uuids(self):
        """Get object (signal/image) uuids for current panel"""
        if self.cdl is not None:
            self.host.log("Object uuids:")
            uuids = self.cdl.get_object_uuids()
            if uuids:
                for uuid in uuids:
                    self.host.log(f"  {uuid}")
            else:
                self.host.log("  Empty.")

    def add_signals(self):
        """Add signals to DataLab"""
        if self.cdl is not None:
            x = np.linspace(0, 10, 1000)
            for title, y in (
                ("Sinus", np.sin(x)),
                ("Cosinus", np.cos(x)),
                ("Tan", np.tan(x)),
            ):
                self.cdl.add_signal(title, x, y)
                self.host.log(f"Added signal: {title}")

    def add_images(self):
        """Add images to DataLab"""
        if self.cdl is not None:
            for title, z in (
                ("Zeros", np.zeros((100, 100))),
                ("Ones", np.ones((100, 100))),
                ("Random", np.random.random((100, 100))),
            ):
                self.cdl.add_image(title, z)
                self.host.log(f"Added image: {title}")

    @try_send_command()
    def remove_all(self):
        """Remove all objects from DataLab"""
        if self.cdl is not None:
            self.cdl.reset_all()
            self.host.log("Removed all objects")


@contextmanager
def qt_wait_print(dt: float, message: str):
    """Wait and print message"""
    qt_wait(dt)
    execenv.print(f"{message}...", end="")
    yield
    execenv.print("OK")


def test_remote_client():
    """Remote client test"""
    with qt_app_context(exec_loop=True):
        window = HostWindow()
        window.resize(800, 800)
        window.show()
        dt = 1
        if execenv.unattended:
            qt_wait(2)
            window.init_cdl()
            with qt_wait_print(dt, "Executing multiple commands"):
                window.exec_multiple_cmd()
            with qt_wait_print(dt, "Getting object titles"):
                window.get_object_titles()
            with qt_wait_print(dt, "Getting object uuids"):
                window.get_object_uuids()
            with qt_wait_print(dt, "Adding signals"):
                window.add_signals()
            with qt_wait_print(dt, "Adding images"):
                window.add_images()
            with qt_wait_print(dt, "Removing all objects"):
                window.remove_all()
            with qt_wait_print(dt, "Closing DataLab"):
                window.close_cdl()


if __name__ == "__main__":
    test_remote_client()
