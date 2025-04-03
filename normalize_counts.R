
library(DESeq2)

gene_counts <- read.delim("./data/data_for_trust4/GSE211044_bulkRNAseq_counts.txt")

# copy to local variable
raw_counts <- gene_counts
# deleting unnecessary columns
raw_counts$Chr <- NULL; raw_counts$Start <- NULL; raw_counts$End <- NULL;
raw_counts$Strand <- NULL; raw_counts$Length <- NULL
# store gene IDs in separate variable
gene_ids <- raw_counts$Geneid
raw_counts$Geneid <- NULL
# convert to matrix
raw_counts <- as.matrix(raw_counts)
# use gene IDs as row names
rownames(raw_counts) <- gene_ids
sample_info <- data.frame(
  sample_id = colnames(raw_counts),
  condition1 <- unlist(sapply(strsplit(colnames(raw_counts),"_"), `[`, 1, simplify=FALSE)),
  condition2 <- unlist(sapply(strsplit(colnames(raw_counts),"_"), `[`, 2, simplify=FALSE)),
  condition3 <- unlist(sapply(strsplit(colnames(raw_counts),"_"), `[`, 3, simplify=FALSE))
)
# normalize counts using DESeq2
dds <- DESeqDataSetFromMatrix(countData = raw_counts, colData = sample_info, design = ~ 1)
dds <- estimateSizeFactors(dds)
normalized_counts <- counts(dds, normalized = TRUE) 
# store data
write.csv(normalized_counts,"./data/normalized_counts.csv")
