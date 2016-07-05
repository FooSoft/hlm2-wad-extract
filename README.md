# HLM2-Wad-Extract #

This tool extracts binary asset data (including the soundtrack in OGG format) packaged with [Hotline Miami 2: Wrong
Humber](https://en.wikipedia.org/wiki/Hotline_Miami_2:_Wrong_Number).

## Dependencies ##

* [Python 2.7](https://www.python.org/download/releases/2.7/)

## Usage ##

This application extracts asset data from the WAD files that are shipped with the game (currently
`hlm2_data_desktop.wad` and `hlm2_patch_desktop.wad`). These files can be found in the game install path; on Linux, this
is the `~/.steam/steam/steamapps/common/Hotline Miami 2` directory.

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

## License ##

MIT
