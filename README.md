# HLM2-Wad-Extract #

This tool extracts binary asset data (including the soundtrack in OGG format) packaged with the game [Hotline Miami 2:
Wrong Humber](https://en.wikipedia.org/wiki/Hotline_Miami_2:_Wrong_Number).

## Requirements ##

* [Python 2.7](https://www.python.org/download/releases/2.7/)

## Usage ##

Execute `extract.py` script with the `-h` option for a description of available options:

```
usage: parse.py [-h] [--pattern PATTERN] [--output DIRECTORY]
                filename [filename ...]

Extract assets from Hotline Miami 2 WAD files

positional arguments:
  filename            WAD files to extract

optional arguments:
  -h, --help          show this help message and exit
  --pattern PATTERN   asset file filter pattern (ex: *.ogg)
  --output DIRECTORY  output directory for asset files
```

For example, in order to extract the game's music files only, you could execute the following command:

```
$ ./parse.py --pattern "*.ogg" hlm2_data_desktop.wad
```

The relevant WAD files can be found in the `~/.steam/steam/steamapps/common/Hotline Miami 2` directory on Linux.

## License ##

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
