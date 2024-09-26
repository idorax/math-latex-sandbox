#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Query YAML block according to a specified date and print out as a JSON block.
If it is not found, print out an error and exit.
"""

#_DEBUG_#import pysnooper
import sys
import argparse
import yaml
import json


__version__ = '1.0.1'


#_DEBUG_#@pysnooper.snoop(prefix='[ DEBUG ] 03:text2obj> ')
def text2obj(text):
    """
    Convert YAML to Python object.

    :param text: YAML block.

    :returns: Python object.
    """
    text = text.replace(u'\x8f', '')
    obj = yaml.safe_load(text)
    return obj


#_DEBUG_#@pysnooper.snoop(prefix='[ DEBUG ] 02:get_all_text> ')
def get_all_text(yaml_files):
    """
    Get all text of a list of YAML files.

    :param yaml_files: A list of YAML files.

    :returns: A string having all text of the YAML files.
    """
    all_text = ""
    for yaml_file in set(yaml_files):
        text = None
        with open(yaml_file, 'r') as file_handler:
            text = ''.join(file_handler.readlines())
            if text is not None:
                all_text += text
    return all_text


#_DEBUG_#@pysnooper.snoop(prefix='[ DEBUG ] 01:main> ')
def main(argc, argv):
    #
    # XXX: For more info on `argparse`, please refer to:
    #      1) argparse::usage:   https://zhuanlan.zhihu.com/p/657689302
    #      2) argparse::version: https://blog.51cto.com/u_16175470/8009482
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', action='store_true', default=False, help='show all records')
    parser.add_argument('-d', '--date', type=int, default=19700101, help='specify date to query')
    parser.add_argument('-f', '--file', dest='yaml_files', required=True, action='append', type=str, help='YAML files')
    parser.add_argument('-v', '--verbose', action='store_true', help='output verbosity')
    parser.add_argument('-V', '--version', action='version', version=__version__)
    args = parser.parse_args()

    if args.verbose:
        print(f">>> args: {args}", file=sys.stderr)

    text = get_all_text(args.yaml_files)
    obj = text2obj(text)

    if args.verbose:
        out = yaml.dump(obj, default_flow_style=False, indent=4)
        print(f">>> {'#' * 120}", file=sys.stderr)
        out_list = out.split('\n')
        out_str = '\n>>> '.join(out_list)
        print(f">>> {out_str}", file=sys.stderr)
        print(f">>> {'#' * 120}", file=sys.stderr)

    obj_target = obj if args.all else obj.get(args.date, None)
    if obj_target is None:
        if args.date is not None:
            print(f"Oops, not found according to keyword {args.date}.", file=sys.stderr)
        else:
            print(f"Oops, faild to load {' '.join(args.yaml_files)}", file=sys.stderr)
        return -1

    out = json.dumps(obj_target, indent=4)
    print(out)

    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
