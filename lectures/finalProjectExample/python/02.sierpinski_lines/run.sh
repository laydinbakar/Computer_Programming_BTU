for j in 1 2 3 4 5 6 7 8
do 
python3 gen_sierpinski_lines.py -i ${j}
echo "lines${j}.txt is written."
done
