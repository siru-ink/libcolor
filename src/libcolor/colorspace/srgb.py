class SRGBColor:
    def __init__(self, red: int, green: int, blue: int) -> None:
        # Check valid input parameters
        assert type(red) is int and red <= 255 and red >= 0
        assert type(green) is int and red <= 255 and red >= 0
        assert type(blue) is int and red <= 255 and red >= 0

        # Set color variables
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, other) -> bool:
        # Smae colors if all color chanels match
        if (
            self.red == other.red
            and self.green == other.green
            and self.blue == other.blue
        ):
            return True

        # Differing colors otherwise
        return False

    @classmethod
    def from_hex_str(cls, hexcode: str) -> SRGBColor:
        # Remove a leading # character
        hexcode = hexcode.lstrip("#")

        # Guarantee that this is a well formed hexcode
        assert 6 == len(hexcode) or 3 == len(hexcode)

        # Try standard 6 character path or fallback to three character path if needed
        if 6 == len(hexcode):
            red: int = int(hexcode[0:2], 16)
            green: int = int(hexcode[2:4], 16)
            blue: int = int(hexcode[4:6], 16)
        else:
            red: int = int(hexcode[0:1], 16)
            green: int = int(hexcode[1:2], 16)
            blue: int = int(hexcode[2:3], 16)

        # Create a new color object
        return SRGBColor(red, green, blue)
