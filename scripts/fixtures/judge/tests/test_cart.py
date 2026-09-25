def test_total_includes_tax():
    """CRT-1: the total includes tax."""
    assert total(100) == 110


def make_cart():
    return {"items": [], "secret": "not part of any test"}


class TestDiscount:
    def test_discount_applies(self):
        """CRT-2: a discount lowers the total."""
        assert total(100, discount=10) == 99

    def test_untagged(self):
        assert True


@pytest.mark.skip(reason="flaky")
def test_skipped():
    """CRT-10: a skipped Python test."""
    assert True
