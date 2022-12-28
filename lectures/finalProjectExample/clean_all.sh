#!/usr/bin/env zsh

echo "This is Team-X Final Project repository."
echo "***************"
echo "Team members are:"
echo "# ID Name Surname"
echo "1 1234567890 Levent Aydinbakar"
echo "2 1234567890 Levent Aydinbakar"
echo "***************"
echo "Press enter to clean all unnecessary files."
echo "***************"
read X

cd python/01.sierpinski_points
rm -rf *.txt
cd ../../

cd python/02.sierpinski_lines
rm -rf *.txt
cd ../../

cd python/03.koch
rm -rf *.txt
cd ../../

cd report/figures/
for i in midpoints iterations lines1 lines2 lines34567 KSP1 KSP2 KSPPgf hexaPgf treePgf
do
cd ${i}
rm -rf *.pdf textFiles
cd ../
find -type l -delete
done

cd ../
./clean.sh
cd ../

echo "***************"
echo "All unnecessary files are removed."
echo "To reproduce the report, run run_all.sh ."
echo "Exiting..."
