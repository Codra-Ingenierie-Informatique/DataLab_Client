# DataLab Simple Client Releases #

## Version 0.10.0 ##

DataLab Simple Client is fully compatible with **DataLab 0.14.2** and above.
With older versions of the DataLab server, some features may not work.

💥 Changes:

* Remote API (`SimpleRemoteProxy`):
  * Merged `open_object` and `open_objects` methods to `load_from_files`

## Version 0.9.1 ##

DataLab Simple Client is fully compatible with **DataLab 0.14.0** and above.
With older versions of the DataLab server, some features may not work.

💥 Changes:

* Remote API (`SimpleRemoteProxy`):
  * Changed constructor signature to accept `autoconnect` as argument,
    defaulting to `True`
  * Thus, when creating a `SimpleRemoteProxy` instance, the connection to the
    server is now established automatically by default (i.e. same behavior as
    DataLab's `cdl.proxy.RemoteProxy` class)
  * `get_object_titles` method now accepts "macro" as panel name and returns
    the list of macro titles
  * New `run_macro`, `stop_macro` and `import_macro_from_file` methods

## Version 0.8.1 ##

DataLab Simple Client is fully compatible with **DataLab 0.11.0** and above.
With older versions of the DataLab server, some features may not work.

💥 Changes:

* Added `keep_roi` argument to `SimpleRemoteProxy.delete_metadata` method

🛠️ Bug fixes:

* Fixed `SimpleRemoteProxy.get_object` method when there is no object to return
  (`None` is returned instead of an exception)

## Version 0.7.0 ##

DataLab Simple Client is fully compatible with **DataLab 0.10.0** and above.
With older versions of the DataLab server, some features may not work.

💥 Changes:

* Added `toggle_auto_refresh` method to `SimpleRemoteProxy`
* Added `context_no_refresh` method to `SimpleRemoteProxy` (context manager)
* Added `toggle_show_titles` method to `SimpleRemoteProxy`
* Remote client is now checking the server version and shows a warning message if
  the server version may not be fully compatible with the client version.

## Version 0.6.0 ##

💥 Changes:

* Remote API (`SimpleRemoteProxy`):
  * Added `get_group_titles_with_object_infos` method

* New `widgets` module:
  * New `GetObjectDialog` class:
    * Ready-to-use dialog box to retrieve an object from a DataLab server
    * `from cdlclient.widgets import GetObjectDialog`
    * See example in `cdlclient/tests/get_object_dialog.py`

## Version 0.5.0 ##

💥 Changes:

* Remote API (`SimpleRemoteProxy`):
  * Added `is_connected` method

* New `widgets` module:
  * New `ConnectionDialog` class:
    * Ready-to-use dialog box to connect to a DataLab server
    * `from cdlclient.widgets import ConnectionDialog`
    * See example in `cdlclient/tests/connect_dialog.py`

## Version 0.4.0 ##

💥 Changes:

* Remote API (`SimpleRemoteProxy`):
  * Added dict-like interface (e.g. `proxy['obj123']`)
  * Renamed `switch_to_panel` method to `set_current_panel` (compatibility with DataLab 0.9)
  * Added `get_current_panel` method
  * Changed `select_groups` first argument `selection` (compatibility with DataLab 0.9)
  * Changed `select_objects` arguments (compatibility with DataLab 0.9)

## Version 0.3.0 ##

💥 Changes:

* Remote API (`SimpleRemoteProxy`):
  * `get_object` method now takes either object number, UUID or a title
  * `get_object_shapes` method now takes either object number, UUID or a title
  * Removed deprecated `get_object_from_uuid` and `get_object_from_title` methods

* Simplified DataLab object model:
  * Added `SignalObj.uuid` item
  * Added `ImageObj.uuid` item

## Version 0.2.0 ##

💥 Changes:

* Remote API (`SimpleRemoteProxy`):
  * New `raise_window` method
  * New `get_object_shapes` method
  * New `get_object` method
  * New `get_object_from_uuid` method
  * New `get_object_from_title` method

* Added simplified DataLab object model:
  * `simplemodel.SignalObj` class
  * `simplemodel.ImageObj` class

## Version 0.1.0 ##

First release of the DataLab Simple Client.
