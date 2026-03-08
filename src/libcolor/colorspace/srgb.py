from math import isclose


class Color:
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
        # Guarantee that this equality check is against a class/subclass of the same type
        assert isinstance(other, Color)

        # Same colors if all color chanels match
        if (
            self.red == other.red
            and self.green == other.green
            and self.blue == other.blue
        ):
            return True

        # Differing colors otherwise
        return False

    def __lt__(self, other) -> bool:
        # Guarantee that this less-than check is against a class/subclass of the same type
        assert isinstance(other, Color)

        # Treating colors as compound numbers (akin to the hex code representation), i.e. rgb(0,0,0)
        # is less than rgb(0,0,1), but rgb(1,0,0) is greater than rgb(0,0,1).
        if self.red >= other.red:
            return False

        if self.green >= other.green:
            return False

        if self.blue >= other.blue:
            return False

        return True

    def __le__(self, other) -> bool:
        # Guarantee that this less-than-or-equal check is against a class/subclass of the same type
        assert isinstance(other, Color)

        # Treating colors as compound numbers (akin to the hex code representation), i.e. rgb(0,0,0)
        # is less than rgb(0,0,1), but rgb(1,0,0) is greater than rgb(0,0,1).
        if self.red > other.red:
            return False

        if self.green > other.green:
            return False

        if self.blue > other.blue:
            return False

        return True

    def __gt__(self, other) -> bool:
        # Guarantee that this less-than-or-equal check is against a class/subclass of the same type
        assert isinstance(other, Color)

        # Treating colors as compound numbers (akin to the hex code representation), i.e. rgb(0,0,0)
        # is less than rgb(0,0,1), but rgb(1,0,0) is greater than rgb(0,0,1).
        if self.red <= other.red:
            return False

        if self.green <= other.green:
            return False

        if self.blue <= other.blue:
            return False

        return True

    def __ge__(self, other) -> bool:
        # Guarantee that this less-than-or-equal check is against a class/subclass of the same type
        assert isinstance(other, Color)

        # Treating colors as compound numbers (akin to the hex code representation), i.e. rgb(0,0,0)
        # is less than rgb(0,0,1), but rgb(1,0,0) is greater than rgb(0,0,1).
        if self.red < other.red:
            return False

        if self.green < other.green:
            return False

        if self.blue < other.blue:
            return False

        return True

    def __str__(self) -> str:
        return f"rgb({self.red}, {self.green}, {self.blue})"

    def __repr__(self) -> str:
        return f"srgb.Color({self.red}, {self.green}, {self.blue})"

    @classmethod
    def from_hex_str(cls, hexcode: str) -> Color:
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
        return Color(red, green, blue)


class NormalizedColor:
    def __init__(self, red: float, green: float, blue: float) -> None:
        # Check validity of input parameters
        assert type(red) is float and red >= 0 and red <= 1
        assert type(green) is float and green >= 0 and green <= 1
        assert type(blue) is float and blue >= 0 and blue <= 1

        # Set color variables
        self.red: float = red
        self.green: float = green
        self.blue: float = blue

    def __eq__(self, other) -> bool:
        # Guarantee that this equality check is against a class/subclass of the same type
        assert isinstance(other, NormalizedColor)

        equal_color_channel_values = (
            isclose(self.red, other.red)
            and isclose(self.green, other.green)
            and isclose(self.blue, other.blue)
        )

        # If all channels are identical, then the colors are the same
        return equal_color_channel_values

    @classmethod
    def from_rgb_color(cls, color: Color) -> NormalizedColor:
        # Convert from standard rgb to normalized colors
        red: float = color.red / 255
        green: float = color.green / 255
        blue: float = color.blue / 255

        # Construct a new NormalizedColor object
        return NormalizedColor(red, green, blue)


class LinearizedColor:
    def __init__(self, red: float, green: float, blue: float) -> None:
        # Check validity of input paramters
        assert type(red) is float and red >= 0.0 and red <= 1.0
        assert type(green) is float and green >= 0.0 and green <= 1.0
        assert type(blue) is float and blue >= 0.0 and blue <= 1.0

        # Set color variables
        self.red: float = red
        self.green: float = green
        self.blue: float = blue

    def __eq__(self, other) -> bool:
        # Guarantee that this equality check is against a class/subclass of the same type
        assert isinstance(other, LinearizedColor)

        # Same colors if all color chanels match
        if (
            self.red == other.red
            and self.green == other.green
            and self.blue == other.blue
        ):
            return True

        # Differing colors otherwise
        return False

    @classmethod
    def from_rgb_color(cls, rgb_color: Color):
        def _linearize(color_value: float) -> float:
            if 0.04045 > color_value:
                return color_value / 12.95
            else:
                return ((color_value + 0.055) / 1.055) ** 2.4

        # Linearize the color-chanel values
        new_red = _linearize(rgb_color.red / 255)
        new_green = _linearize(rgb_color.green / 255)
        new_blue = _linearize(rgb_color.blue / 255)

        # Construct a new linearize sRGB color object
        return LinearizedColor(new_red, new_green, new_blue)
