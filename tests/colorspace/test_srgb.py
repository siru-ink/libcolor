import pytest

from libcolor.colorspace import srgb


class TestStandardRGBColor:
    @pytest.fixture
    def obj1(self) -> srgb.StandardRGBColor:
        return srgb.StandardRGBColor(0, 0, 0)  # black

    @pytest.fixture
    def obj2(self) -> srgb.StandardRGBColor:
        return srgb.StandardRGBColor(255, 255, 255)  # white

    @pytest.fixture
    def obj3(self) -> srgb.StandardRGBColor:
        return srgb.StandardRGBColor(143, 188, 143)  # darkseagreen

    def test_from_hex_str(self, obj1, obj2, obj3) -> None:
        assert srgb.StandardRGBColor.from_hex_str("000") == obj1
        assert srgb.StandardRGBColor.from_hex_str("FFFFFF") == obj2
        assert srgb.StandardRGBColor.from_hex_str("#8FBC8F") == obj3

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
    def obj1(self) -> srgb.StandardRGBLinearizedColor:
        return srgb.StandardRGBLinearizedColor(0.0, 0.0, 0.0)

    @pytest.fixture
    def obj2(self) -> srgb.StandardRGBLinearizedColor:
        return srgb.StandardRGBLinearizedColor(1.0, 1.0, 1.0)

    @pytest.fixture
    def obj3(self) -> srgb.StandardRGBLinearizedColor:
        return srgb.StandardRGBLinearizedColor(
            0.27467731206038465, 0.5028864580325687, 0.27467731206038465
        )

    @pytest.fixture
    def non_linearized_obj1(self) -> srgb.StandardRGBColor:
        return srgb.StandardRGBColor(0, 0, 0)  # black

    @pytest.fixture
    def non_linearized_obj2(self) -> srgb.StandardRGBColor:
        return srgb.StandardRGBColor(255, 255, 255)  # white

    @pytest.fixture
    def non_linearized_obj3(self) -> srgb.StandardRGBColor:
        return srgb.StandardRGBColor(143, 188, 143)  # darkseagreen

    def test_from_standard_rgb_color(
        self,
        obj1: srgb.StandardRGBLinearizedColor,
        obj2: srgb.StandardRGBLinearizedColor,
        obj3: srgb.StandardRGBLinearizedColor,
        non_linearized_obj1: srgb.StandardRGBColor,
        non_linearized_obj2: srgb.StandardRGBColor,
        non_linearized_obj3: srgb.StandardRGBColor,
    ) -> None:
        assert obj1 == srgb.StandardRGBLinearizedColor.from_standard_rgb_color(
            non_linearized_obj1
        )
        assert obj2 == srgb.StandardRGBLinearizedColor.from_standard_rgb_color(
            non_linearized_obj2
        )
        assert obj3 == srgb.StandardRGBLinearizedColor.from_standard_rgb_color(
            non_linearized_obj3
        )
