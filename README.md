##sublime-magento
Sublime text 2 plugin for easier magento development. It contains code snippets for faster module creation (code within standard module files - mostly XML).

**NOTE** - this package contains lot of trash files. It is under development, albeit very sloppy one at the time. It also has few undocumented commands.

**Commands**

* **InsertClass command** (original work @serpentblade)

    Used to insert class name -> works for all classes except controllers (unless you are willing to delete 'controllers' word)
```
    { "keys": ["ctrl+i"], "command": "magento_insert_class"}
```

* **InsertModelClass command** (original work @serpentblade)

    Used to insert model class name with a boilerplate function
```
    { "keys": ["ctrl+shift+m"], "command": "magento_insert_model_class"}
```

* **OpenFromMagentoPath command**

    On keypress fills the "goto" panel with the text between the nearest quotation marks (single or double). Useful for file paths. Also useful for 'magento-like' paths like ('core/input_filter_maliciousCode') where the command removes the '_' and '/' characters and also populates the "goto" panel.
```
    { "keys": ["alt+shift+p"], "command": "magento_open_from_magento_path"}
```

* **CreateModule command**

    On keypress opens up a dialog for new module name. Name should be entered in the format of "Namespace_ModuleName". Newly created module will be located in the local/Namespace/ModuleName, and it will have few things created already (Model, Helper, Helper/Data.php, Block, controllers, etc, etc/config.xml, controllers), and also will be registered in "/app/etc/Modules/Namespace_Modulename.xml".
    New module will have the default version of 0.0.1.
```
    { "keys": ["alt+shift+m"], "command": "magento_create_module"}
```

**Snippets**
```php
    // (original work @serpentblade)
    model     => Mage::getModel('module/model');
    helper    => Mage::helper('module/helper');
    resource  => Mage::getResourceModel('module/model');
    singleton => Mage::getSingleton('module/model');

```

**mag-modreg**
 * **magento module registration** in app/etc/modules/Namespace_Modulename
 * creates the following snippet with your module name already in place, and cursor on codePool
```xml
<config>
    <modules>
        <Namespace_Modulename>
            <active>true</active>
            <codePool></codePool>
        </Namespace_Modulename>
    </modules>
</config>
```

**mag-confinit**
 * **magento module configuration initialization ** in app/code/[codePool]/Namespace/Modulename/etc/config.xml
 * creates the following snippet with the cursor placed to insert your Namespace_Modulename, autopopulating the closing tag. Tabbing moves you to version.
```xml
<config>
    <modules>
        <>
            <version></version>
        </>
    </modules>
</config>
```

**mag-frontend**
 * **magento module configuration frontend ** in app/code/[codePool]/Namespace/Modulename/etc/config.xml
 * creates the following snippet with the cursor placed to insert your router tag, autopopulating the closing tag. Tabbing moves you to module.
```xml
<frontend>
    <routers>
        <>
            <use>standard</use>
            <args>
                <module></module>
                <frontName></frontName>
            </args>
        </>
    </routers>
</frontend>
```

**mag-modinit**
 * **magento module configuration of models, helpers and blocks ** in app/code/[codePool]/Namespace/Modulename/etc/config.xml
 * Extends the **mag-confinit** adding few new things
 * creates the following snippet with the cursor placed to insert your module name. When you insert it, everything else is autopopulated. Tabbing moves you to version tag.
```xml
<config>
    <modules>
        <>
            <version></version>
        </>
    </modules>
    <global>
        <models>
            <>
                <class>_Model</class>
            </>
        </models>
        <helpers>
           <>
                <class>_Helper</class>
            </>
        </helpers>
        <blocks>
            <>
                <class>_Block</class>
            </>
        </blocks>
    </global>
</config>
```
**mag-mod-admin**
* creates admin routers xml code
```xml
<admin>
    <routers>
        <adminhtml>
            <use>admin</use>
            <args>
                <modules>
                    < before="Mage_Adminhtml">_Adminhtml</>
                </modules>
            </args>
        </adminhtml>
    </routers>
</admin>
```
