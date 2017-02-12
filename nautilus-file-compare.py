from gi.repository import Nautilus, GObject, Gtk
import subprocess
import os

source_file = ""
diff_rule = "meld {0} {1}"
home_folder = os.getenv("HOME")

def execute_sh( script, directory ):
    """ Execute a shell command """
    #logging.debug('Execute: {0}'.format(script))
    p = subprocess.Popen( script, shell=True, cwd=directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    #logging.debug('-   stderr: {0}'.format(stderr))
    #logging.debug('-   stdout: {0}'.format(stdout))

    return stderr

def showMessageDialog(text, secondText):
    md = Gtk.MessageDialog(None,
          0, Gtk.MessageType.ERROR,
          Gtk.ButtonsType.OK, text)
    md.format_secondary_text(secondText)
    md.run()
    md.destroy()

class FileCompareExtension(GObject.GObject, Nautilus.MenuProvider):

    def __init__(self):
        pass

    def menu_select_source_cb(self, menu, file):
        global source_file
        source_file = file

    def menu_select_dest_cb(self, menu, file):
        global source_file
        diff_command = diff_rule.format(source_file.get_uri(), file.get_uri())
        #showMessageDialog(diff_command)
        errorLogging =  execute_sh( diff_command, home_folder )
        if errorLogging <> "":
            compareString =  "Failed to compare {0} with {1}".format(source_file.get_name(), file.get_name())
            secondString = "Due: {0}".format(errorLogging)
            showMessageDialog(compareString, secondString)

        source_file = ""

    def get_file_items(self, window, files):
        global source_file
        if len(files) != 1:
            return

        file = files[0]
        itemSource = None
        itemDestination = None

        if source_file == "":
            itemSource = Nautilus.MenuItem(
                name="FileCompareExtension::Compare_Select_Source",
                label="Select source for compare",
                sensitive=True,
                tip="Select %s as source" % file.get_name()
            )
            itemSource.connect('activate', self.menu_select_source_cb, file)

            itemDestination = Nautilus.MenuItem(
                name="FileCompareExtension::Compare_Select_Destination",
                label="Select destination for compare",
                sensitive=False,
                tip="Select source first"
            )
            itemDestination.connect('activate', self.menu_select_dest_cb, file)
        else:
            itemSource = Nautilus.MenuItem(
                name="FileCompareExtension::Compare_Select_Source",
                label="Select source for compare",
                sensitive=True,
                tip="Select %s as source" % file.get_name()
            )
            itemSource.connect('activate', self.menu_select_source_cb, file)

            itemDestination = Nautilus.MenuItem(
                name="FileCompareExtension::Compare_Select_Destination",
                label="Select destination for compare",
                sensitive=True,
                tip="Select %s as destination" % file.get_name()
            )
            itemDestination.connect('activate', self.menu_select_dest_cb, file)

        return [itemSource, itemDestination]

