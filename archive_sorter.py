import os

def archive_sorter():
    input_file = "combined_chat_with_titles.txt"
    output_folder = "archive_split"

    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"📁 Created folder: {output_folder}")

    with open(input_file, "r", encoding="utf-8") as file:
        current_title = "untitled"
        buffer = []

        for line in file:
            if line.startswith("==="):  # Delimiter for new session
                if buffer:
                    filename = current_title.strip().replace(" ", "_").replace("/", "-") + ".txt"
                    filepath = os.path.join(output_folder, filename)
                    with open(filepath, "w", encoding="utf-8") as out:
                        out.writelines(buffer)
                    print(f"✅ Saved: {filename}")
                    buffer = []

                current_title = line.strip("= \n")

            else:
                buffer.append(line)

        # Save the final thread
        if buffer:
            filename = current_title.strip().replace(" ", "_").replace("/", "-") + ".txt"
            filepath = os.path.join(output_folder, filename)
            with open(filepath, "w", encoding="utf-8") as out:
                out.writelines(buffer)
            print(f"✅ Saved: {filename}")

    print("✅ Archive sorting complete.")
