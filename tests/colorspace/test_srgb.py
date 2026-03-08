import pytest

from libcolor.colorspace import srgb


class TestStandardRGBColor:
    @pytest.fixture
    def obj1(self) -> srgb.Color:
        return srgb.Color(0, 0, 0)  # black

    @pytest.fixture
    def obj2(self) -> srgb.Color:
        return srgb.Color(255, 255, 255)  # white

    @pytest.fixture
    def obj3(self) -> srgb.Color:
        return srgb.Color(143, 188, 143)  # darkseagreen

    def test_from_hex_str(self, obj1, obj2, obj3) -> None:
        assert srgb.Color.from_hex_str("000") == obj1
        assert srgb.Color.from_hex_str("FFFFFF") == obj2
        assert srgb.Color.from_hex_str("#8FBC8F") == obj3

    def test_lt(self, obj1, obj2) -> None:
        assert obj1 < obj2
        assert not obj2 < obj1
        assert not obj1 < obj1

    def test_le(self, obj1, obj2) -> None:
        assert obj1 <= obj2
        assert not obj2 <= obj1
        assert obj1 <= obj1

    def test_gt(self, obj1, obj2) -> None:
        assert not obj1 > obj2
        assert obj2 > obj1
        assert not obj2 > obj2

    def test_ge(self, obj1, obj2) -> None:
        assert not obj1 >= obj2
        assert obj2 >= obj1
        assert obj2 >= obj2


class TestStandardRGBLiearizedColor:
    @pytest.fixture
    def obj1(self) -> srgb.LinearizedColor:
        return srgb.LinearizedColor(0.0, 0.0, 0.0)

    @pytest.fixture
    def obj2(self) -> srgb.LinearizedColor:
        return srgb.LinearizedColor(1.0, 1.0, 1.0)

    @pytest.fixture
    def obj3(self) -> srgb.LinearizedColor:
        return srgb.LinearizedColor(
            0.27467731206038465, 0.5028864580325687, 0.27467731206038465
        )

    @pytest.fixture
    def non_linearized_obj1(self) -> srgb.Color:
        return srgb.Color(0, 0, 0)  # black

    @pytest.fixture
    def non_linearized_obj2(self) -> srgb.Color:
        return srgb.Color(255, 255, 255)  # white

    @pytest.fixture
    def non_linearized_obj3(self) -> srgb.Color:
        return srgb.Color(143, 188, 143)  # darkseagreen

    def test_from_standard_rgb_color(
        self,
        obj1: srgb.LinearizedColor,
        obj2: srgb.LinearizedColor,
        obj3: srgb.LinearizedColor,
        non_linearized_obj1: srgb.Color,
        non_linearized_obj2: srgb.Color,
        non_linearized_obj3: srgb.Color,
    ) -> None:
        assert obj1 == srgb.LinearizedColor.from_standard_rgb_color(non_linearized_obj1)
        assert obj2 == srgb.LinearizedColor.from_standard_rgb_color(non_linearized_obj2)
        assert obj3 == srgb.LinearizedColor.from_standard_rgb_color(non_linearized_obj3)
