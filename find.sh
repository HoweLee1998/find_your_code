ls *R | while read id
do
a='WGCNA'
b=`cat ${id} | grep $a`
if [ ! -z "$b" ];then
    echo ${id}
    echo $b
    echo "\n"
fi
done