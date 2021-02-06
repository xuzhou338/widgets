import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def value_counts(df):
    """Count values or Plot histograms for categorical and numerical values respectively."""
    for col in df.columns:
        dtype = df[col].dtype
        cnt = df[col].count()
        num_na = df[col].isna().sum()
        value_cnt = df[col].value_counts(dropna=False)

        print('** {0} ** ({1})'.format(col, dtype))
        print('----------------------')
        print('Total Counts:', df[col].shape[0])
        print('Non-null Counts:', cnt)
        print('NA Counts:', num_na)
        print('NA Ratio:', round(num_na / (num_na + cnt), 2))
        print('----------------------')
        if df[col].dtype == np.dtype('float64'):
            df[col].hist()
            plt.show()
        else:
            print(value_cnt)
        print('\n')

def corr_heatmap(df, cbar=False, title="Pearson's Correlation Among Numerical Features",
                 title_size=16, title_pad=16, label_size=14, anot_size=14):
    """Plot the correlation heatmap"""
    fig, ax = plt.subplots(figsize=(16, 12))
    sns.heatmap(
        round(df.corr(), 2),
        cmap=sns.diverging_palette(220, 10, as_cmap=True),
        square=True,
        #         cbar_kws={'shrink':.9 },
        cbar=cbar,
        ax=ax,
        annot=True,
        linewidths=0.1,
        vmin=-1.0,
        vmax=1.0,
        linecolor='white',
        annot_kws={'fontsize': anot_size})
    ax.set_yticklabels(ax.get_yticklabels(), size=label_size)
    ax.set_xticklabels(ax.get_xticklabels(), size=label_size)
    ax.set_title(title, pad=title_pad, size=title_size)
    return fig, ax

def corr_scatter(df):
    """Plot the correlation scatterplot"""
    grid = sns.pairplot(df)
    return grid