file=KristianTuv.csv
while read line ; do
    username=$( echo "$line" |cut -d',' -f3 )
    echo $( git clone https://github.com/UiO-INF3331/INF3331-$username )
done < ${file}
