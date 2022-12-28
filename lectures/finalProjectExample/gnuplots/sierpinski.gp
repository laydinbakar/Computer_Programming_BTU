#/usr/bin/gnuplot

set terminal pdfcairo font 'Times,14' size 4.5in,4.5in
set output 'sierpinski.pdf'

#unset border
#unset xtics
#unset ytics
#unset key

plot 'T.txt' using 1:2 ps 1 lw 1 lt -1 w lp ,\
#     'KSRotP.txt' using 1:2 ps 1 lw 2 lt 1 w lp ,\
#     'KSRotPP.txt' using 1:2 ps 1 lw 1 lt 2 w lp


