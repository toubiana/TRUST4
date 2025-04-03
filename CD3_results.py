import pandas as pd
import matplotlib.pyplot as plt

# Load TRUST4 output NSCLC 4
df = pd.read_csv("./data/trust4_output/NSCLC4_report.tsv", sep="\t")

# Compute CDR3 lengths
df["CDR3_length"] = df["CDR3aa"].str.len()

# Plot histogram
plt.figure(figsize=(8,5))
plt.hist(df["CDR3_length"], bins=20, color="royalblue", edgecolor="black")
plt.xlabel("CDR3 Length (Amino Acids)  NSCLC 4, TIL, eTconv, bulk RNA-seq")
plt.ylabel("Frequency")
plt.title("CDR3 Length Distribution")

# Save the figure as a PDF
plt.savefig("./data/cdr3_length_distribution_NSCLC4.pdf", format="pdf", bbox_inches="tight")
plt.close() 

# Load TRUST4 output NSCLC 3
df = pd.read_csv("./data/trust4_output/NSCLC3_report.tsv", sep="\t")

# Compute CDR3 lengths
df["CDR3_length"] = df["CDR3aa"].str.len()

# Plot histogram
plt.figure(figsize=(8,5))
plt.hist(df["CDR3_length"], bins=20, color="royalblue", edgecolor="black")
plt.xlabel("CDR3 Length (Amino Acids)  NSCLC 3, TIL, eTconv, bulk RNA-seq")
plt.ylabel("Frequency")
plt.title("CDR3 Length Distribution")

# Save the figure as a PDF
plt.savefig("./data/cdr3_length_distribution_NSCLC3.pdf", format="pdf", bbox_inches="tight")
plt.close() 
