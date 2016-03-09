# Tkinter Notes

### Terms and Concepts

* Widget: Elements the make up the GUI
  * Invisible container widgets (e.g. Frame)
  * Visible interactive widgets (e.g. Button)
* Layout: Organizing widgets on GUI to specific positions
* Event: Objects that are generated for user or system actions, such as mouse click

### Widgets

Tkinter provides 18 built-in widget implementations.

* Button
* Canvas
* Entry
* Scrollbar
* Frame

### Hello Tkinter

Code: [00_hello_tkinter.py](00_hello_tkinter.py)

* Initialization: Create Tk root which is a window
  * One root per application
  * It should be created before anything else

### Button Widget

Code: [01_button_widget.py](01_button_widget.py)

* Used for adding buttons in a Python application
* Can display text or images
* You can attach a function or a method to a button which is called automatically when the button is clicked

### Checkbutton Widget

Code: [02_checkbutton_widget.py](02_checkbutton_widget.py)

* Provides a checkbox with a text label
* Has two states: on and off
* Denotes a boolean property (True and False)

### Label Widget

Code: [03_label_widget.py](03_label_widget.py)

* Used to display text tor images
* No user interaction

### ListBox Widget

Code: [04_listbox_widget.py](04_listbox_widget.py)

* Displays a list of entries
* Allows selecting one or multiple items
