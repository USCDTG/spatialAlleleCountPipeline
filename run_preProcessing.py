# AC Tool - 0.1.0
# Functions file needs to be adjacent in directory
from functions_ac import getVCFPos, runAC
import argparse
import sys
parser = argparse.ArgumentParser(description='Filter Germline VCF for Heterozygous Positions and Obtain Allele Counts for Bayes Factor Calculations')
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
parser.add_argument('-b','--bamList', help='a file containing full paths to per-cluster BAMs')
parser.add_argument('-s','--sampleList', help='a file containing sample and cluster names in the format sample_cluster1')
parser.add_argument('-v','--vcf', help='full path to HaplotypeCaller snpEff Annotated VCF')
parser.add_argument('-o','--outputDir')
args = parser.parse_args()

bamListFile = args.bamList
sampleNameFile = args.sampleList
vcf = args.vcf
output = args.outputDir

with open(bamListFile) as f:
  bamList = [line.rstrip('\n') for line in f]
  f.close()
print(bamList)
with open(sampleNameFile) as f:
  sampleList = [line.rstrip('\n') for line in f]
  f.close()

print("## AC Tool - version 0.0.1")
chr1, start1, stop1, df1 = getVCFPos(vcf)

[runAC(a,b,chr1,start1,stop1,df1,output) for a,b in zip(bamList,sampleList)]
print("## AC Tool - Complete")
