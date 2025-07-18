
import os
from datetime import datetime

def master_index_generator():
    folder = "archive_split"
    index_file = "00_Master_Index.txt"

    if not os.path.exists(folder):
        print(f"❌ Folder not found: {folder}")
        return

    entries = []
    for filename in sorted(os.listdir(folder)):
        if not filename.endswith(".txt"):
            continue
        path = os.path.join(folder, filename)
        line_count = sum(1 for _ in open(path, "r", encoding="utf-8"))
        created = datetime.fromtimestamp(os.path.getctime(path)).strftime("%Y-%m-%d")
        entries.append(f"• {filename} — [{folder}], {line_count} lines, created {created}")

    with open(index_file, "w", encoding="utf-8") as out:
        out.write("\n".join(entries))

    print(f"📜 Master index saved to '{index_file}'")
