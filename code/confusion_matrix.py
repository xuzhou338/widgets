import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from itertools import product

from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

class ConfusionMatrixDisplay:
    """Confusion matrix class copied from sklearn."""
    def __init__(self, confusion_matrix, *, display_labels=None):
        self.confusion_matrix = confusion_matrix
        self.display_labels = display_labels

    def plot(self, *, include_values=True, cmap=plt.cm.Blues,
             xticks_rotation='horizontal', values_format=None,
             ax=None, colorbar=True):

        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure

        cm = self.confusion_matrix
        n_classes = cm.shape[0]
        self.im_ = ax.imshow(cm, interpolation='nearest', cmap=cmap)
        self.text_ = None
        cmap_min, cmap_max = self.im_.cmap(0), self.im_.cmap(256)

        if include_values:
            self.text_ = np.empty_like(cm, dtype=object)

            # print text with appropriate color depending on background
            thresh = (cm.max() + cm.min()) / 2.0

            for i, j in product(range(n_classes), range(n_classes)):
                color = cmap_max if cm[i, j] < thresh else cmap_min

                if values_format is None:
                    text_cm = format(cm[i, j], '.2g')
                    if cm.dtype.kind != 'f':
                        text_d = format(cm[i, j], 'd')
                        if len(text_d) < len(text_cm):
                            text_cm = text_d
                else:
                    text_cm = format(cm[i, j], values_format)

                self.text_[i, j] = ax.text(
                    j, i, text_cm,
                    ha="center", va="center",
                    color=color)

        if self.display_labels is None:
            display_labels = np.arange(n_classes)
        else:
            display_labels = self.display_labels
        if colorbar:
            fig.colorbar(self.im_, ax=ax)
        ax.set(xticks=np.arange(n_classes),
               yticks=np.arange(n_classes),
               xticklabels=display_labels,
               yticklabels=display_labels,
               ylabel="True label",
               xlabel="Predicted label")

        ax.set_ylim((n_classes - 0.5, -0.5))
        plt.setp(ax.get_xticklabels(), rotation=xticks_rotation)

        self.figure_ = fig
        self.ax_ = ax
        return self

def plot_confusion_matrix(estimator, X, y_true, *, thresh=None, labels=None,
                          sample_weight=None, normalize=None,
                          display_labels=None, include_values=True,
                          xticks_rotation='horizontal',
                          values_format=None,
                          cmap=plt.cm.Blues, ax=None, colorbar=True):
    """Similar to the official plot_confusion_matrix function from sklearn, but with threshold support"""
    if thresh:
        y_pred = pd.Series(estimator.predict_proba(X)[:, 0]).apply(lambda x: int(x < thresh))
    else:
        y_pred = estimator.predict(X)
    cm = confusion_matrix(y_true, y_pred, sample_weight=sample_weight,
                          labels=labels, normalize=normalize)

    if display_labels is None:
        if labels is None:
            display_labels = unique_labels(y_true, y_pred)
        else:
            display_labels = labels

    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  display_labels=display_labels)
    return disp.plot(include_values=include_values,
                     cmap=cmap, ax=ax, xticks_rotation=xticks_rotation,
                     values_format=values_format, colorbar=colorbar)

def plot_cm(y_true, y_pred, *, labels=None,
            sample_weight=None, normalize=None,
            display_labels=None, include_values=True,
            xticks_rotation='horizontal',
            values_format=None,
            cmap=plt.cm.Blues, ax=None, colorbar=True):

    """Plot confusion matrix bypassing the input of estimator. Directly uses y_true and y_pred"""
    cm = confusion_matrix(y_true, y_pred, sample_weight=sample_weight,
                          labels=labels, normalize=normalize)

    if display_labels is None:
        if labels is None:
            display_labels = unique_labels(y_true, y_pred)
        else:
            display_labels = labels

    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  display_labels=display_labels)
    return disp.plot(include_values=include_values,
                     cmap=cmap, ax=ax, xticks_rotation=xticks_rotation,
                     values_format=values_format, colorbar=colorbar)

def predict_thresh(estimator, X, thresh):
    """Return the prediction result using threshold"""
    return pd.Series(estimator.predict_proba(X)[:, 0]).apply(lambda x: int(x < thresh))

def confusion_matrix_thresh(estimator, X, y, thresh):
    """Return the confusion matrix using threshold"""
    return confusion_matrix(y, predict_thresh(estimator, X, thresh))