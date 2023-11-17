# DataLab Simple Client Releases #

## Version 0.3.0 ##

Changes:

* Remote API:
  * `get_object` method now takes either object number, UUID or a title
  * `get_object_shapes` method now takes either object number, UUID or a title
  * Removed deprecated `get_object_from_uuid` and `get_object_from_title` methods

* Simplified DataLab object model:
  * Added `SignalObj.uuid` item
  * Added `ImageObj.uuid` item

## Version 0.2.0 ##

Changes:

* Remote API:
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
