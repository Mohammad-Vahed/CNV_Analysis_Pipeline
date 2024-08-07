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

bash
Copy code

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/CNV_Analysis_Pipeline.git
   cd CNV_Analysis_Pipeline
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Usage
Place your CNV data files in the data/ directory. Each file should be in TSV format and named as sample_name_cnv.tsv.

Run the pipeline:

bash
Copy code
python scripts/cnv_pipeline.py
Output: The results, including filtered CNV BED files and size distribution plots, will be saved in the results/ directory.

Example CNV Data Format
Each CNV data file should be in TSV format with the following columns:

chromosome: Chromosome name
start: Start position of the CNV
end: End position of the CNV
size: Size of the CNV
pvalue: P-value of the CNV
cnv_id: Unique identifier for the CNV
Pipeline Details
Script: scripts/cnv_pipeline.py
This script performs the following steps:

Load CNV Data: Reads CNV data from TSV files.
Filter CNVs: Filters CNVs based on minimum size and maximum p-value.
Visualize CNV Size Distribution: Generates a histogram of CNV sizes.
Create BED File: Generates BED files for filtered CNVs for visualization in IGV.
Functions:
load_cnv_data(file_path): Loads CNV data from a TSV file.
filter_cnvs(cnv_data, min_size, max_pvalue): Filters CNVs based on size and p-value.
plot_cnv_size_distribution(cnv_data, output_path): Plots the distribution of CNV sizes.
create_bed_file(cnv_data, output_path): Creates a BED file from filtered CNV data.
process_sample(sample_file, output_dir, min_size, max_pvalue): Processes a single sample.
main(data_dir, output_dir, min_size=1000, max_pvalue=0.05): Processes multiple samples.
Requirements
pandas
numpy
matplotlib
seaborn
pybedtools
igv
