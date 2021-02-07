import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_fi(model, features, top=None):
    """Plot the feature importance of the models that support feature importance"""

    # Make a dataframe of feature importance
    fi = pd.DataFrame({'feature': features, 'importance': model.feature_importances_.flatten().tolist()})
    fi_sorted = fi.sort_values(by='importance', ascending=False)

    # Plot
    sns.set(font_scale=1.5)
    if top:
        sns.catplot(x='importance', y='feature', kind='bar', color='blue', alpha=0.3,
                    data=fi_sorted.head(top), height=15)
    else:
        sns.catplot(x='importance', y='feature', kind='bar', color='blue', alpha=0.3,
                    data=fi_sorted, height=15)
    plt.show()