import json

import pytest

from cost_xray import count_tokens as ct


@pytest.mark.parametrize("value", [[], None, {"invalid": True}])
def test_invalid_cache_maps_recover(monkeypatch, tmp_path, value):
    path = tmp_path / "tokens.json"
    path.write_text(json.dumps(value))
    monkeypatch.setattr(ct, "_TOOL_STORE", path)
    ct._TOOL_CACHE.clear()

    def http(payload, headers):
        return 100 + 10 * len(payload.get("tools", []))

    tools = [{"name": "fixture"}]
    assert ct.tools_exact(tools, "fixture", _http=http, now=1000) == [10]
