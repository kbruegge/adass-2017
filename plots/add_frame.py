import matplotlib.patches as patches


def add_frame(ax, offset=0.1):

    kwargs = {
        'linewidth': 0,
        'edgecolor': 'white',
        'facecolor': 'white',
        'alpha': 0.6,
    }

    left_rect = patches.Rectangle(
        (0 - offset, 0),
        offset,
        1,
        **kwargs
    )
    ax.add_patch(left_rect)


    right_rect = patches.Rectangle(
        (1, 0),
        offset,
        1,
        **kwargs
    )
    ax.add_patch(right_rect)

    top_rect = patches.Rectangle(
        (0 - offset, 1),
        1 + 2 * offset,
        offset,
        **kwargs
    )
    ax.add_patch(top_rect)

    bottom_rect = patches.Rectangle(
        (0 - offset, 0 - offset),
        1 + 2 * offset,
        offset,
        **kwargs
    )
    ax.add_patch(bottom_rect)
