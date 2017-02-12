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

### Change compare tool
At the moment is [meld](http://meldmerge.org/) the hard-coded tool that is spawn to do the compare. If you prefer another compare tool, then change the following line in ""nautilus-file-compare.py"":

    diff_rule = "meld {0} {1}"
  
Leave {0} and {1} in the line, because they will be replaced by the source-filename & target-filename.
For example:
  
     diff_rule = "kdiff3 {0} {1}"
