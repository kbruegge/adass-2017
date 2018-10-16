import click
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from natsort import natsorted


@click.command()
@click.argument('input_files', nargs=-1, type=click.Path(exists=True))
@click.argument('output_file', type=click.Path(exists=False))
def main(input_files, output_file):
    '''
    This takes multiple csv files as INPUT_FILES and produces a
    plot at the given OUTPUT_FILE path. The csv files are expected to contain at
    least the 'copy_id' and '@datarate' columns.
    '''

    total_datarates = pd.DataFrame()

    for f in input_files:
        # print('reading file {}'.format(f))
        df = pd.read_csv(f)
        result = pd.DataFrame()
        n_threads = len(df.groupby('copy_id'))

        for n, g in df.groupby('copy_id'):
            # remove first row. its an outlier
            result[n] = g['@datarate'].values[4:]

        total_datarates['{}'.format(n_threads)] = result.sum(axis=1)



    sorted_columns = natsorted(total_datarates.columns)[0:24]
    total_datarates = total_datarates.reindex_axis(sorted_columns, axis=1)

    # sns.set_style('darkgrid')
    ax = sns.stripplot(data=total_datarates, color='#348ABD', size=4.0, jitter=0.02)
    # ax.set_xlim([-1, 49])
    major_ticks = np.arange(3, 26, 4)
    minor_ticks = np.arange(0, 26, 1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)

    labels = np.arange(4, 26, 4)
    ax.set_xticklabels(labels)

    sns.despine()
    plt.xlabel('Number of Threads')
    plt.ylabel('Events per Second')
    plt.tight_layout()
    plt.savefig(output_file)


if __name__ == "__main__":
    main()
