import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


# df = pd.read_csv('Rules/Pearson_correlation_phd.csv')

# # comparison_column = np.where(df["Positive Examples"] == df["Inferred_Support"], True, False)
# # df["equal"] = comparison_column
#
# # # pearsoncorr.to_csv('Rules/Pearson.csv')
# #
# # plt.figure(figsize=(10,8))
# # sns.regplot(x='Positive Examples', y='Inferred_Support', data=df, scatter_kws={"color": "black"}, line_kws = {"color": "red"})
# # # plt.title('Correlation')
# # # sns.lmplot(x='PCA Confidence', y='Inferred_PCA', col='equal', hue='equal', data=df, col_wrap=2, height=5, aspect=.4, y_jitter=.1, ci=None)
# # plt.show()
#
#
# # fig, axs = plt.subplots(2, 2)
# #
# # for ax, i in zip(axs.flat, range(3)):
# #     sns.regplot(x='Positive Examples', y='Inferred_Support', data=df, scatter_kws={"color": "black"}, line_kws = {"color": "red"}, ax=ax)
# #     sns.regplot(x='Head Coverage', y='Inferred_Confidence', data=df, scatter_kws={"color": "black"},line_kws={"color": "red"}, ax=ax)
# #     sns.regplot(x='PCA Confidence', y='Inferred_PCA', data=df, scatter_kws={"color": "black"},line_kws={"color": "red"}, ax=ax)
#
# # pearsoncorr = df.corr(method='pearson')
# # print(pearsoncorr)
# # pearsoncorr.to_csv('LC_trial.csv')
# # sns.heatmap(pearsoncorr)
# Support = df['Positive Examples']
# Confidence = df['Head Coverage']
# PCA = df['PCA Confidence']
#
# fig, axs = plt.subplots(ncols=2)
# sns.regplot(x=Support, y=df['Inferred_Support'], data=df, ax=axs[0])
# sns.regplot(x=Confidence, y=df['Inferred_Confidence'], data=df, ax=axs[1])
# # sns.boxplot(x=PCA,y=df['Inferred_PCA'], data=df, ax=axs[2])
# plt.show()
# sns.heatmap(df, cmap ='RdYlGn', linewidths = 0.30, annot = True)
# cols = df.columns
# index = df.iloc[:,0]

# sns.heatmap(df, annot=True)
# # df.style.background_gradient(cmap ='coolwarm')
# plt.show()


# Python program to generate a heatmap
# which represents the correlation between
# columns of panda dataframe

# import required libraries
import pandas as pd
import seaborn as sn

# Defining figure size
# for the output plot
fig, ax = plt.subplots(figsize=(20,10))

# Defining index for the dataframe
idx = ['Head Coverage', 'PCA Confidence', 'Positive Examples', 'Inferred_Support','Inferred_Confidence', 'Inferred_PCA']
# idx = ['A','B','C','D','E','F']
df = pd.read_csv('Rules/Pearson_correlation_phd.csv')

df = pd.DataFrame(df, columns=['Head Coverage', 'PCA Confidence', 'Positive Examples', 'Inferred_Support','Inferred_Confidence', 'Inferred_PCA'])
#  cmap='RdYlGn_r',
sn.heatmap(df, cmap='RdYlGn_r', annot=True,xticklabels=True, yticklabels=idx, annot_kws={"fontsize":12})
plt.yticks(rotation='horizontal')
plt.savefig('Rules/seabornPandas.png', dpi=100)
# plt.show()