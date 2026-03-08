import pytest

from libcolor.colorspace import srgb


@pytest.fixture
def color1() -> srgb.Color:
    return srgb.Color(0, 0, 0)  # black


@pytest.fixture
def color2() -> srgb.Color:
    return srgb.Color(255, 255, 255)  # white


@pytest.fixture
def color3() -> srgb.Color:
    return srgb.Color(143, 188, 143)  # darkseagreen


@pytest.fixture
def normalized_color1() -> srgb.NormalizedColor:
    return srgb.NormalizedColor(0.0, 0.0, 0.0)


@pytest.fixture
def normalized_color2() -> srgb.NormalizedColor:
    return srgb.NormalizedColor(1.0, 1.0, 1.0)


@pytest.fixture
def normalized_color3() -> srgb.NormalizedColor:
    return srgb.NormalizedColor(0.5607843137, 0.737254902, 0.5607843137)


@pytest.fixture
def linearized_color1() -> srgb.LinearizedColor:
    return srgb.LinearizedColor(0.0, 0.0, 0.0)


@pytest.fixture
def linearized_color2() -> srgb.LinearizedColor:
    return srgb.LinearizedColor(1.0, 1.0, 1.0)


@pytest.fixture
def linearized_color3() -> srgb.LinearizedColor:
    return srgb.LinearizedColor(
        0.27467731206038465, 0.5028864580325687, 0.27467731206038465
    )


class TestColor:
    def test_from_hex_str(self, color1, color2, color3) -> None:
        assert srgb.Color.from_hex_str("000") == color1
        assert srgb.Color.from_hex_str("FFFFFF") == color2
        assert srgb.Color.from_hex_str("#8FBC8F") == color3

    def test_lt(self, color1, color2) -> None:
        assert color1 < color2
        assert not color2 < color1
        assert not color1 < color1

    def test_le(self, color1, color2) -> None:
        assert color1 <= color2
        assert not color2 <= color1
        assert color1 <= color1

    def test_gt(self, color1, color2) -> None:
        assert not color1 > color2
        assert color2 > color1
        assert not color2 > color2

    def test_ge(self, color1, color2) -> None:
        assert not color1 >= color2
        assert color2 >= color1
        assert color2 >= color2

    def test_str(self, color1, color2, color3) -> None:
        assert "rgb(0, 0, 0)" == str(color1)
        assert "rgb(255, 255, 255)" == str(color2)
        assert "rgb(143, 188, 143)" == str(color3)

    def test_repr(
        self, color1: srgb.Color, color2: srgb.Color, color3: srgb.Color
    ) -> None:
        assert "srgb.Color(0, 0, 0)" == repr(color1)
        assert "srgb.Color(255, 255, 255)" == repr(color2)
        assert "srgb.Color(143, 188, 143)" == repr(color3)


class TestNormalizedColor:
    def test_from_rgb_color(
        self,
        color1: srgb.Color,
        color2: srgb.Color,
        color3: srgb.Color,
        normalized_color1: srgb.NormalizedColor,
        normalized_color2: srgb.NormalizedColor,
        normalized_color3: srgb.NormalizedColor,
    ) -> None:
        assert srgb.NormalizedColor.from_rgb_color(color1) == normalized_color1
        assert srgb.NormalizedColor.from_rgb_color(color2) == normalized_color2
        assert srgb.NormalizedColor.from_rgb_color(color3) == normalized_color3

    def test_str(
        self,
        normalized_color1: srgb.NormalizedColor,
        normalized_color2: srgb.NormalizedColor,
        normalized_color3: srgb.NormalizedColor,
    ) -> None:
        assert "rgb(0.000, 0.000, 0.000)" == str(normalized_color1)
        assert "rgb(1.000, 1.000, 1.000)" == str(normalized_color2)
        assert "rgb(0.561, 0.737, 0.561)" == str(normalized_color3)


class TestLinearizedColor:
    def test_from_rgb_color(
        self,
        linearized_color1: srgb.LinearizedColor,
        linearized_color2: srgb.LinearizedColor,
        linearized_color3: srgb.LinearizedColor,
        color1: srgb.Color,
        color2: srgb.Color,
        color3: srgb.Color,
    ) -> None:
        assert linearized_color1 == srgb.LinearizedColor.from_rgb_color(color1)
        assert linearized_color2 == srgb.LinearizedColor.from_rgb_color(color2)
        assert linearized_color3 == srgb.LinearizedColor.from_rgb_color(color3)
