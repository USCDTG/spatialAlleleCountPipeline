# Spatial Allele Count Pipeline v0.1.0
04-22-2021             

#### Pre-processing pipeline for the spatialLOH R package
### Overview


![alt text](https://github.com/USCDTG/spatialAlleleCountPipeline/blob/main/images/preProcessingPipeline.png)


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
3. **dbSNP** https://www.ncbi.nlm.nih.gov/snp/
4. **SnpEff:** https://pcingola.github.io/SnpEff/        


## Contact   
Michelle Webb           
michelgw@usc.edu
