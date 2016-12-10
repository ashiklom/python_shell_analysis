
# Python script for plotting gene data
# Author: Alexey Shiklomanov
# Email: alexey.shiklomanov@gmail.com

import pandas as pd
import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]

# Usage:
# python gc_gene_plot.py myfile
# filename = "myfile"

print("You are analyzing file:")
print(filename)

human_chr21 = pd.read_table(filename, sep ='\t')
human_chr21

human_chr21['gc_content'] = human_chr21['gc_bases'] /    (human_chr21['win_end'] - human_chr21['win_start'])

human_chr21['gene_content'] = human_chr21['exon_bases'] /    (human_chr21['win_end'] - human_chr21['win_start'])

plt.plot(human_chr21['gc_content'], human_chr21['gene_content'], 'o')
plt.xlabel('GC content')
plt.ylabel('Gene content')
# plt.show()
plot_file_name = filename + '.plot.png'
plt.savefig(plot_file_name)

