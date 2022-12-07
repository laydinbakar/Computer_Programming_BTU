#/usr/bin/env gnuplot
set terminal pdf font 'Times,14' size 4.5in,3in
set output 'population.pdf'

set xyplane 0
set yrange [1962:2022]
set zrange [20:90]
set xrange [1:3]
set ytics autofreq 1962,10

set grid ytics lt -1 lw 0.2 lc rgb 'gray'
set grid xtics lt -1 lw 0.2 lc rgb 'gray'
set grid ztics lt -1 lw 0.2 lc rgb 'gray'

set border lw 1.5

set xtics ("Turkiye" 1, "Germany" 2, "UK" 3) offset 0,-1

unset key

splot 'population.txt' using (1):1:($2/1000000) t 'Turkiye' ps 0.3 lt 7 lc rgb 'navy blue' lw 3 w boxes ,\
'population.txt' using (2):1:($3/1000000) t 'Germany' ps 0.3 lt 4 lc rgb 'red' lw 3 w boxes ,\
'population.txt' using (3):1:($4/1000000) t 'UK' ps 0.3 lt 8 lc rgb 'green' lw 3 w boxes
