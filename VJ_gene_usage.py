import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load TRUST4 output NSCLC4
df = pd.read_csv("./data/trust4_output/NSCLC4_report.tsv", sep="\t")

# Count occurrences of each V gene
v_usage = df["V"].value_counts()

# Create figure
plt.figure(figsize=(10, 5))
sns.barplot(x=v_usage.index, y=v_usage.values, color="steelblue")

# Format plot
plt.xticks(rotation=90)
plt.xlabel("V Gene")
plt.ylabel("Count")
plt.title("V Gene Usage")

# Save plot as a PDF
plt.savefig("NSCLC4_vj_gene_usage.pdf", format="pdf", bbox_inches="tight")

print("Plot saved as vj_gene_usage.pdf")

# Load TRUST4 output NSCLC4
df = pd.read_csv("./data/trust4_output/NSCLC3_report.tsv", sep="\t")

# Count occurrences of each V gene
v_usage = df["V"].value_counts()

# Create figure
plt.figure(figsize=(10, 5))
sns.barplot(x=v_usage.index, y=v_usage.values, color="steelblue")

# Format plot
plt.xticks(rotation=90)
plt.xlabel("V Gene")
plt.ylabel("Count")
plt.title("V Gene Usage")

# Save plot as a PDF
plt.savefig("NSCLC3_vj_gene_usage.pdf", format="pdf", bbox_inches="tight")

print("Plot saved as vj_gene_usage.pdf")
