#!/bin/sh

pdflatex 05.05.example1.tex
convert -verbose -density 150 -trim 05.05.example1.pdf -quality 100 -flatten -sharpen 0x1.0 05.05.example1.png
rm -rf *.aux *.log *.pdf
mv *.png ../
