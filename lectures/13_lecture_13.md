# Lecture 13 (30.12.2022)
## Pgfplots

We can read data from a file and plot it in LaTeX documents. To do it we need the `pgfplots` package. A line graph and a bar graph examples are given below.
To draw those graphs you need [population.txt](https://raw.githubusercontent.com/laydinbakar/Computer_Programming_BTU/main/lectures/scripts/population.txt) file in the same directory as your LaTeX documents.

### Line graph

```latex
\documentclass{article}
%\documentclass[margin=2mm]{standalone}
\usepackage{pgfplots}
\usepackage{amsmath}

\date{\today}
\title{Population Change in Different Countries}
\author{Levent Aydinbakar}

\def\w{4.5in}
\def\h{3in}
\def\lpx{1990}
\def\lpy{0}

\begin{document}
\maketitle

\section{Population in Turkiye}

\begin{figure}[h]
  \centering
    \begin{tikzpicture}
      \begin{axis}
      [
      % Graph sizes
      width=\w,
      height=\h,
      % Line thickness
      axis line style = thick,
      % Grids
      major grid style={line width=.2pt,draw=gray!50},
      grid style={line width=.1pt, draw=gray!10},
      minor x tick num=4,
      minor y tick num=1,
      grid = both,
      % Legend type and position
      legend style={draw=none, at={(axis cs:\lpx, \lpy)}, /tikz/every even column/.append style={column sep=5mm}, anchor=center},
      legend columns=5,
      scaled y ticks = false,
      % Settings
      ymin = 20, 
      ymax = 90,
      xmin = 1960, 
      xmax = 2020,
      xtick = {1960, 1970, 1980, 1990, 2000, 2010, 2020},
      xticklabels = {1960, 1970, 1980, 1990, 2000, 2010, 2020},
      ytick = {20,30,40,50,60,70,80,90},
      xlabel = $\displaystyle\int_\Omega \mathbf{w} \cdot \pmb\nabla \cdot \pmb\sigma \mathrm{d} \Omega$,
      ylabel = $\int_\Omega \mathbf{w} \cdot \pmb\nabla \cdot \pmb\sigma \mathrm{d} \Omega$,
      ]
      \addplot[thick,blue] table[x expr=\thisrowno{0}, y expr=\thisrowno{1}/1000000] {population.txt};
      \addplot[thick,red] table[x expr=\thisrowno{0}, y expr=\thisrowno{2}/1000000] {population.txt};
      \addplot[thick,green!80!black] table[x expr=\thisrowno{0}, y expr=\thisrowno{3}/1000000] {population.txt};
      \legend{Turkiye, Germany, UK}


      \node[right] at (axis cs:1962,85) {Population of three different countries};
      \draw[line width=1.1pt, red] (axis cs:1992,55) rectangle (axis cs:1996,60);
      \draw[line width=1.1pt, cyan] (axis cs:2017.5,80) rectangle (axis cs:2019.5,85);
      \end{axis}
    \end{tikzpicture}
  \caption{Population change in Turkiye in years. The \textit{red} and \textit{cyan} boxes show where population of Turkiye exceeded the population of Germany and the UK, respectively}
\end{figure}

\begin{align}
\int_\Omega \mathbf{w} \cdot \pmb\nabla \cdot \pmb\sigma \mathrm{d} \Omega
\end{align}

\end{document}
```

### Bar graph

```latex
\documentclass{article}
%\documentclass[margin=2mm]{standalone}
\usepackage{pgfplots}
\usepackage{amsmath}

\date{\today}
\title{Population Change in Different Countries}
\author{Levent Aydinbakar}

\def\w{4.5in}
\def\h{3in}
\def\lpx{2015}
\def\lpy{0}

\begin{document}
\maketitle

\section{Population in Turkiye}

\begin{figure}[h]
  \centering
    \begin{tikzpicture}
      \begin{axis}
      [
      % Set bar graph
      ybar, bar width=4pt,
      % Graph sizes
      width=\w,
      height=\h,
      % Line thickness
      axis line style = thick,
      % Grids
      major grid style={line width=.2pt,draw=gray!50},
      grid style={line width=.1pt, draw=gray!10},
      minor x tick num=1,
      minor y tick num=1,
      grid = both,
      % Legend type and position
      legend style={draw=none, at={(axis cs:\lpx, \lpy)}, /tikz/every even column/.append style={column sep=5mm}, anchor=center},
      legend columns=5,
      scaled y ticks = false,
      % Settings
      ymin = 20, 
      ymax = 90,
      xmin = 2009.5, 
      xmax = 2020.5,
      %xtick = {1960, 1970, 1980, 1990, 2000, 2010, 2020},
      xtick = {2010, 2012, 2014, 2016, 2018, 2020},
      %xticklabels = {1960, 1970, 1980, 1990, 2000, 2010, 2020},
      xticklabels = {2010, 2012, 2014, 2016, 2018, 2020},
      ytick = {20,30,40,50,60,70,80,90},
      xlabel = $\displaystyle\int_\Omega \mathbf{w} \cdot \pmb\nabla \cdot \pmb\sigma \mathrm{d} \Omega$,
      ylabel = $\int_\Omega \mathbf{w} \cdot \pmb\nabla \cdot \pmb\sigma \mathrm{d} \Omega$,
      ]
      \addplot[fill=blue, thick,blue] table[x expr=\thisrowno{0}, y expr=\thisrowno{1}/1000000] {population.txt};
      \addplot[fill=red, thick,red] table[x expr=\thisrowno{0}, y expr=\thisrowno{2}/1000000] {population.txt};
      \addplot[fill=green!80!black, thick,green!80!black] table[x expr=\thisrowno{0}, y expr=\thisrowno{3}/1000000] {population.txt};
      \legend{Turkiye, Germany, UK}


      \node[right] at (axis cs:2010,85) {Population of three different countries};
      \draw[line width=1.1pt, red] (axis cs:1992,55) rectangle (axis cs:1996,60);
      \draw[line width=1.1pt, cyan] (axis cs:2017.5,80) rectangle (axis cs:2019.5,85);
      \end{axis}
    \end{tikzpicture}
  \caption{Population change in Turkiye in years. The \textit{red} and \textit{cyan} boxes show where population of Turkiye exceeded the population of Germany and the UK, respectively}
\end{figure}

\begin{align}
\int_\Omega \mathbf{w} \cdot \pmb\nabla \cdot \pmb\sigma \mathrm{d} \Omega
\end{align}

\end{document}
```

