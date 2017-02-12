# nautilus-file-compare
Comparing files/folders in Gnome Nautilus


## Installation
Make sure nautilus-python is installed. For Fedora f23 or later:

    sudo dnf install nautilus-python

Other distros:

    ?

Than copy nautilus-file-compare.py to folder:
    
    ~/.local/share/nautilus/python/extension

If folder does not exist, just create it.

Make sure the extension is executable:

    chmod 744 ~/.local/share/nautilus/python/extension/nautilus-file-compare.py

Then restart Nautilisu/Files (make sure the process was actually killed). Select a file or folder and right click, now you should see the new option(s).

