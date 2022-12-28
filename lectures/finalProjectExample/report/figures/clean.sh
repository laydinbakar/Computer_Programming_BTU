for i in KSP1 KSP2 lines1 lines2 iterations midpoints
do
cd ${i}
rm -rf *.aux *.log
cd ..
done

for i in KSPPgf hexaPgf treePgf
do
cd ${i}
rm -rf *.aux *.log
cd ..
done

find -type l -delete
