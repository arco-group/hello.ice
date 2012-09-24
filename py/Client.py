#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import Ice
Ice.loadSlice('Printer.ice')
import Example


class client (Ice.Application):
    def run(self, argv):
        proxy = self.communicator().stringToProxy(argv[1])
        printer = Example.PrinterPrx.checkedCast(proxy)

        if not printer:
            raise RuntimeError("Invalid proxy")

        printer.write("Hello World!")

        return 0


sys.exit(client().main(sys.argv))
