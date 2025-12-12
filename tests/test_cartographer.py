import unittest
from cairn_realmify.cartographer import realmify
from cairn_realmify.territory import Territory, generate_territory
from difflib import unified_diff

EXPECTED_MAP_WITH_DECORATION = """
┌────────────────────┐
│aaaaaaaaaaabbbbbbbbb│
│aaaaaaaaaaabbbbbbbbb│
│aaaaaaaaaaabbbbbbbbb│
│aaaaaAaaaaabbbbBbbbb│
│aaaaaaaaaaabbbbbbbbb│
│aaaaaaaaaaabbbbbbbbb│
│aaaaaaaaaacccccccccc│
│aaaaaaaaaacccccccccc│
│aaaaaaaaaccccccCcccc│
│aaaaaaaaaccccccccccc│
│aaaaaaaacccccccccccc│
└────────────────────┘
┌───────────────────┐
│A: Silver_Face     │
│B: Broken_Sundial  │
│C: Great_Waterwheel│
└───────────────────┘
""".strip("\n")


class TestCartographer(unittest.TestCase):
    def assert_equal_realms(self, realm, expected_realm):
        split_realm = realm.splitlines(keepends=True)
        split_expected_realm = expected_realm.splitlines(keepends=True)

        diff = unified_diff(
            split_realm, split_expected_realm, fromfile="old", tofile="new", lineterm=""
        )
        printable_diff = "".join(diff)

        for l_r in split_realm:
            for l_e in split_expected_realm:
                self.assertEqual(l_r, l_e, f"got {realm}\n expected {expected_realm}")
                break
            break

        n_newlines = realm.count("\n")
        n_newlines_expected = expected_realm.count("\n")

        self.assertEqual(n_newlines, n_newlines_expected)
        self.maxDiff = None
        self.assertEqual(realm, expected_realm, printable_diff)

    def test_basic_rendering(self):
        t = generate_territory({})

        arbitrary_width = 64
        arbitrary_height = 32

        realm = realmify(
            t, width=arbitrary_width, height=arbitrary_height, legend=False
        )

        lines = realm.splitlines()

        self.assertEqual(arbitrary_height, len(lines))
        for line in lines:
            self.assertEqual(arbitrary_width, len(line))

    def test_expected_territory(self):
        config = {
            "A": ("Silver_Face", (0.25, 0.25)),
            "B": ("Broken_Sundial", (0.25, 0.75)),
            "C": ("Great_Waterwheel", (0.75, 0.75)),
        }
        t = generate_territory(config)
        realm = realmify(t, 12, 4, filler_char="·")

        expected_realm = "\n".join(
            [
                "aaaaaaabbbbb",
                "aaaAaaabbBbb",
                "aaaaaaabbbbb",
                "aaaaaacccCcc",
                "",
                "A: Silver_Face",
                "B: Broken_Sundial",
                "C: Great_Waterwheel",
            ]
        )

        self.assert_equal_realms(realm, expected_realm)

    def test_legend_length_retrieval(self):
        """
        In order to encase the legend in a border decoration,
        we need to learn the longest string entry in it.
        """
        config = {
            "A": ("Silver_Face", (0.25, 0.25)),
            "B": ("Broken_Sundial", (0.25, 0.75)),
            "C": ("Great_Waterwheel", (0.75, 0.75)),
        }
        t = generate_territory(config)
        longest_entry_length = t.get_longest_legend_entry_length()
        expected_length = len("C: Great_Waterwheel")
        self.assertEqual(longest_entry_length, expected_length)

    def test_border_decoration(self):

        config = {
            "A": ("Silver_Face", (0.25, 0.25)),
            "B": ("Broken_Sundial", (0.25, 0.75)),
            "C": ("Great_Waterwheel", (0.75, 0.75)),
        }
        t = generate_territory(config)
        realm = realmify(t, 20, 11, filler_char="·", border_decoration=True)
        self.assert_equal_realms(realm, EXPECTED_MAP_WITH_DECORATION)


if __name__ == "__main__":
    unittest.main()
