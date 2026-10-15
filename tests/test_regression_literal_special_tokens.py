from cost_xray import analyze


def test_literal_control_token_strings_are_counted_as_text():
    text = "Show <|endoftext|> literally."
    assert analyze.ntok(text) == len(analyze._ENC.encode(text, disallowed_special=()))
    assert analyze.analyze({"messages": [{"role": "user", "content": text}]})["used"] > 0
