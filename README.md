
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

MIT
