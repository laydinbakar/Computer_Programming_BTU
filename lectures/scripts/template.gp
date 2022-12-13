#/usr/bin/gnuplot

set terminal pdfcairo font 'Times,14' size 4.5in,3.0in
set output 'population.pdf'

set xrange [1962:2022]
set yrange [20:90]
set xlabel 'Year'
set ylabel 'Population in millions'
set xtics autofreq 1962,10

set grid xtics lt -1 lw 0.2 lc rgb 'gray'

set grid xtics mxtics
set grid ytics mytics
set mytics 2
set mxtics 5
set grid lw 1 lt -1 lc rgb 'dark-gray', lw 0.05 lt -1 lc rgb 'light-gray'

set border lw 1.5 

set key reverse below Left spacing 2

plot 'population.txt' using 1:($2/1000000) t 'Turkiye' ps 0.3 lt 7 lc rgb 'navy blue' lw 3 w lp ,\
'population.txt' using 1:($3/1000000) t 'Germany' ps 0.3 lt 4 lc rgb 'red' lw 3 w lp ,\
'population.txt' using 1:($4/1000000) t 'UK' ps 0.3 lt 8 lc rgb 'green' lw 3 w lp 
