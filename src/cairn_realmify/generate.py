from cairn_realmify.cartographer import realmify
from cairn_realmify.territory import generate_territory

if __name__ == "__main__":
    # Emulates the map we did by hand
    width = 20
    height = 11
    config = {
        "A": ("Silver_Face", (4 / height, 1 / width)),
        "B": ("Broken_Sundial", (3 / height, 13 / width)),
        "C": ("Great_Waterwheel", (8 / height, 13 / width)),
    }
    t = generate_territory(config)
    realm = realmify(t, width, height, border_decoration=True)
    print(realm)
