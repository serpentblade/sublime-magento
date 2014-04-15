import sublime, sublime_plugin
import os
import re

class MagentoOpenFromPathCommand(sublime_plugin.WindowCommand):
    def run(self):
        text = self.window.active_view().substr(self.window.active_view().sel()[0])
        self.window.run_command("show_overlay", {"overlay": "goto", "text": text, "show_files": "true"})



