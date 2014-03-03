import sublime, sublime_plugin
import os.path
import re

class MagentoOpenParentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		text = self.view.substr(sublime.Region(0,self.view.size()))
		result = re.search("class\s+?(?:(?:[A-Z][a-zA-Z0-9]+_?)+)\s+?extends\s+?((?:[A-Z][a-zA-Z0-9]+_?)+)", text, re.M | re.U)

		if result != None:
			parentClass = result.group(1)

			if len(parentClass):
				self.open(self.get_file(parentClass))

	def get_file(self, text):
		return text.strip().replace('_', '/') + '.php'

	def open(self, filePath):
		rootDirectories = ['/app/code/core/', '/app/code/community/', '/app/code/local/', '/lib/']

		for folder in sublime.active_window().folders():
			for root in rootDirectories:
				print folder+root+filePath
				if os.path.isfile(folder+root+filePath):
					sublime.active_window().open_file(folder+root+filePath)
					return

	def is_visible(self):
		value = False
		for region in self.view.sel():
			if region.empty():
				continue
			if self.view.score_selector(region.a, 'source.php') <= 0:
				return False
			else:
				value = True
		return value or self.view.score_selector(sublime.Region(0, 100).a, 'source.php') > 0




