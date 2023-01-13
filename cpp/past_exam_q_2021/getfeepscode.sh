FILENAME=$1
wget http://www.soton.ac.uk/~rpb/feeg6002/code/c/$FILENAME
gcc $FILENAME -o out
./out
rm -r out
echo your codes have been saved
