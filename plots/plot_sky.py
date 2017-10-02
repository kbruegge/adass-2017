import click
import pandas as pd
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import cartesian_to_spherical, Angle, SkyCoord, EarthLocation
from dateutil import parser
import numpy as np


def select_events(df, threshold=0.6):
    df = df.loc[df['prediction:signal:mean'] > 0.6]
    x = df['stereo:estimated_direction:x']
    y = df['stereo:estimated_direction:y']
    z = df['stereo:estimated_direction:z']

    r, lat, lon = cartesian_to_spherical(x.values * u.m, y.values * u.m, z.values * u.m)

    alt = Angle(90 * u.deg - lat)

    az = Angle(lon).wrap_at(180 * u.deg)

    paranal = EarthLocation.of_site('paranal')
    dt = parser.parse('1987-09-20 22:15')

    c = SkyCoord(
        alt=alt,
        az=az,
        obstime=dt,
        frame='altaz',
        location=paranal,
    ).transform_to(frame='icrs')
    return c, df.w


@click.command()
@click.argument('gammas', type=click.Path(exists=True))
@click.argument('protons', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path(exists=False))
def main(gammas, protons, output_file):
    df_g = pd.read_csv(gammas).dropna()
    df_g['w'] = 1
    df_p = pd.read_csv(protons).dropna()
    df_p['w'] = 1000

    df = pd.concat([df_g, df_p])
    c, w = select_events(df)
    # import IPython; IPython.embed()
    plt.hist2d(c.ra.deg, c.dec.deg, cmap='inferno', bins=[np.linspace(262.25, 263.25, 30), np.linspace(-5.2, -4.2, 30)], weights=w)

    plt.xlabel('Right Ascension  / degree')
    plt.ylabel('Declination / degree')
    plt.tight_layout()
    # b = plt.colorbar()
    # b.set_label('Events')
    plt.savefig(output_file)


if __name__ == "__main__":
    main()
