#!/usr/bin/python

import os
import sys
import collections
import xml.parsers.expat


class XMLToolsAnalizer(object):
    def __init__(self, name):
        self._name = os.path.abspath(name)
        self._p = None
        self._cnt = collections.Counter()
        self._path = []

    # 3 handler functions
    def start_element(self, name, attrs):
        self._path.append(name)
        #
        name = ".".join(self._path)
        self._cnt[name] += 1
        #
        #print 'Start element:', name, attrs

    def end_element(self, name):
        top = self._path.pop()
        #print 'End element:', name

    def char_data(self, data):
        print('Character data: {data!r}'.format(data=data))

    def run(self):
        # Step 1. Create parser
        self._p = xml.parsers.expat.ParserCreate()
        self._p.StartElementHandler = self.start_element
        self._p.EndElementHandler = self.end_element
        #self._p.CharacterDataHandler = self.char_data
        # Step 2. Reading source information
        with open(self._name, "rb") as stream:
            for block in stream:
                self._p.Parse(block, 0)
            self._p.Parse("", 1)
            stream.close()
        # Step 3. Show report
        for (name, value) in self._cnt.items():
            print("| {name:40s} | {value:8d} |".format(name=name, value=value))


def main():
    argc, argv = len(sys.argv), sys.argv
    name = None
    if argc > 1:
        if argv[1] == "--help":
            print("Usage: {programm} [name]".format(programm=argv[0]))
            return 0
        else:
            name = argv[1]

    if name is not None:
        xml_analizer = XMLToolsAnalizer(name=name)
        xml_analizer.run()
    else:
        print("Require argument. You must usage --help to inforamtion.")


if __name__ == "__main__":
    sys.exit(main())
