import yaml
import argparse
import logging

import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser(description='Plot petal length from UCI Iris dataset')
parser.add_argument('--title', '-t', type=str, help='Plot title', default='Petal dimensions')
parser.add_argument('--output_file', '-o', type=str, help='Output plot filename', default='iris')
args = parser.parse_args()

logging.basicConfig(
    handlers=(logging.StreamHandler(), logging.FileHandler('uci_iris.log')), 
    level=logging.INFO,
    )

dataset_url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.cs'

try:
    iris_data = pd.read_csv(dataset_url)
    logging.info(f'Successfully loaded {dataset_url}')
except Exception as e:
    logging.error('Error loading dataset', exc_info=e)
    raise e

def plot_scatter(df, yvar, xvar, title):
    plt.scatter(df[yvar], df[xvar])
    plt.title(title)

plot_scatter(iris_data, 'sepal_width', 'sepal_length', args.title)
plt.savefig(f'{args.output_file}.png')
