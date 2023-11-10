Overview
========

DataLab may be controlled remotely using the `XML-RPC`_ protocol which is
natively supported by Python (and many other languages). Remote controlling
allows to access DataLab main features from a separate process.

From an IDE
^^^^^^^^^^^

DataLab may be controlled remotely from an IDE (e.g. `Spyder`_ or any other
IDE, or even a Jupyter Notebook) that runs a Python script. It allows to
connect to a running DataLab instance, adds a signal and an image, and then
runs calculations. This feature is exposed by the `cdlclient.SimpleRemoteProxy`
class.

From a third-party application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DataLab may also be controlled remotely from a third-party application, for the
same purpose.

If the third-party application is written in Python 3, it may directly use
:py:class:`cdlclient.SimpleRemoteProxy` as mentioned above. From another language,
it is also achievable, but it requires to implement a XML-RPC client in this
language using the same methods of proxy server as in the
:py:class:`cdlclient.SimpleRemoteProxy` class.

Data (signals and images) may also be exchanged between DataLab and the remote
client application, in both directions.

The remote client application may be run on the same computer as DataLab or on
different computer. In the latter case, the remote client application must
know the IP address of the computer running DataLab.

The remote client application may be run before or after DataLab. In the latter
case, the remote client application must try to connect to DataLab until it
succeeds.

Supported features
^^^^^^^^^^^^^^^^^^

Supported features are the following:

  - Switch to signal or image panel
  - Remove all signals and images
  - Save current session to a HDF5 file
  - Open HDF5 files into current session
  - Browse HDF5 file
  - Open a signal or an image from file
  - Add a signal
  - Add an image
  - Get object list
  - Run calculation with parameters

Some examples are provided to help implementing such a communication
between your application and DataLab:

  - See module: ``cdlclient.tests.remoteclient_app``
  - See module: ``cdlclient.tests.remoteclient_unit``

.. figure:: /images/shots/remote_control_test.png

    Screenshot of remote client application test (``cdlclient.tests.remoteclient_app``)

Additional features
^^^^^^^^^^^^^^^^^^^

For simple remote controlling, :py:class:`cdlclient.SimpleRemoteProxy` may be
used. For more advanced remote controlling, the `cdl.RemoteCDLProxy` class
provided by the DataLab (``cdl``) package may be used.

See DataLab documentation for more details about the ``cdl.RemoteCDLProxy``
class (on the section "Remote control").

.. _XML-RPC: https://docs.python.org/3/library/xmlrpc.html

.. _Spyder: https://www.spyder-ide.org/
