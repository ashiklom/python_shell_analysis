# Add header to chromosome gene data
# Author: Alexey "bash man" Shiklomanov
# Last modified: Sat Dec 10, 2016
# For questions, contact <alexey.shiklomanov@gmail.com>

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

