package cart

import "testing"

func TestMessage(t *testing.T) {
	t.Run("formats the message", func(t *testing.T) {
		if Message() != "CRT-14: shown in Go" {
			t.Error("CRT-14: wrong message")
		}
	})
}
