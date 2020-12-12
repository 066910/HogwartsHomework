import pytest

from Homework1212.Calculator import Calculator


class TestCalculator:

    def setup_class(self):
        self.cal = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a, b, expected", [
        (3, 4, 7), (-1, -5, -6), (1000, 2500, 3500), (1.6, 2.5, 4.1), (-1, 1, 0)
    ], ids=["int", "minus", "bingint", "decimal", "zero"])
    def test_add(self, a, b, expected):
        assert self.cal.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (4, 3, 1), (-1, -5, 4), (3500, 2500, 1000), (2.6, 1.5, 1.1), (-1, -1, 0)
    ], ids=["int", "minus", "bingint", "decimal", "zero"])
    def test_sub(self, a, b, expected):
        assert self.cal.sub(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (4, 3, 12), (-1, -5, 5), (3500, 2500, 8750000), (2.5, 1.5, 3.75), (-1, 0, 0), (-3, 3, -9)
    ], ids=["int", "minus", "bingint", "decimal", "zero", "nega_result"])
    def test_mul(self, a, b, expected):
        assert self.cal.mul(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (4, 2, 2), (-5, -1, 5), (3500, 1000, 3.5), (4.5, 1.5, 3), (0, 3, 0), (-9, 3, -3)
    ], ids=["int", "minus", "bingint", "decimal", "zero", "nega_result"])
    def test_div(self, a, b, expected):
        assert self.cal.div(a, b) == expected
