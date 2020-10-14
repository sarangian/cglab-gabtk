
.. _commands:

Commands
========

.. toctree::
   :hidden:


Prepare Prpject
------------------

To design and perform a RNASeq experiment, a Project need to be prepaired using the ``prepareProject.py`` script. Conda environment mest be activated before running the script.

Usage:  prepareProject.py -h


.. code-block:: none

    prepareProject.py <arguments>
    -h       --help             show this help message and exit

    mandatory arguments         Description
    
    -f      --fastqDir          Path to Directory containing raw RNASeq reads
                                type: string
                                Example: $HOME/bulkRNASeqPIPE/sample_data/mastigocladus_rnaseq

    -x      --fileExtention     extensions for a FASTQ files. 
                                type: string
                                allowed values: [fq, fq.gz, fastq, fastq.gz]

    -r      --readType          RNASeq read type 
                                type: string
                                allowed values: [single, paired]

    -d      --domain            Organism Domain
                                type: string
                                allowed values: [prokaryote, eukaryote]

    -a      --adapterFile       Path to adapter file
                                type: string
                                example: $HOME/bulkRNASeqPIPE/utility/adapter.fasta.gz

    -o      --organismName      Organims Name 
                                Must not contain blank spaces and (or) special characters
                                type: string
                                example: MLA_UU774


    -g      --genomeDir         Path to Directory containing genome FASTA (.fna) and 
                                genome annotation (.gff / .gtf ) files 
                                type: string
                                example: $HOME/bulkRNASeqPIPE/sample_data/mastigocladus_genome


    Optional arguments
    ------------------
    -p     --projectName        Name of the Project Directory to be created
                                Must not contain blank spaces and (or) special characters
                                type: string
                                Default: MyProject

    -s     --schedulerPort      Scheduler Port Number for luigi
                                type: int
                                Default: 8082

    -e     --emailAddress       Provide your email address
                                type: string
                                Default: Null

    -c     --threads            Number of threads to be used
                                type: int
                                Default = (total threads -1)

    -m     --maxMemory          Maximum allowed memory in GB. 
                                type: int
                                Default = [(available memory in GB) -1)
    

**Run**

.. code-block:: none

   prepareProject.py  -f /path/to/bulkRNASeqPIPE/sample_data/mastigocladus_rnaseq/ \
                      -x fastq.gz \
                      -r paired \
                      -d prokaryote \
                      -a /path/to/bulkRNASeqPIPE/utility/adapters.fasta.gz \
                      -g /path/to/bulkRNASeqPIPE/sample_data/mastigocladus_genome/ \
                      -o UU774 \
                      -p mastigocladus \
 

**Output**

|   Successful run of the prepareProject.py script with appropriate parameters will generate 
|
|   1. Luigi Configuration file ``luigi.cfg`` in the parent folder
|
|   2. a project folder in the name of ``mastigocladus`` containing three files 
|      a. group.tsv
|      b. samples.txt
|      c. target.tsv
|
|   The ``target.tsv`` file contains the sample names with their associated biological conditions, which will be used for differential expression analysis 
|  
|


Commands to run BulkRNA-Seq Workflow
------------------------------------

.. code-block:: none

    Command                      Description   
    
    1. rawReadsQC                   Raw Reads Quality Assessment using FASTQC tool  
    2. preProcessSamples            Process Raw Reads using BBDUK

    3. quantifyTranscripts          Quantify transcripts using salmon (or) kallisto
    4. transcriptomeBasedDEA        Transcriptome based differential expression analysis
    
    5. mapReadsToGenome             Map RNASeq reads to the genome (organismName.fna) of the organism
    6. genomeGuidedTransAssembly    Genome Guided Transcript Assembly using Trinity 
    7. mapReadToGGTansript          Map RNASeq reads to the assembled transcriptome using genome-guided approach
    8. clusterGGTranscripts         Clustred assembled transcripts using genome-guided approach
    9. genomeGuidedDEA              Genome guided transcriptome differential expression analysis
 

   10. generateCounts               Generates gene counts from .bam files using featureCount tool
   11. genomeBasedDEA               Genome alignment based differential expression analysis

   12. denovoTransAssemble          Denovo Assembly of Prokaryotic and Eukaryotic Transcripts
   13. quantifyAssembledTranscripts Quantify denovo assembled transcripts using Salmon 
   14. clusterContigs               Clustred Assembled transcripts based on equivalence class
   15. denovoDEA                    denovo transcriptome assembly based differential expression analysis



2. Raw reads quality assessment
--------------------------------

