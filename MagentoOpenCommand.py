import sublime, sublime_plugin
import os.path
import re

class MagentoOpenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		if(len(sels) == 1):
			text = self.view.substr(sels[0])
			if(len(text)):
				self.open(self.get_file(text))

	def get_file(self, text):
		return text.strip().replace('_', '/') + '.php'

	def open(self, filePath):
		rootDirectories = ['/app/code/core/', '/app/code/community/', '/app/code/local/', '/lib/']

		for folder in sublime.active_window().folders():
			for root in rootDirectories:
				if os.path.isfile(folder+root+filePath):
					sublime.active_window().open_file(folder+root+filePath)
					return

	def is_visible(self):
		value = False
		for region in self.view.sel():
			selText = self.view.substr(region)
			if len(selText) == 0:
				continue
			if self.view.score_selector(region.a, 'source.php') <= 0:
				return False
			else:
				value = value or (re.match("([A-Z][a-zA-Z0-9]+_?)+", self.view.substr(region)) > 0)
		return value




