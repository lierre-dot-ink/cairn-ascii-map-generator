from .territory import Territory
import numpy as np


def _make_blank_canvas(width: int, height: int, filler_char):
    representation = [filler_char] * height
    for i in range(0, height):
        representation[i] = [filler_char] * width
    return representation


def _draw_landmark_and_land_types(
    representation, territory: Territory, width: int, height: int
):
    for w in range(0, width):
        for h in range(0, height):
            marker = None
            associated_distance = None
            for k, v in territory.landmarks.items():
                vertical_ix = round(v[1][0] * height)
                horizontal_ix = round(v[1][1] * width)
                current_distance = np.linalg.norm(
                    np.array((vertical_ix, horizontal_ix)) - np.array((h, w))
                )
                is_landmark = vertical_ix == h and horizontal_ix == w
                if is_landmark:
                    representation[h][w] = k.upper()
                    break
                if marker == None:
                    marker = k.lower()
                    associated_distance = current_distance
                else:
                    is_closest = current_distance < associated_distance
                    if is_closest:
                        associated_distance = current_distance
                        marker = k.lower()
                representation[h][w] = marker
    return representation


def _make_legend(territory: Territory):
    n_entries = len(territory.landmarks.keys())
    legend_base = [""] * n_entries

    writing_head = 0
    max_line_length = 0
    for k, v in territory.landmarks.items():
        legend_base[writing_head] = f"{k}: {v[0]}"
        writing_head += 1

    render = "\n"
    render += "\n".join("".join(line) for line in legend_base)
    return render


def realmify(
    territory: Territory,
    width: int,
    height: int,
    filler_char=" ",
    legend=True,
    border_decoration=False,
):
    representation = _make_blank_canvas(width, height, filler_char)
    representation = _draw_landmark_and_land_types(
        representation, territory, width, height
    )

    if not border_decoration:
        render = "\n".join("".join(line) for line in representation)
        if legend:
            render += "\n"
            render += _make_legend(territory)
    else:
        render = "┌" + "─" * (width) + "┐\n"
        for line in representation:
            render += "│" + "".join(line) + "│\n"
        render += "└" + "─" * (width) + "┘\n"

        if legend:
            base_legend = _make_legend(territory)
            longest_entry = territory.get_longest_legend_entry_length()
            render += "┌" + "─" * (longest_entry) + "┐\n"
            for line in base_legend.split("\n"):
                if line == "":
                    continue
                if len(line) < longest_entry:
                    line += " " * (longest_entry - len(line))
                render += "│" + line + "│\n"
            render += "└" + "─" * (longest_entry) + "┘"

    return render
