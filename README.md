# pymegablast - Automated megablast #

`pymegablast` is a python wrapper for *megablast*, allowing multiple tasks
required by the PGx center.

`pymegablast` should work on MacOS, even though it hasn't been fully tested for
full compatibility.


## Requirements ##

Here are the requirements that must be installed before `pymegablast`:

* [Python](http://python.org/) version 2.7, but not 3.0
* [biopython](http://biopython.org/wiki/Main_Page) version 1.62 or latest


## Usage ##

```console
$ pymegablast.py --help
usage: pymegablast.py [-h] [-v] -i FILE [-w] [-wl INT] [-d PATH] [-W INT]
                      [-s INT] [-o DIR]

Runs pymegablast (version 0.3).

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

Input Files:
  -i FILE, --input FILE
                        The file containing the sequence(s).

Sequence(s) Pre-Processing:
  -w, --window          If set to True, the sequence(s) will be split by a
                        window of X characters (see -wl/--window-length
                        option). [Default: False]
  -wl INT, --window-length INT
                        The window size (if -w/--window option is used).
                        [Default: 20]

MegaBlast Options:
  -d PATH, --database PATH
                        The database to use for the search. [Default:
                        /mnt/isi/reference/Genome_Build_37/chromosomes]
  -W INT, --word-size INT
                        The word size for MegaBlast. [Default: 10]
  -s INT, --minimal-hit-score INT
                        The minimal hit score for MegaBlast. [Default: 17]

Output Files:
  -o DIR, --output-dir DIR
                        The name of the output directory. [Default:
                        megablast.2015-01-23_11.36.35]
```

