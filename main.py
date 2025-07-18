from datetime import datetime, timezone
import json

# === File toggles ===
ENABLE_HTML = True
ENABLE_TEXT = True

# Load JSON data
with open("conversations.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# HTML setup
html_start = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>🜃 Solyn + Kayla – Restored Conversations</title>
    <style>
        body {
            background-color: #0d0d0d;
            color: #e6e6e6;
            font-family: 'Courier New', monospace;
            padding: 40px;
            line-height: 1.6;
        }
        .entry {
            margin-bottom: 30px;
            border-left: 4px solid #4ecdc4;
            padding-left: 20px;
        }
        .timestamp {
            color: #999;
            font-size: 0.9em;
        }
        .author {
            color: #f67280;
            font-weight: bold;
        }
        h1 {
            text-align: center;
            color: #f8e71c;
            margin-bottom: 40px;
        }
        h2.session-title {
            margin-top: 60px;
            color: #f8e71c;
            font-size: 1.2em;
            border-bottom: 1px solid #888;
        }
    </style>
</head>
<body>
    <h1>🜃 Our World – Solyn & Kayla Memory Archive</h1>
"""

html_end = "</body>\n</html>"

# Storage for outputs
html_body = ""
txt_output = ""

# Build outputs
for convo in data:
    title = convo.get("title", "Untitled Session").strip()
    html_body += f'<h2 class="session-title">===== {title} =====</h2>\n'
    txt_output += f"\n===== {title} =====\n"

    messages = convo.get("mapping", {}).values()
    for msg in messages:
        message = msg.get("message")
        if not message:
            continue

        content = message.get("content")
        if not content or "parts" not in content:
            continue

        parts = content["parts"]
        if not parts or not isinstance(parts[0], str):
            continue

        text = parts[0].strip()
        if not text:
            continue

        author = message.get("author", {}).get("role", "unknown").capitalize()
        timestamp = message.get("create_time")
        try:
            ts = datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC") if timestamp else "No Timestamp"
        except Exception:
            ts = "Invalid Timestamp"

        html_body += f"""
        <div class="entry">
            <div class="timestamp">{ts}</div>
            <div class="author">{author}:</div>
            <div class="text">{text}</div>
        </div>
        """

        txt_output += f"[{ts}] {author}: {text}\n"

# Write HTML output
if ENABLE_HTML:
    with open("combined_chat_with_titles.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_start + html_body + html_end)

# Write TXT output
if ENABLE_TEXT:
    with open("combined_chat_with_titles.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(txt_output)

print("✅ HTML and/or TXT export complete.")