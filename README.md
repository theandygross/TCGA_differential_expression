
# README

This repository contains all of the analysis notebook required for the reproduction of the manuscript:

[__Analysis of matched tumor and normal profiles reveals common transcriptional and epigenetic signals shared across cancer types__.  ](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0142618)

[Andrew M. Gross](http://andy-gross.flavors.me/), [Jason F. Kreisberg](http://sdcsb.ucsd.edu/about/contact-info-2/), [Trey Ideker](http://healthsciences.ucsd.edu/som/medicine/research/labs/ideker/Pages/default.aspx)

## Analysis 

All analysis for the manuscript is recorded in a series of Jupyter (formerly IPython) Notebooks. 

To view please follow the [Github](https://github.com/theandygross/TCGA_differential_expression/tree/master/Notebooks) or [NBviewer](http://nbviewer.ipython.org/github/theandygross/TCGA_differential_expression/blob/master/Notebooks/Index.ipynb) links.

## Dependencies  

This code uses a number of features in the scientific python stack as well as a small set of standard R libraries. Thus far, this code has only been tested in a Linux enviroment, it may take some modification to run on other operating systems.
I highly recomend installing a scientific Python distribution such as Anaconda or Enthought to handle the majority of the Python dependencies in this project (other than rPy2). These are both free for academic use.

### Python Dependencies 

* [Numpy and Scipy](http://www.scipy.org/), numeric calculations and statistics in Python 
* [matplotlib](http://matplotlib.org/), plotting in Python
* [Pandas](http://pandas.pydata.org/), data-frames for Python, handles the majority of data-structures  
* [rPy2](http://rpy.sourceforge.net/rpy2.html), communication between R and Python  
  * __NOT IN DISTRIBUTIONS__  
  * I recommend installing with `pip install rpy2`  
  * Needs R to be compiled with shared libraries  

### My Internal Package Dependencies

These are Python packages that I use internally for things such as statistics and visualization. They are all available on [my Github page](https://github.com/theandygross), I recomend downloading them and installing them with `python setup.py install`.  I appoligize for the generic names, I am hoping to develop these a bit more and make them into proper packages up to spec in my next code refactor.   

* [Figures](https://github.com/theandygross/Figures) 
  * Code for better figure generation, mainly using Pandas data-structures 
  * I am slowly phasing this out and replacing with the very nice [seaborn](http://stanford.edu/~mwaskom/software/seaborn/index.html) library  
  
* [Stats](https://github.com/theandygross/Stats)  
  * Contains two packages, __Stats__ and __Helpers__ 
  * __Stats__ has a number of helper functions that wrap calls to R or scipy statistics functions and allow them to play nicer with Pandas data-structures  
  * __Helpers__ has a number of common tasks that I envoke to make code a bit more readable 
  
* [NotebookImport](https://github.com/theandygross/NotebookImport) 
  * Utility for importing IPython notebooks as modules
  * Code taken from [MinRK's Gist](http://nbviewer.ipython.org/gist/minrk/6011986) 
  * This is dependent on the IPython/Jupyter version you are using, you may get deprecation warnings, I am trying to keep this up to date but I'm not sure how backwards compatable things are
  
* [MethylTools](https://github.com/theandygross/MethylTools)
  * Utility for organizing probe annotations for the Illumina methylation450k chip 
  * Has some R dependencies

### R Dependencies 
* [IlluminaHumanMethylation450kanno.ilmn12.hg19](http://bioconductor.org/packages/release/data/annotation/html/IlluminaHumanMethylation450kanno.ilmn12.hg19.html)
    * Used for methylation probe annotations 
    * Should only be a dependency for the MethylTools package
* [mgsa](http://www.bioconductor.org/packages/release/bioc/html/mgsa.html) 
    * Model based GSEA  
    * I don't use this in the paper but it is in some exploritory analysis
