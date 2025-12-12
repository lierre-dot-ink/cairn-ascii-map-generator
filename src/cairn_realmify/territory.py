from dataclasses import dataclass


@dataclass
class Territory:
    landmarks: dict = None

    def get_longest_legend_entry_length(self):
        longest = None
        for k, v in self.landmarks.items():
            rendered_string_lenght = len(k) + len(": ") + len(v[0])
            if longest is None:
                longest = rendered_string_lenght
            elif longest < rendered_string_lenght:
                longest = rendered_string_lenght
        return longest


def generate_territory(config):
    t = Territory()
    t.landmarks = config
    return t
