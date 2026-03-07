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
