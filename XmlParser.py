# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET

class XmlParser:
    def __init__(self, _xmlFilePath):
        self._xml_file = _xmlFilePath
        self._parser = ET.parse(self._xml_file)
        self._root = self._parser.getroot()

    @property
    def root(self):
        return self._root

if __name__ == '__main__':
    obj = XmlParser('food_menu.xml')
    print(obj.root.keys())
    print(obj.root.findall('food'))