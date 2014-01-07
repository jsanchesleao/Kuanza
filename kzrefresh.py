#!/usr/bin/env python

import lib.kuanzarefresh
import optparse

def main():
    parser = optparse.OptionParser()
    parser.add_option('--debug', '-d', action='store_true', default=False)
    options, arguments = parser.parse_args()

    try:
        lib.kuanzarefresh.refreshPackageData()
        print('Package data reloaded.')
    except Exception as e:
        print('Error reloading package data.')
        if options.debug:
            raise e
        else:
            print('Try rerun it with --debug flag for more detailed output.')


if __name__ == '__main__':
    main()