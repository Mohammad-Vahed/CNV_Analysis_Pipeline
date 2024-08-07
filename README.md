# CNV_Analysis_Pipeline

# CNV Analysis Pipeline

This repository contains a pipeline for analyzing Copy Number Variations (CNVs) and visualizing the results using the Integrative Genomics Viewer (IGV). The pipeline processes multiple samples and generates filtered CNV data along with visualizations.

## Directory Structure

CNV_Analysis_Pipeline/
│
├── data/
│ ├── sample1_cnv.tsv
│ ├── sample2_cnv.tsv
│ └── ...
│
├── scripts/
│ └── cnv_pipeline.py
│
├── results/
│ └── (output files will be stored here)
│
├── README.md
│
└── requirements.txt


## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/CNV_Analysis_Pipeline.git
   cd CNV_Analysis_Pipeline

2. Install the required Python packages.
pip install -r requirements.txt

Usage
1. Place your CNV data files in the data/ directory. Each file should be in TSV format and named as sample_name_cnv.tsv.

2. Run the pipeline:
   python scripts/cnv_pipeline.py

Output: The results, including filtered CNV BED files and size distribution plots, will be saved in the results/ directory.

3. Example CNV Data Format
Each CNV data file should be in TSV format with the following columns:

'chromosome': Chromosome name
'start': Start position of the CNV
'end': End position of the CNV
'size': Size of the CNV
'pvalue': P-value of the CNV
'cnv_id': Unique identifier for the CNV
