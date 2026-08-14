def extract_text(result) -> str:

    if isinstance(result, str):
        return result

    if not result.content:
        return ""

    content = result.content[0]

    if hasattr(content, "text"):
        return content.text

    return str(content)