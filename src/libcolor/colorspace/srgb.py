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
