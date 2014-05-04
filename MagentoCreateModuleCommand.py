import sublime, sublime_plugin
import os
import re

class MagentoCreateModuleCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("New Module:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        regex = re.compile("([a-zA-Z0-9]*)_([a-zA-Z0-9]*)")
        folder_path =  self.window.active_view().window().folders();
        if (regex.match(text) != None):
            text_split = text.split("_");
            namespace = text_split[0];
            moduleName = text_split[1];
            path = os.path.join(folder_path[0], 'app', 'code', 'local', namespace, moduleName );
            etc_modules_path = os.path.join(folder_path[0], 'app', 'etc', 'modules', text + ".xml")
            
            # Create folder structure
            os.makedirs(path)
            os.makedirs(os.path.join(path, 'Model'))
            os.makedirs(os.path.join(path, 'Block'))
            os.makedirs(os.path.join(path, 'controllers'))
            os.makedirs(os.path.join(path, 'sql'))

            self.create_config_xml(path, namespace, moduleName)
            self.create_etc_modules_xml(etc_modules_path, namespace, moduleName)

            self.create_helper(path, namespace, moduleName)
        pass

    def create_config_xml(self, path, namespace, moduleName):
        template = """<?xml version="1.0" encoding="UTF-8"?>
<config>
    <modules>
        <{namespace}_{moduleName}>
            <version>0.0.1</version>
        </{namespace}_{moduleName}>
    </modules>
</config>
        """
        data = {"namespace" : namespace,
                "moduleName" : moduleName}
        os.makedirs(os.path.join(path, 'etc'))
        file = open(os.path.join(path, 'etc', 'config.xml'), 'w+')
        file.write(template.format(**data))


    def create_etc_modules_xml(self, path, namespace, moduleName):
        template = """<?xml version="1.0" encoding="UTF-8"?>
<config>
    <modules>
        <{namespace}_{moduleName}>
            <active>true</active>
            <codePool>local</codePool>
            <depends><!-- NO DEPENDENCIES --></depends>
        </{namespace}_{moduleName}>
    </modules>
</config>
        """
        data = {"namespace" : namespace,
                "moduleName" : moduleName}
        file = open(path, 'w+')
        file.write(template.format(**data))        
        pass

    def create_helper(self, path, namespace, moduleName):
        template = """<?php

class {namespace}_{moduleName}_Helper_Data extends Mage_Core_Helper_Abstract
{{
    
}}
"""
        data = {"namespace" : namespace,
                "moduleName" : moduleName}
        os.makedirs(os.path.join(path, 'Helper'))
        file = open(os.path.join(path, 'Helper', 'Data.php'), 'w+')
        file.write(template.format(**data))        
        pass