import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import hist
import numpy as np
from pattern3.metrics import fisher
from scipy.stats import fisher_exact
from scipy.stats import fisher_exact
from scipy import stats
from scipy.stats import pearsonr

df = pd.read_csv("Rules/phd_experiments_result.csv")
df1 = df[['PCA Confidence','Inferred_PCA']]



p_val = pearsonr(df['PCA Confidence'], df['Inferred_PCA'])[1]

print(p_val)
fig = plt.figure(figsize=(12,5))
plt.suptitle("Pearson correlation coefficient and p-value for testing non-correlation with p-value: {}".format(p_val),fontsize=12)
ax1 = fig.add_subplot(121)
ax1.hist(df['PCA Confidence'], bins=20, alpha=0.5)
# ax1.set_yscale('symlog')
ax1.set_yscale('linear')
ax1.set_title('PCA Confidence')
ax1.set_xlabel('PCA Confidence')
ax1.set_ylabel('Rules')
ax2 = fig.add_subplot(122)
ax2.hist(df['Inferred_PCA'], bins=20, alpha=0.5)
# ax2.set_yscale('symlog')
ax2.set_yscale('linear')
ax2.set_title('Inferred PCA Confidence')
ax2.set_xlabel('Inferred PCA Confidence')
ax2.set_ylabel('Rules')
plt.show()
# fig.savefig('PCA_Confidence_Histogram_linear_pval.png')

