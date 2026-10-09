import json

from cost_xray import materialize


def test_truncated_capture_invalidates_saved_offset(tmp_path):
    (tmp_path / "raw.jsonl").write_text("")
    (tmp_path / "derived.jsonl").write_text("{}\n")
    (tmp_path / "summary.json").write_text(
        json.dumps(
            {
                "agent": "claude",
                "n_turns": 1,
                "logic_version": materialize.LOGIC_VERSION,
                "raw_offset": 100,
            }
        )
    )
    _, count, offset = materialize._load_state(tmp_path, "claude")
    assert (count, offset) == (0, 0)
