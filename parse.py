#!/usr/bin/env python

# Copyright (c) 2015 Alex Yatskov <alex@foosoft.net>
# Author: Alex Yatskov <alex@foosoft.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import argparse
import fnmatch
import os
import struct


class Asset:
    def __init__(self, filename, offset, length):
        self.filename = filename
        self.offset = offset
        self.length = length

    def extract(self, wad_data, wad_offset, extract_dir):
        output_path = os.path.join(extract_dir, self.filename)
        output_dir = os.path.dirname(output_path)

        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        with open(output_path, 'w') as fp:
            absolute_offset = wad_offset + self.offset
            fp.write(wad_data[absolute_offset : absolute_offset + self.length])


def extract(wad_file, extract_dir='.', extract_pattern='*.*'):
    print('Processing WAD file "{}"...'.format(wad_file))
    with open(wad_file, 'r') as fp:
        wad_data = fp.read()

    wad_offset = 0
    asset_count = struct.unpack_from('I', wad_data, wad_offset)[0]
    wad_offset += 4

    asset_list = list()
    for asset_index in xrange(asset_count):
        asset_name_length = struct.unpack_from('I', wad_data, wad_offset)[0]
        wad_offset += 4

        asset_name = struct.unpack_from(str(asset_name_length) + 's', wad_data, wad_offset)[0]
        wad_offset += asset_name_length

        asset_length, asset_offset = struct.unpack_from('2Q', wad_data, wad_offset)
        wad_offset += 16

        asset_list.append(Asset(asset_name, asset_offset, asset_length))

    asset_list = filter(lambda asset: fnmatch.fnmatch(asset.filename, extract_pattern), asset_list)

    for index, asset in enumerate(asset_list):
        print('\t({} / {}) Extracting asset file "{}"...'.format(index+1, len(asset_list), asset.filename))
        asset.extract(wad_data, wad_offset, extract_dir)

    print('Operation complete!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract assets from Hotline Miami 2 WAD files')
    parser.add_argument('filenames', metavar='filename', nargs='+', help='WAD files to extract')
    parser.add_argument('--pattern', dest='pattern', default='*.*', help='asset file filter pattern (ex: *.ogg)')
    parser.add_argument('--output', dest='directory', default='.', help='output directory for asset files')

    args = parser.parse_args()
    for filename in args.filenames:
        extract(filename, args.directory, args.pattern)
