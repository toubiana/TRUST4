#!/bin/bash

# Usage: ./run_trust4.sh fastq1 fastq2 output_dir reference imgt

# Check if TRUST4 is installed
if ! command -v run-trust4 &> /dev/null
then
    echo "Error: TRUST4 not found. Please install TRUST4 first."
    exit 1
fi

# Check if correct number of arguments are provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <FASTQ_FILE_1> <FASTQ_FILE_2> <OUTPUT_DIR> <REFERENCE>"
    exit 1
fi


FASTQ1=$1
FASTQ2=$2
OUTPUT_DIR=$3
REFERENCE=$4


# Create output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Run TRUST4 on the first FASTQ file
echo "Processing $FASTQ1 with TRUST4..."
run-trust4 -u $FASTQ1 -o $OUTPUT_DIR/NSCLC4 -t 4 -f $REFERENCE --ref $REFERENCE

echo "Processing $FASTQ2 with TRUST4..."
run-trust4 -u $FASTQ2 -o $OUTPUT_DIR/NSCLC3 -t 4 -f $REFERENCE --ref $REFERENCE

echo "TRUST4 processing complete. Results saved in $OUTPUT_DIR."
