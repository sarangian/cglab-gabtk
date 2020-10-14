Genome Assembly Benchmark Toolkit
=================================

installation instruction:
--------------------
git clone https://github.com/sarangian/cglab-gabtk.git

cd cglab-gabtk

./install.sh

Running Genome Assembly Benchmark Toolkit
------------------------------------------
step 1: Export python path
export PYTHONPATH=$PYTHONPATH:/path/to/cglab-gabtk/gabtk

step 2: Get help
python3 -m gabtk --help-all

Available commands::

    configureProject    #creates the luigi configuration file luigi.cfg
    
    rawReadsQC          #fastqc analysis of raw reads
    
    cleanReads	        #processs illumina short reads
    
    cleanLongReads      #filter nanopore or pacbio long reads
    
    correctPAC          #Correct pacbio reads
    
    correctONT          #Correct Nanopore reads
    
    lightAssembler      #Assembly of illumina paired end reads using Light Assembler
    
    sparseAssembler     #Assembly of illumina paired-end reads using Sparse Assembler
    
    discovardenovo      #Assembly of illumina paired-end reads using discovardenovor
    
    spades              #Assembly of (i)   illumina paired-end reads
                                     (ii)  illumina paired-end reads with mate-pair reads
                                     (iii) illumina paired-end reads with nanopore reads
                                     (iv) illumina paired-end reads with pacbio reads
    
    abyss              #Assembly of  (i)   illumina paired-end reads
                                     (ii)  illumina paired-end reads with mate-pair reads
                                     (iii) illumina paired-end reads with nanopore reads
                                     (iv) illumina paired-end reads with pacbio reads
                                     
    
    idba              #Assembly of   (i)   illumina paired-end reads
                                     (ii)  illumina paired-end reads with mate-pair reads
                                     (iii) illumina paired-end reads with nanopore reads
                                     (iv) illumina paired-end reads with pacbio reads
                                     
    ray              #Assembly of    (i)   illumina paired-end reads
                                     (ii)  illumina paired-end reads with mate-pair reads
                                     (iii) illumina paired-end reads with nanopore reads
                                     (iv) illumina paired-end reads with pacbio reads 
                                     
     
    masurca          #Assembly of    (i)   illumina paired-end reads
                                     (ii)  illumina paired-end reads with mate-pair reads
                                     (iii) illumina paired-end reads with nanopore reads
                                     (iv) illumina paired-end reads with pacbio reads
                                     
                                     
    dbg2olc          #Assembly of   illumina paired-end reads with nanopore reads
                     #Assembly of   illumina paired-end reads with pacbio reads
     
    smartdenovo      #Assembly of nanopore long reads or pacbio long reads
    
    wtdbg2           #Assembly of nanopore long reads or pacbio long reads
    
    flye             #Assembly of nanopore long reads or pacbio long reads
    
    canu             #Assembly of nanopore long reads or pacbio long reads
    
    abruijn          #Assembly of nanopore long reads or pacbio long reads
    
    neact            #Assembly of nanopore long reads
    
    meact            #Assembly of pacbio long reads



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

