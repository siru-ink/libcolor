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
