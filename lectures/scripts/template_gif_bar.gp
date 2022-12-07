#/usr/bin/gnuplot
set terminal gif animate delay 1 font 'Times,14'
set output 'population.gif'

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

set boxwidth 10
set style fill solid
unset xtics
unset xlabel

do for [i=1:62]{
plot 'population.txt' using (1980):($2/1000000) every ::i::i t 'Turkiye' ps 0.3 lt 7 lc rgb 'navy blue' lw 3 w boxes ,\
'population.txt' using (1992):($3/1000000) every ::i::i t 'Germany' ps 0.3 lt 4 lc rgb 'red' lw 3 w boxes ,\
'population.txt' using (2004):($4/1000000) every ::i::i t 'UK' ps 0.3 lt 8 lc rgb 'green' lw 3 w boxes
}
