import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the data from CSV files
norm_data = pd.read_csv("./data/normalized_cell_counts.csv", index_col=0)  # Rows: Cell types, Cols: Samples
p_values = pd.read_csv("./data/pvalues_cell_counts.csv", index_col=0)  # Same structure

# Extract specific cell types
cell_types = ["CD8+ T-cells", "NK cells"]
norm_selected = norm_data.loc[cell_types]
p_selected = p_values.loc[cell_types]

# Define color scale for p-values (red = significant, blue = non-significant)
def get_colors(p_vals):
    return [plt.cm.coolwarm(1 - min(1, p)) for p in p_vals]  # Coolwarm colormap

# Plot function for each cell type
def plot_cell_type(cell_type):
    values = norm_selected.loc[cell_type]
    p_vals = p_selected.loc[cell_type]
    
    # Sort by values for better visualization
    #sorted_indices = np.argsort(values)
    #values = values.iloc[sorted_indices]
    #p_vals = p_vals.iloc[sorted_indices]
    
    colors = get_colors(p_vals)

    plt.figure(figsize=(10, 6))
    plt.barh(values.index, values, color=colors, edgecolor="black")
    plt.xlabel("Normalized Cell Counts")
    plt.ylabel("Samples")
    plt.title(f"{cell_type} Cell Counts Across Samples")
    
    # Reduce y-axis font size
    plt.yticks(fontsize=6)
    
    # Add color bar for p-values
    sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=plt.Normalize(vmin=0, vmax=1))
    #plt.colorbar(sm, label="P-value (Significance)")
     # Save the figure as a PDF
    pdf_filename = f"./data/{cell_type.replace('+', 'pos').replace(' ', '_')}_cellcounts_unsorted.pdf"
    plt.savefig(pdf_filename, format="pdf", bbox_inches="tight")
    plt.close() 

# Generate plots for both cell types
for cell in cell_types:
    plot_cell_type(cell)
