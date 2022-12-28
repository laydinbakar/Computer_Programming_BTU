#!/usr/bin/env zsh

echo "This is Team-X Final Project repository."
echo "***************"
echo "Team members are:"
echo "# ID Name Surname"
echo "1 1234567890 Levent Aydinbakar"
echo "2 1234567890 Levent Aydinbakar"
echo "***************"
echo "Press enter to continue"
echo "***************"
read X

echo "This script compiles all the necessary files to prepare our report."
ls

echo "***************"
echo "Press enter to continue"
echo "***************"
read X

cd python/01.sierpinski_points
./run.sh
mkdir -p ../../report/figures/iterations/textFiles/
cp -r *.txt ../../report/figures/iterations/textFiles/
cd ../../
echo "***************"
echo "Text files for section 1 is made and copied to report/figures/iterations/textFiles directory."

echo "***************"
echo "Press enter to continue"
echo "***************"
read X

cd python/02.sierpinski_lines
./run.sh
mkdir -p ../../report/figures/lines1/textFiles/ 
mkdir -p ../../report/figures/lines2/textFiles/
cp -r lines1.txt ../../report/figures/lines1/textFiles/ 
cp -r lines1.txt ../../report/figures/lines2/textFiles/ 
cp -r lines2.txt ../../report/figures/lines2/textFiles/
for i in 3 4 5 6 7
do
mkdir -p ../../report/figures/lines34567/textFiles/
cp -r lines${i}.txt ../../report/figures/lines34567/textFiles/
done
cd ../../
echo "***************"
echo "Text files for section 2 are made and copied to lines1/textFiles, lines2/textFiles and lines34567/textFiles directories in report/figures/ directory."

echo "***************"
echo "Press enter to continue"
echo "***************"
read X

cd python/03.koch
./run.sh
mkdir -p ../../report/figures/KSP1/textFiles/ 
cp -r KSP1.txt ../../report/figures/KSP1/textFiles/ 
for i in 2 3 4 5 6 
do
mkdir -p ../../report/figures/KSP2/textFiles/
cp -r KSP${i}.txt ../../report/figures/KSP2/textFiles/
done
cd ../../
echo "***************"
echo "Text files for section 3 are made and copied to KSP1/textFiles and KSP2/textFiles directories in report/figures/ directory."

echo "***************"
echo "Python files are all compiled. Tex files are being compiled."
echo "Press enter to continue"
echo "***************"
read X

cd report/figures/
for i in midpoints iterations lines1 lines2 lines34567 KSP1 KSP2 KSPPgf hexaPgf treePgf
do
cd ${i}
./run.sh
echo "${i}.tex is compiled."
echo "***************"
echo "Press enter to continue"
echo "***************"
read X
cd ../
ln -s -f ${i}/${i}.pdf .
done


echo "***************"
echo "All necessary PDF figures are made."
echo "Main PDF will be generated..."
echo "Press enter to continue"
echo "***************"
read X

cd ../
./run.sh
./clean.sh
cd ../
ln -s -f report/main.pdf TeamX_final_report.pdf

echo "***************"
echo "All done."
echo "The PDF file will be opened."
sleep 4
evince TeamX_final_report.pdf &
echo "Exiting..."
echo "***************"
