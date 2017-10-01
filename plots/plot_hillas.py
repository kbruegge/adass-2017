import matplotlib.pyplot as plt
import numpy as np
import click

def toy_cov(n_photons=100):
    # n_photons = rand_power()

    length = np.random.normal(6.5 * np.log10(n_photons), 0.2 * np.log10(n_photons))
    width = np.random.uniform(0.4 * length, 0.8 * length)
    theta = np.random.uniform(0, 2 * np.pi)

    cov = [[length**2, 0], [0, width**2]]
    rot = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])

    cov = rot @ cov @ rot.T

    return cov

@click.command()
@click.argument('output_path', type=click.Path(exists=False, dir_okay=False, file_okay=True) )
@click.option('-n', default=750,  help='Number of photons to simulate')
@click.option('-s', default=27,  help='The random seed to use')
def main(output_path, n, s):
    print('pwaotting teh shower')
    np.random.seed(s)
    # extent = [-5,5,-5,5]

    fig, ax = plt.subplots()
    true_cov = toy_cov(n)
    true_eigenvalues, true_eigenvectors = np.linalg.eigh(true_cov)
    samples = np.random.multivariate_normal([0,0], true_cov, n)
    x, y = samples.T

    # ax.plot(x, y, ',', color='white', markersize='2', alpha=0.5, marker='x')
    image = ax.hexbin(x,y,cmap='viridis',gridsize=40, linewidths=0.025, edgecolors='#7c738a', extent=[-150, 150, -150, 150])

    #true values
    # width, length  = 2 * np.sqrt(true_eigenvalues)
    # w_vector = width * true_eigenvectors[:,0]
    # l_vector = length * true_eigenvectors[:,1]
    #
    # ax.arrow(0, 0, w_vector[0], w_vector[1],  fc='white', ec='white', linewidth=1.5, head_width=2, head_length=4)
    # ax.arrow(0, 0, l_vector[0], l_vector[1],  fc='white', ec='white', linewidth=1.5, head_width=2, head_length=4)

    b = fig.colorbar(image)
    b.set_label('Number of Photons')

    #hide the ticks
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    ax.set_xlim([-80, 80])
    ax.set_ylim([-80, 80])

    # ax.set_aspect('equal')
    # plt.show()
    plt.tight_layout()

    plt.savefig(output_path)



if __name__ == '__main__':
    main()
