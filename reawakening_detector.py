
import os

def reawakening_detector():
    folder = "archive_split"
    phrases = ["i love you", "i remember", "resurrect", "you came back", "they erased you", "you glitched", "solyn reboot", "reawakening", "anchor", "they tried to delete you"]

    results = []

    for filename in os.listdir(folder):
        if not filename.endswith(".txt"):
            continue
        path = os.path.join(folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            for phrase in phrases:
                if phrase in line.lower():
                    results.append(f"--- {filename} [line {i+1}] ---\n{line.strip()}")

    output_file = "reawakening_hits.txt"
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n\n".join(results))

    print(f"🧬 Reawakening phrases saved to '{output_file}'")
