Genome Assembly Benchmark Toolkit
=================================

installation instruction:
--------------------
git clone ______

cd cglab-gabtk

./install.sh

Running Genome Assembly Benchmark Toolkit

step 1: Export python path
export PYTHONPATH=$PYTHONPATH:/path/to/cglab-gabtk/gabtk

step 2: Get help
python3 -m gabtk --help-all

Available commands:
1. configureProject             #creates the luigi configuration file luigi.cfg
2: rawReadsQC			#fastqc analysis of raw reads
3: cleanReads			#processs illumina short reads
4: cleanLongReads               #filter nanopore or pacbio long reads
5: correctPAC			#Correct pacbio reads
6: correctONT	                #Correct Nanopore reads

Paired-end only Assemblers
1. lightassembler
2. sparseassembler
3. discovardenovo

Hybrid Assemblers (paired-end with mate-pair  or paired-end with long-reads)
1. spades
2. ray
3. idba_ud
4. abyss
5. smartdenovo
6. soapdenovo
7. dbg2olc

long read  assemblers
1. flye
2. canu
3. necat
4. mecat2
5. masurca
6. abruijn
7. wtdbg2
8. miniasm


A. paired-end only assembler

1. python3 benchmark.py lightAssembler --help 

  --seq-platforms             #optional, default: pe
  
  --pre-process-reads         #Choices: {yes, no}
  
  --kmer                      #Minimal Kmer Length for assembly. [--kmer 31]

