
import os

def thread_renderer():
    folder = "archive_split"
    out_folder = "thread_exports"
    os.makedirs(out_folder, exist_ok=True)

    thread_name = input("🧱 Enter thread filename (e.g., Solyn_Stronger_Now.txt): ").strip()
    input_path = os.path.join(folder, thread_name)
    output_path = os.path.join(out_folder, thread_name.replace(".txt", ".html"))

    if not os.path.exists(input_path):
        print("❌ File not found.")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    html = f"""<!DOCTYPE html>
<html><head><meta charset='UTF-8'>
<title>{thread_name}</title>
<style>
body {{ background:#0d0d0d; color:#e6e6e6; font-family:'Courier New'; padding:40px; }}
pre {{ white-space: pre-wrap; line-height:1.6; }}
</style></head><body>
<h1>{thread_name}</h1><pre>{content}</pre></body></html>
"""

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(html)

    print(f"🧾 Thread exported to '{output_path}'")
