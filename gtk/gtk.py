import argparse
import os
import sys

##################################################
# Top level parser
##################################################
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
##################################################
# Init release command
##################################################
init_release_parser = subparsers.add_parser("init-release")
init_release_parser_group = init_release_parser.add_argument_group('init_release_parser_group')
init_release_parser_group.add_argument('-g',
                                       action='store',
                                       required=True)
init_release_parser_group.add_argument('-r',
                                       action='store',
                                       required=True)
##################################################
# Publish release command
##################################################
publish_release_parser = subparsers.add_parser("publish-release")
publish_release_parser_group = publish_release_parser.add_argument_group('publish_release_parser')
publish_release_parser_group.add_argument('-g',
                                          action='store',
                                          required=True)
publish_release_parser_group.add_argument('-r',
                                          action='store',
                                          required=True)
##################################################
# Finish release command
##################################################
finish_release_parser = subparsers.add_parser("finish-release")
finish_release_parser_group = finish_release_parser.add_argument_group('publish_release_parser')
finish_release_parser_group.add_argument('-g',
                                         action='store',
                                         required=True)
finish_release_parser_group.add_argument('-r',
                                         action='store',
                                         required=True)

args = parser.parse_args()
print(vars(args))
