#!/bin/bash
#want to get a first guess for MOOG
#basically do a grid of models to find ones where FeI/H and FeII/H are close
#gives a starting point, but isn't as close as you would assume
#does not look at trends like EP and EW, only the difference between FeI and FeII
password=temp
cd /Users/christinagilligan/moog17scat-master
rm output.txt
for FEH in `seq -2.49 0.1 0.49`; do
#for FEH in -2.49; do
	sshpass -f <(printf '%s\n' $temp) ssh gilligan@polaris.dartmouth.edu <<- EOF
	cd /afs/northstar/users/g/gilligan/abund/teff.rm05
	rm temperature.txt
	./teffvk2_dwarf.e >> temperature.txt <<- EO
#V-K color has to change	
	1.838
	$FEH
	EO
	EOF
	sshpass -f <(printf '%s\n' $temp) scp gilligan@polaris.dartmouth.edu:/afs/northstar/users/g/gilligan/abund/teff.rm05/temperature.txt .
	TEMP=5239
#make a python script that reads this temperature value and finds the correct isochrone and gets a value for logg
	python ~/isochroneLogG.py $FEH $TEMP> templogg.txt
#	TEMP=$(awk 'NR==1' templogg.txt)
	LOGG=$(awk 'NR==2' templogg.txt)
	MICRO=1.0
#make kurucz model
	sshpass -f <(printf '%s\n' $temp) ssh gilligan@polaris.dartmouth.edu <<- EOF
	cd /afs/northstar/users/g/gilligan/abund/makekurucz
	echo $TEMP $LOGG $FEH $MICRO
	./makekurucz3.e <<- EO
	$TEMP $LOGG $FEH $MICRO
	AODFNEW
	EO
	EOF
	sshpass -f <(printf '%s\n' $temp) scp gilligan@polaris.dartmouth.edu:/afs/northstar/users/g/gilligan/abund/makekurucz/MODEL .
#run MOOGSILENT
#have to create the par file beforehand
	./MOOGSILENT <<- EO
	TYC9131-1075-1.par
	EO
#run abundance calculation
	echo $FEH $TEMP $LOGG>> output.txt
	python abundanceCalcNoGraph.py >> output.txt
done
#better to do metal rich ones in ODFNEW
for FEH in `seq -0.99 0.1 0.49`; do
	sshpass -f <(printf '%s\n' $temp) ssh gilligan@polaris.dartmouth.edu <<- EOF
	cd /afs/northstar/users/g/gilligan/abund/teff.rm05
	rm temperature.txt
	./teffvk2_dwarf.e >> temperature.txt <<- EO
	1.838
	$FEH
	EO
	EOF
	sshpass -f <(printf '%s\n' $temp) scp gilligan@polaris.dartmouth.edu:/afs/northstar/users/g/gilligan/abund/teff.rm05/temperature.txt .
#make a python script that reads this temperature value and finds the correct isochrone and gets a value for logg
	TEMP=5239
	python ~/isochroneLogG.py $FEH $TEMP> templogg.txt
	#TEMP=$(awk 'NR==1' templogg.txt)
	LOGG=$(awk 'NR==2' templogg.txt)
	MICRO=1.0
#make kurucz model
	sshpass -f <(printf '%s\n' $temp) ssh gilligan@polaris.dartmouth.edu <<- EOF
	echo ‘got here instead’
	cd /afs/northstar/users/g/gilligan/abund/makekurucz
	./makekurucz3.e <<- EO
	$TEMP $LOGG $FEH $MICRO
	ODFNEW
	EO
	EOF
	sshpass -f <(printf '%s\n' $temp) scp gilligan@polaris.dartmouth.edu:/afs/northstar/users/g/gilligan/abund/makekurucz/MODEL .
#run MOOGSILENT
#have to create the par file beforehand
	./MOOGSILENT <<- EO
	TYC9131-1075-1.par
	EO
#run abundance calculation
	echo $FEH $TEMP $LOGG>> output.txt
	python abundanceCalcNoGraph.py >> output.txt
done
