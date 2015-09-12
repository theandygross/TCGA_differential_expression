
# Notebook Directory

### File paths 

File paths are stored in the [Global_Parameters](./Global_Parameters.ipynb) Notebook.

### Setup and Processing 

Data setup and processing are generally handled in the Preprocessing directory. Note that the data pipeline depends on data being downloaded from the [Broad Firehose website](http://gdac.broadinstitute.org/) and organized in a specific file structure.  

The code for downloading and organizing these datasets is available in my [CancerData](https://github.com/theandygross/CancerData) repository. The specific notebook doing the download is available [here](https://github.com/theandygross/CancerData/blob/master/Notebooks/Download_From_Firehose.ipynb).  

I apologize for the dependency hell, and will try and simplify this in the near future if possible. If you run into issues, please feel free to send me an email. 

To initialize the data run the Notebooks in the following order:


### Imports and Globals  
* [Global_Parameters](Global_Parameters.ipynb) this is used to store all of the hard paths being used throughout the analysis. You should manually edit this file to point to where your data is stored locally.
* [Imports](./Imports.ipynb) import some commonly used data and functions into the Python enviroment. This is used to avoid muddying up analysis files with boilerplate import and functions. I generally load everything in the notebook globally by importing it (this requires first loading the [NotebookImport package](https://github.com/theandygross/NotebookImport)).  
* [GTEX](./GTEX.ipynb) Downloads and handles tissue-specific expression data from the GTEX project. 

### Initial fraction upregulated screen 

* [DX_screen.ipynb](./DX_screen.ipynb) is where the fraction upregulated statistic is calculated. 
* [GSEA_fraction_upregulated_expression](./GSEA_fraction_upregulated_expression.ipynb) GSEA on the rna sequencing datasets. 
* [methylation_upregulated_probe_annotation](./methylation_upregulated_probe_annotation.ipynb) exploration of probe and gene-set annotations for fraction upregulated on methylation450k data.

### Proliferation signature and detrended fraction-upregulated 
* [metaPCNA](./metaPCNA.ipynb) calculation of meta-PCNA proliferation score and analysis of proliferation in paired mRNA expression dataset. 
* [switchiness_screen](./switchiness_screen.ipynb) analysis and gene set enrichment for detrended fraction upregulated statistic on mRNA sequencing data. 
* [switchiness_miR](./switchiness_miR.ipynb) analysis for detrended fraction upregulated statistic on microRNA sequencing data. 
* [switchiness_methylation](./switchiness_methylation.ipynb) analysis for detrended fraction upregulated statistic on methylation450k data. 

### Microarray datasets 
For the microarray data, I manually downloaded the series matrix files from GEO. There are links to each datasets in the notebooks, or you can look them up fairly eaisily from the accession codes. You are going to want to point to where you store these .txt files using the __MICROARRAY_PATH__ variable, which is set in the [Global_Parameters](Global_Parameters.ipynb) notebook.  
* [microarray_validation_data](./microarray_validation_data.ipynb) reads in and calculates fraction upregulated on all microarray datasets. Assumes data and mapping files are already downloaded and placed in MICROARRAY_PATH. 
* [microarray_validation_aggregation](./microarray_validation_aggregation.ipynb) reads in microarray data from MICROARRAY_STORE and looks at concordinance of fraction upregulated in pooled microarray data and pooled TCGA rna-sequencing data. 
* [microarray_validation_aggregation_GABA](./microarray_validation_aggregation_GABA.ipynb) targeted analysis of GABA receptors and GABRD specifically in the validation microarray datasets. 

### Targeted Followup 
This is where I dig into specific results. There are a bunch of other attempts at this that did not make the cut in the Exploratory folder. 
* [GABA_Receptors](./GABA_Receptors.ipynb) exploration of GABA receptor subunits. 
* [GABA_Receptors_GTEX](./GABA_Receptors_GTEX.ipynb) looks at tissue specific expression of GABA subunits in healthy tissue using the GTEX dataset.


```python

```
