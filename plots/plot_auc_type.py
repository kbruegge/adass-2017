import click
import matplotlib.pyplot as plt
from add_frame import add_frame
from sklearn.metrics import roc_curve, roc_auc_score
from fact import io


@click.command()
@click.argument('cv_predictions_path', type=click.Path(exists=True, dir_okay=False,))
@click.argument('output_file', type=click.Path(exists=False, dir_okay=False,))
def main(cv_predictions_path, output_file):
    '''
    Plot the event distributions from the triggered gammas given in the
    PREDICTED_EVENTS input file.
    '''

    cv_predictions = io.read_data(cv_predictions_path)

    for name, group in cv_predictions.groupby('telescope_type'):
        y_score = group['probabilities']
        y_true = group['label']

        fpr, tpr, _ = roc_curve(y_true, y_score)
        auc = roc_auc_score(y_true, y_score)

        plt.plot(fpr, tpr, lw=1, label='{} Area under Curve:${:.4f}$'.format(name, auc))

    add_frame(plt.gca())
    plt.legend()
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.tight_layout()
    plt.savefig(output_file)


if __name__ == '__main__':
    main()
