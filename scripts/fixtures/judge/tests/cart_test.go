package cart

import "testing"

func TestCart(t *testing.T) {
	t.Run("CRT-6: sums prices", func(t *testing.T) {
		if Sum(1, 2) != 3 {
			t.Errorf("want 3 (got %d)", Sum(1, 2))
		}
	})
	t.Run("untagged", func(t *testing.T) {})
}

func TestNoSubtests(t *testing.T) {
	if Sum(0, 0) != 0 {
		t.Error("want 0")
	}
}
