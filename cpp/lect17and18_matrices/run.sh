file=$1
gcc $file -o a.out
./a.out
rm -r a.out
echo "$1 has been compiled and ran"