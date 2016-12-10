
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import sys

# %matplotlib inline


# In[2]:

filename = sys.argv[1]
# Usage:
# python gc_gene_plot.py myfile
# filename = "myfile"
print("You are analyzing file:")
print(filename)

human_chr21 = pd.read_table(filename, sep ='\t')
human_chr21


# In[13]:

human_chr21['gc_content'] = human_chr21['gc_bases'] /    (human_chr21['win_end'] - human_chr21['win_start'])

human_chr21['gene_content'] = human_chr21['exon_bases'] /    (human_chr21['win_end'] - human_chr21['win_start'])


# In[11]:

plt.plot(human_chr21['gc_content'], human_chr21['gene_content'], 'o')
plt.xlabel('GC content')
plt.ylabel('Gene content')
# plt.show()
plot_file_name = filename + '.plot.png'
plt.savefig(plot_file_name)

