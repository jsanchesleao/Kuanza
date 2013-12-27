#!/usr/bin/env python

import os
from lib.kuanzaproto import KuanzaProto
import lib.protoservice as protoservice

def main():
    for name in protoservice.getInstalledPrototypeNames():
        print(name)


if __name__ == '__main__':
    main()