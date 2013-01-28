======
enplot
======

enplot: a one-line plot command

enplot use python and matplotlib to provide a simple command-line interface
that be used to quickly plot data in CSV and related formats. The focus of
enplot is not publication quanlity plots, but rather quick and easy presentation
of numerical data. 


Usage
=====

    $ enplot --help
    usage: enplot [-h] [-t TITLE] [-o OUTPUT_FILE] [-f OUTPUT_FORMAT] [-x X]
                  [-y Y] [-z Z] [-m] [-T] [-X X_LABEL] [-Y Y_LABEL] [-Z Z_LABEL]
                  [-l LEGENDS] [-s] [-q] [-d] [-v VIEW] [-c]
                  datafile [datafile ...]

    positional arguments:
      datafile              a data file in a CSV-like format

    optional arguments:
      -h, --help            show this help message and exit
      -t TITLE, --title TITLE
                            plot title
      -o OUTPUT_FILE, --output-file OUTPUT_FILE
                            file name for output
      -f OUTPUT_FORMAT, --output-format OUTPUT_FORMAT
                            file format for output
      -x X                  column index in the data file for use as X variable
      -y Y                  comma-separated list of column index in the data file
                            for use as Y variables
      -z Z                  comma-separated list of column index in the data file
                            for use as Y variables
      -m, --matrix-form     data in matrix form
      -T, --matrix-transpose
                            transpose data in matrix form
      -X X_LABEL, --x-label X_LABEL
                            label for use on X axis
      -Y Y_LABEL, --y-label Y_LABEL
                            label for use on Y axis
      -Z Z_LABEL, --z-label Z_LABEL
                            label for use on Z axis
      -l LEGENDS, --legends LEGENDS
                            comma-separated list of legends
      -s, --sort            sort the data by the X-axis data points
      -q, --quiet           do not display plot window
      -d, --debug           activate debug printouts
      -v VIEW, --view VIEW  view perspective (top or 3d)
      -c, --colorbar        Show colorbar


Examples
========

Line plots
----------

Plot lines corresponding to column data:

    $ head -n 4 tests/example-data0.dat 
    # Generated by QuTiP: 1000x3 real matrix in decimal format [',' separated values].
    0.0000000000,0.0000000000,1.0000000000
    0.0125125125,0.0217573882,0.9773997992
    0.0250250250,0.0747018995,0.9246287209

    $ enplot -x 0 -y 1,2 -X "time" -Y "Probabilities" -o tests/example-data0.png tests/example-data0.dat

![example-data0](https://raw.github.com/jrjohansson/enplot/master/tests/example-data0.png)

Plot 3D data
------------

    enplot -x 0 -y 1 -z 2 -c -v 3d -o tests/example-data1a.png tests/example-data1.dat

![example-data1a](https://raw.github.com/jrjohansson/enplot/master/tests/example-data1a.png)


Plot 3D data as colormap
------------------------

    enplot -x 0 -y 1 -z 2 -c -o tests/example-data1b.png tests/example-data1.dat

![example-data1b](https://raw.github.com/jrjohansson/enplot/master/tests/example-data1b.png)


Plot matrix data as colormap
----------------------------

    $ head -3 tests/example-data2.dat 
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    
    $ enplot -m -c -o tests/example-data2.png tests/example-data2.dat

![example-data2](https://raw.github.com/jrjohansson/enplot/master/tests/example-data2.png)

