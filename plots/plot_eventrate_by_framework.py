import click
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@click.command()
@click.argument('input_files', nargs=-1, type=click.Path(exists=True))
@click.argument('output_file', type=click.Path(exists=False))
@click.option('--label', '-l', multiple=True, help='the labels of the groups')
def main(input_files, output_file, label):
    if not len(input_files) == len(label):
        print('Number of input files has to be equal to number of provided labels')
        return

    result = pd.DataFrame()
    print(label)
    if not label:
        label = list(range(1, len(input_files) + 1))

    for i, f in enumerate(input_files):
        df = pd.read_csv(f)
        # drop first 5 lines as outliers
        df = df[15:]
        datarate = df['@datarate']
        result['{}'.format(label[i])] = datarate

    # result = result.reindex_axis(natsorted(result.columns), axis=1)

    sns.stripplot(data=result, jitter=0.02)

    sns.despine()
    plt.ylabel('Events per Second')
    plt.tight_layout()
    plt.savefig(output_file)

if __name__ == "__main__":
    main()
