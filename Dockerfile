# Use the official R base image
FROM rocker/r-ver:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    git \
    openjdk-11-jdk \
    build-essential \
    libxml2-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libz-dev \
    zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh && \
    bash /miniconda.sh -b -p /opt/conda && \
    rm /miniconda.sh

# Set Conda environment variables
ENV PATH="/opt/conda/bin:$PATH"

# Configure Conda to use Bioconda
RUN conda config --add channels defaults && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge

# Install Python and required libraries
RUN conda install -y python=3.10 pandas matplotlib seaborn numpy

# Install TRUST4 via Conda
RUN conda install -y -c bioconda trust4

# Install R and DESeq2
RUN R -e "install.packages('BiocManager', repos='http://cran.r-project.org')"
RUN R -e "BiocManager::install(c('XVector', 'SparseArray', 'GenomicRanges', 'DelayedArray', 'SummarizedExperiment'))"
RUN R -e "BiocManager::install('DESeq2')"

# Set default command
CMD ["/bin/bash"]