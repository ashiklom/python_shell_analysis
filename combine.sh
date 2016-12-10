# Add header to chromosome gene data
# Author: Alexey "bash man" Shiklomanov
# Last modified: Fri Dec 9, 2016
# For questions, contact <ashiklom@bu.edu>

echo "Starting combining script"
for file in "$@"
do
	# Cool trick from Michelle -- combine files
	echo '$file'
	echo "$file"
	cat raw/header.txt "$file" > processed/$file
done

# echo "Switching into new directory"
# cd processed

# for input in *.txt
#do
#	echo "Analyzing $input ..."
#	python gc_gene_plot.py $input
#done
#echo "Done!"