|  **Note**
|    Before running any of the BulkRNA-Seq Workflow commands, a project must be prepared using ``prepareProject.py`` script.
|    The parent forlder must have the luigi.cfg file, in which the globalparameters are defined.
|    Running any of the  BulkRNA-Seq Workflow commands without generating the project folder will give rise to ``luigi.parameter.MissingParameterException``
|

.. code-block:: none

    **Steps**
    1. Run Prepare Projcet with project name mastigocladus as discussed before 
       and inspect the samples.txt file generated inside mastigocladus folder

    2. Run rawReadsQC
       rnaseq-wf.py rawReadsQC --local-scheduler

    **Output**
          |-- luigi.cfg
          |-- mastigocladus
          |   |-- group.tsv
          |   |-- QCReports
          |   |   `-- paired_FastQC-RawReads
          |   |       |-- 74_nitro_nm_d12_A_R1_fastqc.html
          |   |       |-- 74_nitro_nm_d12_A_R1_fastqc.zip
          |   |       |-- 74_nitro_nm_d12_A_R2_fastqc.html
          |   |       |-- 74_nitro_nm_d12_A_R2_fastqc.zip
          |   |       |-- 74_nitro_nm_d12_B_R1_fastqc.html
          |   |       |-- 74_nitro_nm_d12_B_R1_fastqc.zip
          |   |       |-- 74_nitro_nm_d12_B_R2_fastqc.html
          |   |       |-- 74_nitro_nm_d12_B_R2_fastqc.zip
          |   |       |-- 74_nitro_np_d12_A_R1_fastqc.html
          |   |       |-- 74_nitro_np_d12_A_R1_fastqc.zip
          |   |       |-- 74_nitro_np_d12_A_R2_fastqc.html
          |   |       |-- 74_nitro_np_d12_A_R2_fastqc.zip
          |   |       |-- 74_nitro_np_d12_B_R1_fastqc.html
          |   |       |-- 74_nitro_np_d12_B_R1_fastqc.zip
          |   |       |-- 74_nitro_np_d12_B_R2_fastqc.html
          |   |       `-- 74_nitro_np_d12_B_R2_fastqc.zip
          |   |-- samples.txt
          |   `-- target.tsv
          `-- workflow.complete.20200105.163458

      Successful execution of rawReadsQC will generate a folder mastigocladus/QCReports/paired_FastQC-RawReads
      which contains the FASTQC reports of the raw fastq files




3. Raw samples quality control
------------------------------
Quality control analysis of the raw samples can be done using command ``preProcessSamples``

|  **Requirements**
|  1. Exexution of prepareProject.py command 
|  2. Availability of ``luigi.cfg`` file in ``parent folder`` and ``samples.txt`` inside the ``project folder``.
|
.. code-block:: none                                      

   rnaseq-wf.py preProcessSamples <arguments> --local-scheduler
    
    arguments               type      description
      

    --bbduk-Xms             int       Initial Java heap size in GB 
                                      Example: 10
                                      Default: 2

    --bbduk-Xmx             int       Maximum Java heap size in GB
                                      Example: 40
                                      Default: 20

    --bbduk-kmer            int       Kmer length used for finding contaminants
                                      Examle: 13  
                                      Default: 11                     

    --bbduk-minL            int       Minimum read length after trimming
                                      Example: 50
                                      Default:50

    --bbduk-trimF           int       Number of bases to be trimmed from the front of the read
                                      Example: 5
                                      Default: 0

    --bbduk-trimT           int       Number of bases to be trimmed from the end of the read
                                      Example: 5
                                      Default: 0

    --bbduk-minAQ           int       Minimum average quality of reads
                                      Reads with average quality (after trimming) below 
                                      this will be discarded
                                      Example: 15
                                      Default: 10

    --bbduk-minGC           float     Minimum GC content threshold
                                      Discard reads with GC content below minGC
                                      Example: 0.1 
                                      Default: 0.0

    --bbduk-maxGC           float     Maximum GC content  threshold
                                      Discard reads with GC content below minGC
                                      Example: 0.99 
                                      Default: 1.0
    --local-scheduler


**Example Run**

.. code-block:: none

      rnaseq-wf.py preProcessSamples \
                   --bbduk-minAQ 20 \
                   --bbduk-minGC 0.3 \
                   --bbduk-maxGC 0.7 \
                   --bbduk-minL 75  \
                   --local-scheduler

      **Output**
      /path/to/ProjectFolder/InputReads --contains the processed FastQ-reads
      /path/to/ProjectFolder/QCReports/paired_FastQC-ProcessedReads --contains the FASTQC reports of processed reads




4. Quantify transcripts
-----------------------

