import pytest

from cost_xray import analyze


@pytest.mark.parametrize("value", ["0", "-1"])
def test_invalid_window_override_keeps_model_capacity(monkeypatch, value):
    monkeypatch.delenv("COST_XRAY_WINDOW", raising=False)
    expected = analyze.window_for("claude-fixture")
    monkeypatch.setenv("COST_XRAY_WINDOW", value)
    assert analyze.window_for("claude-fixture") == expected
