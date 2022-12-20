# Lecture 12 (23.12.2022)
## Tikz and Pgfplots

You can watch the video lectures on YouTube using the links below.
* [1-Tikz](https://youtu.be/mlq51ZY5cXk)
* [2-Pgfplots](https://youtu.be/mlq51ZY5cXk)

## Tikz
Tikz is a package in LaTeX to draw professional-looking drawings.

### Import package
We need to import Tikz package first.
```latex
\usepackage{tikz}
```
We can either make our drawings in our LaTeX documents directly or we can make the drawings outside of the documents and import to LaTeX as PDF files using `includegraphics` function.

To make the drawings outside an appropriate document class is `standalone`. We can open it as follows.
```latex
\documentclass[tikz, margin=2mm]{standalone}
```

In this tutorial, the drawings will be made in the LaTeX documents.

We can draw simple shapes as follows:
### Lines
```latex
\documentclass{article}
\usepackage{tikz}

\begin{document}
\begin{figure}
\begin{tikzpicture}

\draw (0,0) -- (4,0);

\end{tikzpicture}
\end{figure}
\end{document}
```

### Rectangles
```latex
\documentclass{article}
\usepackage{tikz}

\begin{document}
\begin{figure}
\begin{tikzpicture}

\draw (0,0) rectangle (4,2);

\end{tikzpicture}
\end{figure}
\end{document}
```

### Circles
```latex
\documentclass{article}
\usepackage{tikz}

\begin{document}
\begin{figure}
\begin{tikzpicture}

\draw (0,0) circle (4cm);

\end{tikzpicture}
\end{figure}
\end{document}
```

### Ellipses
```latex
\documentclass{article}
\usepackage{tikz}

\begin{document}
\begin{figure}
\begin{tikzpicture}

\draw (0,0) ellipse (4cm and 2cm);

\end{tikzpicture}
\end{figure}
\end{document}
```

### B-splines
```latex
\documentclass{article}
\usepackage{tikz}

\begin{document}
\begin{figure}
\begin{tikzpicture}

\draw (0,0) .. controls (1,-1) and (2,1) .. (3,0);

\end{tikzpicture}
\end{figure}
\end{document}
```

### Line shape and colors
```latex
\documentclass{article}
\usepackage{tikz}
\usepackage{xcolor}

\begin{figure}[ht]
\centering
\begin{tikzpicture}
\draw[line width=1pt, brown!50!yellow] (5,0) ellipse (2cm and 3cm);
\draw[line width=2pt, black!53!blue!90!white, dotted] (0,0) ellipse (3cm and 2cm);
\end{tikzpicture}
\end{figure}
\end{document}
```

### Arrows
```latex
\documentclass{article}
\usepackage{tikz}
\usepackage{xcolor}

\begin{figure}[ht]
\centering
\begin{tikzpicture}
\draw[->] (0,0) -- (6,0);
\draw[-latex] (0,-2) -- (6,-2);
\draw[-stealth] (0,-4) -- (6,-4);
\end{tikzpicture}
\end{figure}
\end{document}
```

### Nodes
```latex
\documentclass{article}
\usepackage{tikz}
\usepackage{xcolor}

\begin{figure}[ht]
\centering
\begin{tikzpicture}
\draw[-latex] (0,0) -- (6,0) node[right]{$x_1$};
\draw[-latex] (0,0) -- (0,6) node[above]{$x_2$};
\end{tikzpicture}
\end{figure}
\end{document}
```

### Define variables
```latex
\documentclass{article}
\usepackage{tikz}
\usepackage{xcolor}

\begin{figure}[ht]
\centering
\begin{tikzpicture}
\draw[-latex] (0,0) -- (6,0) node[right]{$x_1$};
\draw[-latex] (0,0) -- (0,6) node[above]{$x_2$};
\def\x{-0.4}
\def\y{-0.4}
\node at (\x,\y) {$(0,0)$};
\node at ( 1.0,\y) {$1$};
\node at ( 2.0,\y) {$2$};
\node at ( 3.0,\y) {$3$};
\node at ( 4.0,\y) {$4$};
\node at ( 5.0,\y) {$5$};
\draw (1,0.1) -- (1,-0.1);
\draw (2,0.1) -- (2,-0.1);
\draw (3,0.1) -- (3,-0.1);
\draw (4,0.1) -- (4,-0.1);
\draw (5,0.1) -- (5,-0.1);
\end{tikzpicture}
\end{figure}
\end{document}
```

### For loops with `foreach` function
```latex
\documentclass{article}
\usepackage{tikz}
\usepackage{xcolor}

\begin{figure}[ht]
\centering
\begin{tikzpicture}
\draw[-latex] (0,0) -- (6,0) node[right]{$x_1$};
\draw[-latex] (0,0) -- (0,6) node[above]{$x_2$};
\def\x{-0.4}
\def\y{-0.4}
\node at (\x,\y) {$(0,0)$};
\node at ( 1.0,\y) {$1$};
\node at ( 2.0,\y) {$2$};
\node at ( 3.0,\y) {$3$};
\node at ( 4.0,\y) {$4$};
\node at ( 5.0,\y) {$5$};
\draw (1,0.1) -- (1,-0.1);
\draw (2,0.1) -- (2,-0.1);
\draw (3,0.1) -- (3,-0.1);
\draw (4,0.1) -- (4,-0.1);
\draw (5,0.1) -- (5,-0.1);

\foreach \y in {1,2,3,4,5}
\node at (\x, \y) {$\y$};
\foreach \y in {1,2,3,4,5}
\draw (0.1,\y) -- (-0.1,\y);
\end{tikzpicture}
\end{figure}

\begin{figure}[ht]
\centering
\begin{tikzpicture}
\foreach \y in {-3,-2,-1,0,1,2,3,4,5,6}
  \draw (1,\y) -- (-1,\y);
\end{tikzpicture}
\caption{These are lines (foreach)}
\end{figure}

\begin{figure}[ht]
\centering
\begin{tikzpicture}
\foreach \y in {-3,-2,-1,0,1,2,3,4,5,6}
  \draw ( 1,\y) -- (-1,\y); 
\foreach \y in {-3,-2,-1,0,1,2,3,4,5,6}
  \node at (0,\y+0.2) {$\y$};
\end{tikzpicture}
\caption{These are lines with numbers}
\end{figure}

\end{document}
```

### Grid lines
```latex
\documentclass{article}
\usepackage{tikz}
\usepackage{xcolor}

\begin{figure}[ht]
\centering
\begin{tikzpicture}
%\draw[step=0.1cm, gray!50!white, line width=0.5pt] (-3,-3) grid (6,6);
%\draw[step=1cm, gray, line width=0.5pt] (-3,-3) grid (6,6);
%\foreach \y in {-3,-2,-1,0,1,2,3,4,5,6}
%  \draw (1pt,\y cm) -- (-1pt,\y cm) node[anchor=east] {$\y$};
%\foreach \x in {-3,-2,-1,0,1,2,3,4,5,6}
%  \draw (\x cm,1pt) -- (\x cm,-1pt) node[anchor=north] {$\x$};
\draw[fill=red] (2.2,2.2) circle (1mm);
\draw[fill=black] (-2.2,-2.2) circle (1mm);
\draw[line width=1pt, brown!50!yellow] (0,0) ellipse (2cm and 3cm);
\end{tikzpicture}
\caption{This is a grid}
\end{figure}
\end{document}
```

### An example document

```latex
\documentclass{article}
%\documentclass{standalone}
\usepackage{tikz}
\usepackage{xcolor}

\begin{document}

\begin{figure}[h]
\begin{center}
\begin{tikzpicture}
\draw (0.0, 0.0) 
-- (3.5, 0.0) 
-- (3.5, 2.0) 
-- (4.5, 2.0) 
-- (4.5, 4.0) 
-- (3.5, 4.0) 
-- (3.5, 5.0) 
-- (3.0, 5.0)  
-- (3.0, 0.5) 
-- (0.5, 0.5) 
-- (0.5, 5.0) 
-- (0.0, 5.0) 
-- (0.0, 0.0) 
;
\draw (3.5, 2.5) rectangle (4.0, 3.5);
\end{tikzpicture}
\caption{Schematic of the heat transfer problem. Geometry}
\label{fig:problem}
\end{center}
\end{figure}

Schematic of the heat transfer probelm is shown in Figure~\ref{fig:problem}.

\begin{figure}[h]
\begin{center}
\begin{tikzpicture}
\draw (0.0, 0.0) 
-- (3.5, 0.0) 
-- (3.5, 2.0) 
-- (4.5, 2.0) 
-- (4.5, 4.0) 
-- (3.5, 4.0) 
-- (3.5, 5.0) 
-- (3.0, 5.0)  
-- (3.0, 0.5) 
-- (0.5, 0.5) 
-- (0.5, 5.0) 
-- (0.0, 5.0) 
-- (0.0, 0.0) 
;
\draw (3.5, 2.5) rectangle (4.0, 3.5);
\draw[latex-latex] ( 0.0,-0.1) -- ( 3.5,-0.1);
\draw[latex-latex] ( 3.6, 0.0) -- ( 3.6, 2.0);
\draw[latex-latex] ( 4.6, 2.0) -- ( 4.6, 4.0);
\draw[latex-latex] ( 4.1, 2.5) -- ( 4.1, 3.5);
\draw[latex-latex] (-0.1, 0.0) -- (-0.1, 5.0);
\draw[latex-latex] ( 0.0, 5.1) -- ( 0.5, 5.1);
\draw[latex-latex] ( 0.0, 5.1) -- ( 0.5, 5.1);
\draw[latex-latex] ( 3.5, 4.1) -- ( 4.5, 4.1);
\draw[latex-latex] ( 3.5, 3.6) -- ( 4.0, 3.6);
\end{tikzpicture}
\caption{Schematic of the heat transfer problem. Arrows}
\label{fig:problem_geo}
\end{center}
\end{figure}

\begin{figure}[h]
\begin{center}
\begin{tikzpicture}
\draw (0.0, 0.0) 
-- (3.5, 0.0) 
-- (3.5, 2.0) 
-- (4.5, 2.0) 
-- (4.5, 4.0) 
-- (3.5, 4.0) 
-- (3.5, 5.0) 
-- (3.0, 5.0)  
-- (3.0, 0.5) 
-- (0.5, 0.5) 
-- (0.5, 5.0) 
-- (0.0, 5.0) 
-- (0.0, 0.0) 
;
\draw (3.5, 2.5) rectangle (4.0, 3.5);
\draw[latex-latex] ( 0.0,-0.1) -- ( 3.5,-0.1) node[below, midway]{$35$};
\draw[latex-latex] ( 3.6, 0.0) -- ( 3.6, 2.0) node[right, midway]{$20$};
\draw[latex-latex] ( 4.6, 2.0) -- ( 4.6, 4.0) node[right, midway]{$20$};
\draw[latex-latex] ( 4.1, 2.5) -- ( 4.1, 3.5) node[right, midway, inner sep=0mm]{$10$};
\draw[latex-latex] (-0.1, 0.0) -- (-0.1, 5.0) node[left, midway]{$50$};
\draw[latex-latex] ( 0.0, 5.1) -- ( 0.5, 5.1) node[above, midway]{$5$};
\draw[latex-latex] ( 3.5, 4.1) -- ( 4.5, 4.1) node[above, midway]{$10$};
\draw[latex-latex] ( 3.5, 3.6) -- ( 4.0, 3.6) node[above, midway]{$5$};
\end{tikzpicture}
\caption{Schematic of the heat transfer problem. Sizes}
\label{fig:problem_geo_with_numbers}
\end{center}
\end{figure}

There is a paragraph here.
There is a paragraph here.
There is a paragraph here.
There is a paragraph here.
There is a paragraph here.
There is a paragraph here.
There is a paragraph here.
There is a paragraph here.
There is a paragraph here.


\begin{figure}[h]
\begin{center}
\begin{tikzpicture}
\draw[blue!10!white, fill=blue!10!white] (0.5, 0.5) rectangle (3.0, 5.0);
\node at (1.75,4.5) {Water};
\node at (1.75,4.0) {$89^\circ\mathrm{C}$};
\node at (1.75,5.6) {Room temp.: $22^\circ\mathrm{C}$};
\draw (0.0, 0.0) 
-- (3.5, 0.0) 
-- (3.5, 2.0) 
-- (4.5, 2.0) 
-- (4.5, 4.0) 
-- (3.5, 4.0) 
-- (3.5, 5.0) 
-- (3.0, 5.0)  
-- (3.0, 0.5) 
-- (0.5, 0.5) 
-- (0.5, 5.0) 
-- (0.0, 5.0) 
-- (0.0, 0.0) 
;
\draw (3.5, 2.5) rectangle (4.0, 3.5);
\draw[latex-latex] ( 0.0,-0.1) -- ( 3.5,-0.1) node[below, midway]{$35$};
\draw[latex-latex] ( 3.6, 0.0) -- ( 3.6, 2.0) node[right, midway]{$20$};
\draw[latex-latex] ( 4.6, 2.0) -- ( 4.6, 4.0) node[right, midway]{$20$};
\draw[latex-latex] ( 4.1, 2.5) -- ( 4.1, 3.5) node[right, midway, inner sep=0mm]{$10$};
\draw[latex-latex] (-0.1, 0.0) -- (-0.1, 5.0) node[left, midway]{$50$};
\draw[latex-latex] ( 0.0, 5.1) -- ( 0.5, 5.1) node[above, midway]{$5$};
\draw[latex-latex] ( 3.5, 4.1) -- ( 4.5, 4.1) node[above, midway]{$10$};
\draw[latex-latex] ( 3.5, 3.6) -- ( 4.0, 3.6) node[above, midway]{$5$};
\end{tikzpicture}
\caption{Schematic of the heat transfer problem. Water}
\label{fig:problem_geo_with_numbers}
\end{center}
\end{figure}

\end{document}
```

### Animations
```latex
\documentclass[tikz,margin=2mm]{standalone}
\usepackage{tikz}

\begin{document}

\foreach \x in {0,1,...,60,59,58,...,0}{
\begin{tikzpicture}

\draw[line width=1.5pt, blue!30!black, fill=white] (0,0) rectangle (6,4);
\draw[line width=0.5pt, red] (0,0) rectangle (\x/10,4);
\draw[line width=1.5pt, blue!30!black] (0,0) rectangle (6,4);
  
\end{tikzpicture}
}

\end{document}
```

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
