#/usr/bin/gnuplot

set terminal pdfcairo font 'Times,14' size 4.1cm,4.1cm
set output 'sierpinski_points.pdf'

unset border
unset xtics
unset ytics
unset key

plot 'sierpinski_points.txt' using 1:2 pt 7 ps 1 lc rgb "navy blue" w p 
