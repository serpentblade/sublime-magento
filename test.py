def fun():
    r = """<?php
    class %(class)s extends Mage_Core_Model_Abstract {
        public function() {
            $this->_init('');
        }
    } """ % {"class" : "stuff"}
    return r

print fun()