for j in 10 100 1000 2000 5000
do 
python3 gen_sierpinski_points.py -i ${j}
echo "sierpinskiPoints${j}.txt is written."
done
