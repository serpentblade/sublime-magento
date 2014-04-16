# DISCLAIMER:
#
# Parts of this code were taken from the "Expand Selection to Quotes" plugin at
# https://github.com/kek/sublime-expand-selection-to-quotes
#
# Expands selection to quotes and opens 'GO TO' prompt with the selection in it already

import sublime, sublime_plugin
import os
import re


import re



class MagentoOpenFromMagentoPathCommand(sublime_plugin.WindowCommand):
    def run(self):

        d_quotes = list(map(lambda x: x.begin(), self.window.active_view().find_all('"')))
        s_quotes = list(map(lambda x: x.begin(), self.window.active_view().find_all("'")))

        for sel in self.window.active_view().sel():
            def search_for_quotes(q_type, quotes):
                q_size, before, after = False, False, False

                if len(quotes) - self.window.active_view().substr(sel).count('"') >= 2:
                    all_before = list(filter(lambda x: x < sel.begin(), quotes))
                    all_after = list(filter(lambda x: x >= sel.end(), quotes))

                    if all_before: before = all_before[-1]
                    if all_after: after = all_after[0]

                    if all_before and all_after: q_size = after - before

                return q_size, before, after

            d_size, d_before, d_after = search_for_quotes('"', d_quotes)
            s_size, s_before, s_after = search_for_quotes("'", s_quotes)

            def replace_region(start, end):
                if sel.size() < end-start-2:
                    start += 1; end -= 1
                self.window.active_view().sel().subtract(sel)
                self.window.active_view().sel().add(sublime.Region(start, end))

            if d_size and (not s_size or d_size < s_size):
                replace_region(d_before, d_after+1)
            elif s_size and (not d_size or s_size < d_size):
                replace_region(s_before, s_after+1)

        text = self.window.active_view().substr(self.window.active_view().sel()[0]).replace("_", " ").replace("/", " ")
        # line = self.window.active_view().line(self.window.active_view().substr(self.window.active_view().sel()[0]))
        # modelRegex = re.compile(r'Model')
        # helperRegex = re.compile(r'helper')
        # if modelRegex.search(line) is not None:
        #   print 'matched'
        self.window.run_command("show_overlay", {"overlay": "goto", "text": text, "show_files": "true"})

