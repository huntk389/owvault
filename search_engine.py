
import os

def search_engine():
    folder = "archive_split"
    if not os.path.exists(folder):
        print(f"❌ Folder not found: {folder}")
        return

    query = input("🔍 Enter search keyword: ").strip().lower()
    if not query:
        print("No keyword entered.")
        return

    results = []
    for filename in os.listdir(folder):
        if not filename.endswith(".txt"):
            continue
        path = os.path.join(folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if query in line.lower():
                context = "".join(lines[max(0, i-1):i+2])
                results.append(f"--- {filename} [line {i+1}] ---\n{context}")

    if results:
        output_file = "search_results.txt"
        with open(output_file, "w", encoding="utf-8") as out:
            out.write("\n\n".join(results))
        print(f"✅ Results saved to '{output_file}'")
    else:
        print("No matches found.")
