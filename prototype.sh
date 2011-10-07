MYDIR=$(dirname $0)
PROT=$1-prototype.tar.gz

if [ -f $MYDIR/prototypes/$PROT ]
then
	cp $MYDIR/prototypes/$PROT .
	tar xzf $PROT
	mv $1 $2
	rm $PROT
else
	echo "No such prototype: $1"
fi
