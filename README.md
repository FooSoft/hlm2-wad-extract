# HLM2-Wad-Extract #

This application is a tool to extract the asset data used in the newly released [Hotline Miami 2: Wrong
Humber](https://en.wikipedia.org/wiki/Hotline_Miami_2:_Wrong_Number) game. Although it was developed on Linux to run on
Linux, it should work on other platforms without problems.

## Motivation ##

After purchasing and thoroughly enjoying this title, I thought that I would like to listen to the excellent soundtrack
while coding. I was slightly disappointed when I discovered that the music data was not simply included in the install
directory as it was in the preceding game.  Seeing as I had some free time, I decided to try to fish out the music OGG
files myself out of the accompanying game WAD pack files. The file format turned out to be really simple and easy to
understand, so I wrote a small Python utility to extract some or all of the game data.

## Usage ##

This script makes it trivial to extract game data from the WAD files shipped with the game (currently
`hlm2_data_desktop.wad` and `hlm2_patch_desktop.wad`). These files can be found in the game install directory; on Linux
this is under `~/.steam/steam/steamapps/common/Hotline Miami 2` (probably in a similar location on other platforms).

Assuming that you have [Python 2.7](https://www.python.org/download/releases/2.7/) installed, you can execute the
`extract.py` script with the `-h` option for a description of available options:

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

While I expect this utility to be trivial for all to use, let me know if you encounter any difficulties or unexpected
behavior.

## License ##

MIT
