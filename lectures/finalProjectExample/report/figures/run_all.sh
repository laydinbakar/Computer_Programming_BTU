for i in KSP1 KSP2 lines1 lines2 lines34567 iterations midpoints
do
cd ${i}
pdflatex ${i}.tex
rm -rf *.aux *.log
cd ..
ln -s ${i}/${i}.pdf .
done

for i in KSPPgf hexaPgf treePgf
do
cd ${i}
pdflatex ${i}.tex
rm -rf *.aux *.log
cd ..
ln -s ${i}/${i}.pdf .
done
