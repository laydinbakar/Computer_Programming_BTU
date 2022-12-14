# Lecture 11 (16.12.2022)
You can watch the video lectures on YouTube using the links below.
* [1-Introduction to LaTeX](https://youtu.be/mlq51ZY5cXk)
* [2-Math in LaTeX](https://youtu.be/mGm0PpNVQRQ)
* [3-References in LaTeX](https://youtu.be/MCmDVsKFwWE)

## Introduction to LaTeX
LaTeX is a tool for typesetting profesisonal-looking documents. 

## Why learn LaTeX?
* Professional-looking documents can be made in LaTeX.
* It is free and open-source. 
* Writing mathematical expressions is easy in LaTeX.
* Adding indexes, footnotes, references, table of contents, list of figures and tables is easy in LaTeX.
* Check [this](https://www.lode.de/blog/comparing-word-and-latex#:~:text=%E2%80%8DLaTeX%20is%20a%20typesetting%20system,style%2C%20references%2C%20and%20text.) for more reasons.

## Use LaTeX to prepare your professional-looking documents
In the LaTeX documents, the percent sign is used for commenting in the documents.
In this tutorial, I will put a comment explaining one line below.

### The very first LaTeX document
See the below code for the first LaTeX document.

```latex
% Start with
\documentclass{article}

% Begin the document here
\begin{document}

This is the first document prepared using \LaTeX.

% The document finishes here
\end{document}
```

Write this in a file so called `firstLatexDocument.tex`, save and exit. Then run the following command to execute the code.

```latex
pdflatex firstLatexDocument.tex
```


Three files will be made by LaTeX when you compile the document.
1. `firstLatexDocument.pdf`
1. `firstLatexDocument.aux` 
1. `firstLatexDocument.log`

You can open the PDF file by `evince firstLatexDocument.pdf`.

The auxiliary file and log file contain information about your documents, such as, the files loaded, error messages, warnings, general information messages, references-related information and etc. You can delete these files, but LaTeX will create them again when you compile the code next time. The auxiliary file also needed for references. Hence if you remove it, you will need to compile the document two times next time. One is for making the file, second one is for using that file to reference correctly. We will see it in the following parts of this tutorial.

### Paper size, orientation and margins
The package `geometry` can be used to set the paper size to,
* `a4paper` ( $210\times297~\mathrm{mm^2}$ ), 
* `a5paper` ( $148\times210~\mathrm{mm^2}$ ), 
* `b5paper` ( $250\times176~\mathrm{mm^2}$ ), 
* `letterpaper` ( $215.9\times279.4~\mathrm{mm^2}$ ), 
* `legalpaper` ( $215.9\times355.6~\mathrm{mm^2}$ )...

Landscape or portrait modes, and
margins can also be set with the same package. 
See the example below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Begin the document here
\begin{document}

This is the first document prepared using \LaTeX.

% The document finishes here
\end{document}
```

### Italic, bold, underline
Italic, bold and underlined texts can be written in LaTeX as shown below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Import font package
\usepackage{fontenc}

% Begin the document here
\begin{document}

This line uncludes \textit{italic text}, \textbf{bold text} and \underline{underlined text}. Some \texttt{commands of terminal} and \textsc{Small Caps} can also be expressed in \LaTeX. 

\textbf{These \texttt{can also} be \underline{used} \textit{together}}.

\end{document}
```


### Font
The default font in LaTeX is Computer Modern Roman. It can be changed using `fontenc` package as shown below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Import font package
\usepackage{fontenc}

% Begin the document here
\begin{document}

This line is written using the default font of \LaTeX. The default font is ``Computer Modern Roman.'' 

{\fontfamily{ptm}\selectfont
This line is written using ``Times'' font using the short name of it ``ptm.''
}

{\fontfamily{pcr}\selectfont
This line is written using ``Courier'' font using the short name of it ``pcr.''
}

{\fontfamily{phv}\selectfont
This line is written using ``Helvetica'' font using the short name of it ``phv.''
}

% The document finishes here
\end{document}
```

### Font size
The font sizes can be used in LaTeX are listed below.
* `\tiny`,
* `\scriptsize`,
* `\footnotesize`,
* `\small`,
* `\normalsize`,
* `\large`,
* `\Large`,
* `\LARGE`,
* `\huge`,
* `\Huge`.

For example see the document below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Import font package
\usepackage{fontenc}

% Begin the document here
\begin{document}

\scriptsize A script size is this.

\normalsize A normal size is this.

\Large A Large size is this.

\LARGE A LARGE size is this.

\huge A huge size is this.

\footnotesize This \Large sentence is \small written in \tiny various sizes.

This \Huge is \large another \LARGE example.

% The document finishes here
\end{document}
```

### Adding title, author and date...
Title, author and date can be added into the LaTeX documents.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Import font package
\usepackage{fontenc}

% Add title, author and date
\title{The First \LaTeX{} Document}
\author{Levent Aydinbakar}
\date{December 2022}

% Begin the document here
\begin{document}

% Write title, author and date
\maketitle

This document includes a title, author and date.

% The document finishes here
\end{document}
```

### Making customized title pages
With that purpose, we can use some packages (lots of them exists on the internet) or we can just use different font sizes, bold characters and `\centering`, `\vspace`, `\hscpase`, `\newpage`, and `\newline` as shown below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Import font package
\usepackage{fontenc}

% Begin the document here
\begin{document}


\begin{titlepage}

\vfill\null

\centering


\vspace{2cm}
{\Huge \textbf{The First \LaTeX{} Document}}

\vspace{2cm}
\huge Levent Aydinbakar \hspace{2cm} Ismail Hos

\vspace{2cm}
\LARGE Computer Programming Course \\
\LARGE Department of Mechanical Engineering \\
\LARGE Bursa Technical University


\vfill

\begin{abstract}
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
There is an abstract paragraph here.
\end{abstract}

\vspace{3cm}
\large \today

\end{titlepage}


This document includes a title page.

% The document finishes here
\end{document}
```

### Lists
Lists can be made in LaTeX as shown below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Import font package
\usepackage{fontenc}

% Begin the document here
\begin{document}

\begin{itemize}
\item This is an item.
\item This is another item.
\end{itemize}

\vspace{2cm}

\begin{enumerate}
\item This is an ordered item.
\item This is another ordered item.
\end{enumerate}

\vspace{2cm}

\begin{itemize}
\item This is a primary item.
\begin{itemize}
\item This is a secondary item.
\begin{itemize}
\item This is a third level item.
\item This is another third level item.
\end{itemize}
\item This is another secondary item.
\end{itemize}
\item This is another primary item.
\end{itemize}

\vspace{2cm}

\begin{enumerate}
\item This is a primary ordered item.
\begin{enumerate}
\item This is a secondary ordered item.
\begin{enumerate}
\item This is a third level ordered item.
\item This is another third level ordered item.
\end{enumerate}
\item This is another secondary ordered item.
\end{enumerate}
\item This is another primary ordered item.
\end{enumerate}

% The document finishes here
\end{document}
```

### Mathematical expressions
To write an equation in a sentence we can use `$equation$` form. 

One of the best options for writing equations in LaTeX is use of `\begin{align}...\end{align}`. 
By doing this we can align multiple equations. See the examples below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Import font package
\usepackage{fontenc}

% Set title
\title{Derivation of the \\ Residual-Based Variational Multiscale \\ Formulation}
\author{Levent Aydinbakar}
\date{\today}

% Import math package for align
\usepackage{amsmath,amssymb}

% Begin the document here
\begin{document}
\maketitle

\begin{align}
x&=2, \\
y&=3, \\
z&=4, \\
x+y+z&=9.
\end{align}

% The document finishes here
\end{document}
```

### More complex equations
See the example below to write more complex equations in LaTeX.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Import font package
\usepackage{fontenc}

% Set title
\title{The Navier--Stokes Equations of \\ Incompressible Flows}
\author{Levent Aydinbakar}
\date{\today}

% Import math package for align
\usepackage{amsmath,amssymb}

% Begin the document here
\begin{document}
\maketitle

The Navier--Stokes equations are the fluid mechanics governing equations. Those of incompressible flows can be written as follows:
~
\begin{align}
\rho 
\left(
\dfrac{
\partial 
\mathbf{u}
}
{
\partial 
t
}
+ 
\mathbf{u} 
\cdot 
\pmb\nabla 
\mathbf{u} 
- 
\mathbf{f} 
\right)
- 
\pmb\nabla 
\cdot 
\pmb\sigma 
=& 
\mathbf{0}, 
\\
\pmb\nabla 
\cdot 
\mathbf{u} 
=& 
0.
\end{align}
Equations above are also called
the linear momentum conservation and the mass balance (continuity) equations. 
Here,
$\rho$ is the density, 
$\mathbf{u}$ is the velocity, 
$t$ is the time, 
$\mathbf{f}$ is the external force and 
$\pmb\sigma$ is the Cauchy stress tensor defined by
$$
\pmb\sigma = -p\mathbf{I} + 2\mu\pmb\varepsilon,
$$
where $p$, $\mathbf{I}$ and $\pmb\varepsilon$ are the pressure, identity tensor and strain-rate tensor which is formulated as shown below.
\begin{equation}
\pmb\varepsilon = 0.5(\pmb\nabla \mathbf{u} + \pmb\nabla \mathbf{u}^\intercal).
\end{equation}


% The document finishes here
\end{document}
```

Some other useful commands are listed below.

| Explanation | Command | Sign |
| --- | --- | --- | 
| Vectors in math | `\mathbf{u}` | $\mathbf{u}$ |
| Normal characters in math | `\mathrm{d}` | $\mathrm{d}$ |
| Subscripts and super scripts | `a^x` and `a_x` | $a^x$ and $a_x$ |
| Integral | `\int` | $\int$ |
| Sum | `\sum` | $\sum$ |
| Integral with limits | `\int_\Omega` | $\int_\Omega$ |
| Multiplication | `\cdot`, `\times`, `\otimes` | $\cdot$, $\times$, $\otimes$ |
| Inline division | `\frac{a}{b}` | $\frac{a}{b}$ |
| In eqautions division | `\dfrac{a}{b}` | $\dfrac{a}{b}$ |
| Fully covering parantheses | `\left( \dfrac{a}{b} \right)` | $\left( \dfrac{a}{b} \right)$ |
| Fully covering brackets | `\left\[ \dfrac{a}{b} \right\]` | $\left\[ \dfrac{a}{b} \right\]$ |
| Partial sign | `\partial` | $\partial$ |
| Stress tensor | `\pmb\sigma` | $\pmb\sigma$ |
| Strain tensor | `\pmb\varepsilon` | $\pmb\varepsilon$ |
| Nabla operator | `\pmb\nabla` | $\pmb\nabla$ |

For the other commands see [here](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols).

### Sections
We can add titles and easily divide our document into sections as follows:

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Set title
\title{Sections and Subsections}
\author{Levent Aydinbakar}
\date{\today}

% Begin the document here
\begin{document}
\maketitle

\section{The First Part}
This is the first part.
\subsection{The first sub-part}
This is the first sub-part of the first part.
\subsection{The second sub-part}
This is the second sub-part of the first part.
\section{The Second Part}
This is the second part.
\section{The Third Part}
This is the third part.
\subsection{The first sub-part}
This is the first sub-part of the third part.
\subsubsection{The first sub-sub-part}
This is the first sub-sub-part of the first sub-part of the third part.
\subsubsection{The first sub-sub-part}
This is the second sub-sub-part of the first sub-part of the third part.
\subsection{The second sub-part}
This is the second sub-part of the third part.


% The document finishes here
\end{document}
```

### Inserting images
To insert images into a document we can use `graphicx` package and `\includegraphics` function.
We can either use a PNG or a PDF figure to insert. Copy the `population.pdf` file you made last week into a folder so called 'figures'.

```bash
mkdir figures

cp -r ../Lecture10/population.pdf figures/
```

If you do not have that image, you can use [this](../scripts/template.gp) Gnuplot script and [this](../scripts/population.txt) text file to make it.

Then write the LaTeX code given below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Set title
\title{Insert Images in \LaTeX{}}
\author{Levent Aydinbakar}
\date{\today}

% Insert images
\usepackage{graphicx}
\graphicspath{{figures/}}

% Begin the document here
\begin{document}
\maketitle

This document includes a figure.

\begin{figure}
\includegraphics{population.pdf}
\end{figure}

Figure above shows the population change by years in three different countries.

% The document finishes here
\end{document}
```

To resize the figure, relocate it, to write a caption and to make it centered we can use some additional settings as given below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Set title
\title{Arrange Inserted Images in \LaTeX{}}
\author{Levent Aydinbakar}
\date{\today}

% Insert images
\usepackage{graphicx}
\graphicspath{{figures/}}

% Begin the document here
\begin{document}
\maketitle

This document includes a figure.

\begin{figure}[h]
\begin{center}
\includegraphics[width=5in]{population.pdf}
\caption{Population change in time in Turkiye, Germany and the United Kingdom}
\end{center}
\end{figure}

Figure above shows the population change by years in three different countries.

% The document finishes here
\end{document}
```

### Tables

We can add tables in LaTeX as shown below.

Please see [this webpage](https://www.overleaf.com/learn/latex/Tables) for details.


### Labels and cross-referencing
We can add labels in equations, figures, sections and subsections in LaTeX and we can refer in those labels during the document. See the example below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Set title
\title{Labels and Cross-Referencing in \LaTeX{}}
\author{Levent Aydinbakar}
\date{\today}

% Import math package for align
\usepackage{amsmath,amssymb}

% Insert images
\usepackage{graphicx}
\graphicspath{{figures/}}

% Clickable links
\usepackage[hidelinks]{hyperref}

% Begin the document here
\begin{document}
\maketitle
\section{The First Section}
\label{sec:firstSection}

This document includes a figure. Figure~\ref{fig:population} is given in Section~\ref{subsec:figurePart}.

This document also includes some equations. Equation~(\ref{eq:Newton}) and Equations~(\ref{eq:linMom})~and~(\ref{eq:continuity}) are given in Section~\ref{subsec:equationsPart}.

\subsection{Figure part}
\label{subsec:figurePart}

Here a figure is inserted.

\begin{figure}[h]
\begin{center}
\includegraphics[width=5in]{population.pdf}
\caption{Population change in time in Turkiye, Germany and the United Kingdom}
\label{fig:population}
\end{center}
\end{figure}

Figure~\ref{fig:population} shows the population change by years in three different countries.

\subsection{Equations part}
\label{subsec:equationsPart}

Newton's Second Law is given as follows:
\begin{align}
\mathbf{F} = m \mathbf{a}.
\label{eq:Newton}
\end{align}
Equation~(\ref{eq:Newton}) is also called the momentum equation. 
With some arrangements, 
the linear momentum conservation equation given in Equation~(\ref{eq:linMom}) is obtained for incompressible flows.
\begin{align}
\rho 
\left( \dfrac{\partial \mathbf{u}}{\partial t}
+ 
\mathbf{u} \cdot \pmb\nabla \mathbf{u} - \mathbf{f} \right)
- 
\pmb\nabla \cdot \pmb\sigma = \mathbf{0}, 
\label{eq:linMom}
\end{align}

The continuity equation is written as follows:
\begin{align}
\pmb\nabla \cdot \mathbf{u} = 0.
\label{eq:continuity}
\end{align}

Equations~(\ref{eq:linMom}--\ref{eq:continuity}) together is socalled the Navier--Stokes equations.

% The document finishes here
\end{document}
```

### Table of contents and figures
We can use the same document to list the contents and figures at the beginning automatically.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Set title
\title{Labels and Cross-Referencing in \LaTeX{}}
\author{Levent Aydinbakar}
\date{\today}

% Import math package for align
\usepackage{amsmath,amssymb}

% Insert images
\usepackage{graphicx}
\graphicspath{{figures/}}

% Begin the document here
\begin{document}
\maketitle

\tableofcontents
\lisfoffigures

\section{The First Section}
\label{sec:firstSection}

This document includes a figure. Figure~\ref{fig:population} is given in Section~\ref{subsec:figurePart}.

This document also includes some equations. Equation~(\ref{eq:Newton}) and Equations~(\ref{eq:linMom})~and~(\ref{eq:continuity}) are given in Section~\ref{subsec:equationsPart}.

\subsection{Figure part}
\label{subsec:figurePart}

Here a figure is inserted.

\begin{figure}[h]
\begin{center}
\includegraphics[width=5in]{population.pdf}
\caption{Population change in time in Turkiye, Germany and the United Kingdom}
\label{fig:population}
\end{center}
\end{figure}

Figure~\ref{fig:population} shows the population change by years in three different countries.

\subsection{Equations part}
\label{subsec:equationsPart}

Newton's Second Law is given as follows:
\begin{align}
\mathbf{F} = m \mathbf{a}.
\label{eq:Newton}
\end{align}
Equation~(\ref{eq:Newton}) is also called the momentum equation. 
With some arrangements, 
the linear momentum conservation equation given in Equation~(\ref{eq:linMom}) is obtained for incompressible flows.
\begin{align}
\rho 
\left( \dfrac{\partial \mathbf{u}}{\partial t}
+ 
\mathbf{u} \cdot \pmb\nabla \mathbf{u} - \mathbf{f} \right)
- 
\pmb\nabla \cdot \pmb\sigma = \mathbf{0}, 
\label{eq:linMom}
\end{align}

The continuity equation is written as follows:
\begin{align}
\pmb\nabla \cdot \mathbf{u} = 0.
\label{eq:continuity}
\end{align}

Equations~(\ref{eq:linMom}--\ref{eq:continuity}) together is socalled the Navier--Stokes equations.

% The document finishes here
\end{document}
```

### References
Citing a study in our documents is easy in LaTeX. 
To cite a document we need a file `ref.bib` for example and we need to execute that file.
An example `.bib` file is as follows:
```latex
@article{aydinbakar21,
 title={Space--time VMS isogeometric analysis of the Taylor--Couette flow},
 author={Aydinbakar, Levent and Takizawa, Kenji and Tezduyar, Tayfun E and Kuraishi, Takashi},
 journal={Computational Mechanics},
 volume={67},
 number={5},
 pages={1515--1541},
 year={2021},
 publisher={Springer}
}

@article{otoguro19,
 title={Turbocharger turbine and exhaust manifold flow computation with the space--time variational multiscale method and isogeometric analysis},
 author={Otoguro, Yuto and Takizawa, Kenji and Tezduyar, Tayfun E and Nagaoka, Kenichiro and Mei, Sen},
 journal={Computers \& Fluids},
 volume={179},
 pages={764--776},
 year={2019},
 publisher={Elsevier}
}

@article{aydinbakar21b,
  title={U-duct turbulent-flow computation with the ST-VMS method and isogeometric discretization},
  author={Aydinbakar, Levent and Takizawa, Kenji and Tezduyar, Tayfun E and Matsuda, Daisaku},
  journal={Computational Mechanics},
  volume={67},
  number={3},
  pages={823--843},
  year={2021},
  publisher={Springer}
}
```

To execute this file, we first need to run `bibtex filename`, then run `pdflatex filename`.
Find how to refer these two studies in a document below.

```latex
% Start with
\documentclass{article}

% Set the paper size and margins
\usepackage{geometry}
\geometry{a4paper, portrait, left=20mm, right=20mm, top=30mm, bottom=30mm}

% Set title
\title{Referencing in \LaTeX{}}
\author{Levent Aydinbakar}
\date{\today}

% Import math package for align
\usepackage{amsmath,amssymb}

% Insert images
\usepackage{graphicx}
\graphicspath{{figures/}}

% Insert clickable references
\usepackage[hidelinks]{hyperref}

% Begin the document here
\begin{document}
\maketitle

Space--Time Variational Multiscale method is used in \cite{aydinbakar21} on a Taylor--Couette flow computation.

This method is also used in \cite{otoguro19}.

Another similar study is \cite{aydinbakar21b}.

\newpage
%\bibliographystyle{apalike}
%\bibliographystyle{plain}
\bibliographystyle{unsrt}
\bibliography{ref.bib}

\newpage
Appendices
% The document finishes here
\end{document}
```

## Example document
Click [here](https://github.com/laydinbakar/Computer_Programming_BTU/blob/main/lectures/files/heatTransfer.pdf) to download an example report. Write this report by yourself. You can find some PNG, PDF and bib files you need to use in this report [here](https://github.com/laydinbakar/Computer_Programming_BTU/tree/main/lectures/files).
