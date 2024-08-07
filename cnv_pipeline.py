# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pybedtools import BedTool
import igv
import os

# Load CNV data
def load_cnv_data(file_path):
    cnv_data = pd.read_csv(file_path, sep='\t')
    return cnv_data

# Filter CNVs based on criteria
def filter_cnvs(cnv_data, min_size, max_pvalue):
    filtered_cnvs = cnv_data[(cnv_data['size'] > min_size) & (cnv_data['pvalue'] < max_pvalue)]
    return filtered_cnvs

# Visualize CNV size distribution
def plot_cnv_size_distribution(cnv_data, output_path):
    plt.figure(figsize=(10, 6))
    sns.histplot(cnv_data['size'], bins=50, kde=True)
    plt.title('Distribution of CNV Sizes')
    plt.xlabel('CNV Size (bp)')
    plt.ylabel('Frequency')
    plt.savefig(output_path)
    plt.close()

# Create a BED file for IGV visualization
def create_bed_file(cnv_data, output_path):
    cnv_bed = cnv_data[['chromosome', 'start', 'end', 'cnv_id']]
    cnv_bed.to_csv(output_path, sep='\t', header=False, index=False)

# Process a single sample
def process_sample(sample_file, output_dir, min_size, max_pvalue):
    sample_name = os.path.basename(sample_file).replace('_cnv.tsv', '')
    cnv_data = load_cnv_data(sample_file)
    filtered_cnvs = filter_cnvs(cnv_data, min_size, max_pvalue)
    
    # Plot CNV size distribution
    plot_output = os.path.join(output_dir, f"{sample_name}_cnv_size_distribution.png")
    plot_cnv_size_distribution(filtered_cnvs, plot_output)
    
    # Create BED file for IGV
    bed_output = os.path.join(output_dir, f"{sample_name}_filtered_cnvs.bed")
    create_bed_file(filtered_cnvs, bed_output)

# Main function to process multiple samples
def main(data_dir, output_dir, min_size=1000, max_pvalue=0.05):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for sample_file in os.listdir(data_dir):
        if sample_file.endswith('_cnv.tsv'):
            process_sample(os.path.join(data_dir, sample_file), output_dir, min_size, max_pvalue)

if __name__ == '__main__':
    data_dir = 'data/'
    output_dir = 'results/'
    main(data_dir, output_dir)
