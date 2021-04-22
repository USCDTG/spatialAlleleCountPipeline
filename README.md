# Spatial Allele Count Pipeline v0.1.0
04-22-2021             

#### Pre-processing pipeline for the spatialLOH R package
### Overview


![alt text](https://github.com/USCDTG/spatialAlleleCountPipeline/blob/main/images/preProcessingPipeline_overview.png)


## Before Analysis

Process spatial transcriptomics FASTQs through the 10X Genomics spaceranger pipeline<sup>1</sup> with GRCh38 reference. Obtain a sample binary alignment map (BAM) file and a clusters.csv file containing the header line **barcode**,**cluster**.
#### BAM Split
Split the spatial BAM into per-cluster BAMs.

#### VCF File
Obtain a variant call format (VCF) file with likely heterozygous single-nucleotide polymorphism (SNP) positions. If there is companion exome data for your sample, run GATK HaplotypeCaller<sup>2</sup> and SnpEff<sup>3</sup> on an aligned BAM file with a dbSNP<sup>4</sup> database VCF for annotation. Use the snpEff -canon option to output just the canonical transcript for each SNP.

## Analysis
Save all cluster BAMs associated with a single sample in a directory. Create a file with full paths to these files for **run\_preProcessing.py** (one file per line). Create another file with sample names in format Sample1\_Cluster1, Sample2\_Cluster2 (one sample per line).


**Setup Conda Environment:**

```
conda create -n myEnv python=3.6
conda activate myEnv
conda config --add channels r
conda config --add channels bioconda
conda install -c bioconda pyranges
conda install pysam==0.15.4
conda install numpy==1.17.0
conda install pandas==1.1.5
```

**Run pipeline:**


``python run_preProcessing.py --bamList fileContainingBAMpaths.txt --sampleList fileContainingSampleNames.txt --vcf snpEff_Annotated_HaplotypeCaller.vcf --outputDir /path/to/outputDir``

## Dependencies           
**Python:**  
Tool optimized for python version 3.6      
pyranges   
numpy     1.17.0   
pandas   1.1.5     
pysam   0.15.4     

## References
1. **10X Genomics Spaceranger Pipeline:** https://support.10xgenomics.com/spatial-gene-expression/software/pipelines/latest/what-is-space-ranger
2. **HaplotypeCaller:** https://gatk.broadinstitute.org/hc/en-us/articles/360037225632-HaplotypeCaller
	- Van der Auwera GA & O'Connor BD. (2020). Genomics in the Cloud: Using Docker, GATK, and WDL in Terra (1st Edition). O'Reilly Media.
3. **dbSNP** https://www.ncbi.nlm.nih.gov/snp/
	- Sherry,S.T., Ward,M. and Sirotkin,K. (1999) dbSNP—Database for Single Nucleotide Polymorphisms and Other Classes of Minor Genetic Variation. Genome Res., 9, 677–679.
4. **SnpEff:** https://pcingola.github.io/SnpEff/  
	- "A program for annotating and predicting the effects of single nucleotide polymorphisms, SnpEff: SNPs in the genome of Drosophila melanogaster strain w1118; iso-2; iso-3.", Cingolani P, Platts A, Wang le L, Coon M, Nguyen T, Wang L, Land SJ, Lu X, Ruden DM. Fly (Austin). 2012 Apr-Jun;6(2):80-92. PMID: 22728672      




## Contact   
Michelle Webb           
michelgw@usc.edu