Quantification of the transcripts can be done using command ``quantifyTranscripts``

|  **Requirements**
|  1. Pre exexution of prepareProject.py command 
|  2. Availability of ``luigi.cfg`` file in ``parent folder`` and ``samples.txt`` inside the ``project folder``.
|
.. code-block:: none   

    rnaseq-wf.py quantifyTranscripts <arguments> --local-scheduler

    argument               type      Description

    --runQC                str       Run Quality Control Analysis of the RNASeq reads or Not
                                     [yes / no]

                                     If yes, preProcessSamples command will be run with default parameters.
                                     If no, quality control analysis will not be done, instead re-pair.sh or reformat.sh 
                                     script of bbmap will be run based on paired-end or single-end reads.


    --predTranscript       str       Predict transcriptome from genome?
                                     [yes / no]
                                     if yes, genome annotation will be done
                                     using PROKKA for prokaryotes and generated genome.ffn file
                                     will be used as transcript.\

   --annotFileType         str       Type of genome annotation file.
                                     [GFF or GTF or NA]

                                     The annotation file (genome_name.gff or genome_name.gtf) must be present along with 
                                     genome (genome_name.fna) inside the genome folder

                                     For prokaryotes, if user selects --predTranscript yes, then he must select 
                                     --annotFileType as NA.

  --quantMethod            str       Read quantification method
                                     [salmon / kallisto]
  --local-scheduler




|  **Example Run 1**
|  **quantifyTranscripts** 
|
|  1.  with out read quality control analysis  ``--runQC no``
|  2.  with read quantification method ``salmon``
|  3.  with ``GFF`` as genome annotation file type 
|
|  rnaseq-wf.py quantifyTranscripts --runQC ``no`` \
|                                   --quantMethod ``salmon`` \
|                                   --predTranscript ``no``  \
|                                   --annotFileType ``GFF``  \
|                                   --local-scheduler
|

|  **Example Run 2**
|  **quantifyTranscripts**
|  1.  with quality control analysis  ``--runQC yes``
|  2.  with read quantification method ``salmon``
|  3.  with predict transcript using PROKKA (annotFileType must be NA)
|
|  rnaseq-wf.py quantifyTranscripts --runQC ``no`` \
|                                   --quantMethod ``salmon`` \
|                                   --annotFileType ``NA`` \
|                                   --local-scheduler
|


5. Transcriptome based Differential Expression Analysis
-------------------------------------------------------

|  Transcript Quantification using ``salmon`` / ``kallisto`` followed by Differential expression analysis with ``DESeq2`` / ``edgeR``
| 
   **Requirements**
|  1. Pre exexution of prepareProject.py command 
|  2. Availability of ``luigi.cfg`` file in ``parent folder`` and ``samples.txt`` inside the ``project folder``.
|


.. code-block:: none  

    rnaseq-wf.py transcriptomeBasedDEA <arguments> --local-scheduler

    argument               type      Description

    --runQC                str       Run Quality Control Analysis of the RNASeq reads or Not
                                     [yes / no]

                                     If yes, preProcessSamples command will be run with default parameters.
                                     If no, quality control analysis will not be done, instead re-pair.sh or reformat.sh 
                                     script of bbmap will be run based on paired-end or single-end reads.

    --predTranscript       str       Predict transcriptome from genome?
                                     [yes / no]
                                     if yes, genome annotation will be done
                                     using PROKKA for prokaryotes and generated genome.ffn file
                                     will be used as transcript.\

   --annotFileType         str       Type of genome annotation file.
                                     [GFF or GTF or NA]

                                     The annotation file (genome_name.gff or genome_name.gtf) must be present along with 
                                     genome (genome_name.fna) inside the genome folder

                                     For prokaryotes, if user selects --predTranscript yes, then he must select 
                                     --annotFileType as NA.

  --quantMethod            str       Read quantification method
                                     [salmon / kallisto]

  --deaMethod              str       method to be used for differential expression analysis. 
                                     [deseq2 / edger]

  --factorInt              str       factor of intrest column of the target file
                                     example: conditions

  --refCond REFCOND        str       reference biological condition. 
                                     example: control

  --local-scheduler


|  **Example Run**
|  **Transcriptome based Differential Expression Analysis** 
|    rnaseq-wf.py quantifyTranscripts --runQC ``no``  \
|                                   --quantMethod ``salmon``  \
|                                   --predTranscript ``no``   \
|                                   --annotFileType ``GFF``   \
|                                   --deaMethod ``deseq2``  \
|                                   --factorInt ``conditions``  \
|                                   --refCond ``np``  \
|                                   --local-scheduler
|