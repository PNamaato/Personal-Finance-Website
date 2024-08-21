# Utility functions for calculations, chart generation, etc.

import matplotlib.pyplot as plt

def calculate_net_worth(assets, liabilities):
    return assets.sum() - liabilities.sum()

def create_pie_chart(data, labels):
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%')
    return fig
