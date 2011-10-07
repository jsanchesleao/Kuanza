PROT=$1-prototype.tar.gz

if [ -f $START_POINT_HOME/prototypes/$PROT ]
then
	cp $START_POINT_HOME/prototypes/$PROT .
	tar xzf $PROT
	mv $1 $2
	rm $PROT
else
	echo "No such prototype: $1"
fi
