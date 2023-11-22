# DataLab Simple Client Releases #

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
