from astropy.io import fits
from astropy.coordinates import SkyCoord
import astropy.units as u
import matplotlib.pyplot as plt
import click


@click.command()
@click.argument('input_path', type=click.Path(exists=True, dir_okay=False, file_okay=True))
@click.argument('output_path', type=click.Path(exists=False, dir_okay=False, file_okay=True))
def main(input_path, output_path):
    b = fits.open(input_path)

    dec = b[1].data['DEC'] * u.degree
    ra = b[1].data['RA'] * u.degree

    c = SkyCoord(ra=ra, dec=dec, frame='icrs')
    ra_rad = c.ra.wrap_at(180 * u.deg).radian
    dec_rad = c.dec.radian

    fig = plt.figure(figsize=(5, 3))
    ax = fig.add_subplot(111, projection="mollweide")
    ax.set_facecolor('black')
    ax.scatter(ra_rad, dec_rad, s=3, c='#44BBFF')
    ax.grid(color='#555555')
    ax.tick_params(axis='x', colors='#EEEEEE')
    plt.tight_layout()
    plt.savefig(output_path)


if __name__ == '__main__':
    main()
