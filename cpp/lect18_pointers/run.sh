file=$1
gcc $file -o a.out
./a.out
rm -r a.out
echo "\n"
echo "$1 has been complied and executed"
echo "\n"