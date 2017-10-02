import click
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from add_frame import add_frame


@click.command()
@click.argument('predicted_gammas', type=click.Path(exists=True, dir_okay=False,))
@click.argument('predicted_protons', type=click.Path(exists=True, dir_okay=False,))
@click.argument('output_file', type=click.Path(exists=False, dir_okay=False,))
def main(predicted_gammas, predicted_protons, output_file):
    '''
    Plot the event distributions from the triggered gammas given in the
    PREDICTED_EVENTS input file.
    '''

    gammas = pd.read_csv(predicted_gammas)

    protons = pd.read_csv(predicted_protons)

    c_g = gammas['array:num_triggered_telescopes'].value_counts()
    c_p = protons['array:num_triggered_telescopes'].value_counts()

    c_g = c_g / len(gammas)
    c_p = c_p / len(protons)

    # import IPython; IPython.embed()

    nums = np.arange(2, 21, 1)
    width = 1
    plt.bar(left=nums - width / 2.0, width=1, height=c_g[nums], tick_label=nums, alpha=0.5, label='gammas')
    plt.bar(left=nums - width / 2.0, width=1, height=c_p[nums], tick_label=nums, alpha=0.5, label='protons')
    plt.ylabel('Fraction of Events')
    plt.xlabel('Number of Triggered Telescopes')
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file)


if __name__ == '__main__':
    main()
