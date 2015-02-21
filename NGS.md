##Set-up: 
Install/download samtools (1.2), bwa, picard (sourceforge version), GATK + Java 7, Ensembl VEP, and SnpEFF
You'll need a computer that can run UNIX and over 50 GB of hard disk space (+ a fast internet connection makes things way better)
Note: for downloading files from broad use the following 
```
$ftp ftp.broadinstitute.org
username: gsapubftp-anonymous
pass: your email
```

##Pair-end Sequence Assembly
```
#construct an index of reference genome
$bwa index -a bwtsw reference.fasta 
#build sequence alignment indices of raw fastq files
$bwa aln reference.fasta short_pair_1.fastq > short_pair_1.sai
$bwa aln reference.fasta short_pair_2.fastq > short_pair_2.sai
#combine reference index, the two alignment indices and two pair end raw fastq files to create a single sequence alignment map. 
$bwa sampe reference.fasta short_pair_1.sai short_pair_2.sai short_pair_1.fastq short_pair_1.fastq > short_pair.sam
#next need to change "*" to "o" as a flag for unaligned reads, ajust mate pair info and add read headers 
$java -Xmx[memory]g -jar ValidateSamFile.jar I=[.bam or .sam]
#displays MAPQ flag error, mate-pair error, and header error
$java -Xmx[memory]g -jar FixMateInformation.jar I=[.bam] O=[.bam] VALIDATION_STRINGENCY=LENIENT
#requires significant scratch disk space, recommend utilizing $ -Djava.io.tmpdir = /scratch_directory
TMP_DIR=/scratch_directory
$java -Xmx[memory]g -jar ValidateSamFile.jar I=[fixed.bam] IGNORE=INVALID_MAPPING_QUALITY
#validate file accepting MAPQ flag “*”
$java -Xmx[memory]g -jar AddOrReplaceReadGroups.jar I=[.bam] O=[.bam]
LB=anything PL=illumina PU=anything SM=anything
#re-sort the picard output
#you now get an unsorted sam file which has to be converted to binary and sorted using samtools
$ samtools view -bS -o [output.bam] [input.sam]
$ samtools sort [input.bam] [output.sorted]
```

###Viewing the bam file
```
$samtools tview file.bam
#if it is white, when you press n you get colors
```

##The VCF file
```
#generating the VCF
$./samtools mpileup -ugf [reference.fasta]  [sorted.bam] |./bcftools/bcftools call -vmO z -o [output.vcf.gz] 

#preparing the reference
$bwa index -a bwtsw reference.fa
$samtools faidx reference.fa #creates reference.fa.fai
#run picard comand to create reference dictionary 
$java -jar CreateSequenceDictionary.jar -REFERENCE=reference.fa -OUTPUT=reference.dict

#running variant annotator (GATK), need to have a dbsnp in addition to the generated vcf 
$java -Xmx[memory]g -jar GenomeAnalysisTK.jar -R [ref.fasta] -T VariantAnnotator -o [output.vcf] --variant [input.vcf] --dbsnp [dbsnp.vcf]

#running variant filtration: using 4 filters (low, mid, high, Xtreme) 
$java -Xmx[memory]g -jar GenomeAnalysisTK.jar    -R [reference.fasta]    -T VariantFiltration    -o [output.vcf] --variant [input.vcf]   --filterExpression "DP > 10 && DP < 25" --filterName "low" --filterExpression "DP > 25 && DP < 50" --filterName "mid" --filterExpression "DP > 50 && DP < 150" --filterName "high" --filterExpression "DP > 150" --filterName "Xtreme" 
#creating an additional filter for variants that don't even meet the low criterium 
$java -Xmx[memory]g -jar GenomeAnalysisTK.jar    -R [reference.fasta]    -T VariantFiltration    -o [output.vcf] --variant [input.vcf]    --filterExpression "DP < 10" --filterName "PASS"
```
###Troubleshooting 
If you can't run variant annotator because the variant contigs are not the same as the reference contigs run the following (with picard 1.121 or greater)
```
$java -Xmx2g -jar picard.jar SortVcf INPUT=[input.vcf] OUTPUT=[output.vcf] SEQUENCE_DICTIONARY=[reference.fasta]
```
Then you might have to edit the output vcf and remove the #contigs from the header. You can do this from the terminal using vim
```
$vim [filename]
#to quit and save use Esc+shift, Shift+Z, Shift+Z
```

###Functional predictions 
####Method 1: SnpEFF w/ GATK
```
$java -Xmx4G -jar snpEff.jar  -c snpEff.config -v -o gatk hg19 [input.vcf] > [output.snpeff.vcf] 
#sample output http://materechm.github.io/Bioinformatics/snpEFF_summary.html (plus a vcf)
$java -Xmx4g -jar GenomeAnalysisTK.jar -T VariantAnnotator -R [ref.fasta] -A SnpEff --variant [input.vcf (same input than the last algorithm)] --snpEffFile [input.snpeff.vcf] -L [input.vcf] -o [input.gatk.vcf] 
```
####Method 2: Ensembl VEP
```
#go to the directory where you have VEP, cd to scripts/variant_effect_predictor/
$perl INSTALL.pl
#when it asks if you want to create the .vep folder and download cached files put y, download homo_sapiens_vep_78_GRCh38.tar.gz

```

###Figuring out how many variants you have
```
#total variants (approximation)
$grep -v -c "#" [yourfile.vcf]
#by filter
$grep "filterName" [filtered.vcf] | wc -l

```
