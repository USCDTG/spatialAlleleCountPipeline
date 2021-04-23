## Author: Michelle Webb
## Functions File for tLOH pre-processing pipeline
from pysam import VariantFile
import pysam
import pandas
import os

def getVCFPos(vcf):
  print("Reading VCF")
  vcf_in = VariantFile(vcf)
  print("Parsing VCF")
  df = pandas.DataFrame([rec.chrom.replace("chr", ""),rec.chrom,rec.pos,rec.pos-1,rec.id,rec.qual,rec.ref,rec.alts[0],rec.info['ANN'],rec.info['AF'][0],rec.samples[0].items()[0]] for rec in vcf_in.fetch() if rec.qual > 500 and rec.id is not None and len(rec.alts[0]) == 1 and len(rec.ref) == 1 and 0.4 < rec.info['AF'][0] < 0.6)
  df.columns =['CONTIG','CHR','POSITION','POSITION_oneBefore','rsID','QUAL','REF','ALT','INFO','vcfAF','Genotype']
  chr = df['CONTIG'].tolist()
  start = df['POSITION_oneBefore'].tolist()
  stop = df['POSITION'].tolist()
  vcf_in.close()
  return chr, start, stop, df

### Assumptions: BAMs are split by cluster
def runAC(bam,sample,chr,start,stop, df,output):
  print("Count Coverage")
  print("Reading BAM")
  samfile = pysam.AlignmentFile(bam,"rb")
  df_2 = pandas.DataFrame([samfile.count_coverage(contig = a, start = b, stop = c)] for a,b,c in zip(chr,start,stop))
  nucleotides = pandas.DataFrame([x[0][0],x[1][0],x[2][0],x[3][0]] for x in df_2[0].tolist())
  nucleotides.columns = ['A','C','G','T']
  print("Merging")
  final = pandas.merge(df,nucleotides,how='outer',left_index=True, right_index=True)
  print("Loops")
  index = 0
  refCOUNT = []
  for value in final['REF']:
    try:
        refCOUNT.append(final[value][index])
        index += 1
    except KeyError:
        refCOUNT.append("NA")
        index += 1
  index = 0
  altCOUNT = []
  for value2 in final['ALT']:
    try:
        altCOUNT.append(final[value2][index])
        index += 1
    except KeyError:
        altCOUNT.append("NA")
        index += 1
  final['REF_COUNT_CALC'] = refCOUNT
  final['ALT_COUNT_CALC'] = altCOUNT
  final['barcode'] = sample
  final.to_csv('%s/%s_alleleCounts.csv' % (output, sample), index=False)
  samfile.close()
