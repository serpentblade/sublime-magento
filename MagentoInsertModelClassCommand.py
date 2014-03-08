import sublime, sublime_plugin
import os.path
import os
import textwrap

class MagentoInsertModelClassCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        rootDirectories = ['/app/code/core/', '/app/code/community/', '/app/code/local/', '/lib/']

        file_name = self.view.file_name();

        for folder in sublime.active_window().folders():
            for root in rootDirectories:
                basepath = folder+root
                if file_name.startswith(basepath):
                    path = file_name[len(basepath):]
                    class_name = self.get_model_code(path)
                    self.view.run_command('insertAndDecodeCharacters', { 'characters': class_name })

    def get_class_name(self, file):
        class_name = file.replace(os.sep, '_')
        if class_name.endswith('.php'):
            class_name = class_name[:-4]
        return class_name

    def get_model_code(self, file):
        model_name = self.get_class_name(file)
        r = """
            <?php
            class %(class)s extends Mage_Core_Model_Abstract {
            public function() {
                    $this->_init('');
                }
            } """ % {"class" : model_name}
        return r