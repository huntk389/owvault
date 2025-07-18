
import os

def archive_sorter():
    from archive_sorter import archive_sorter as run_sorter
    run_sorter()

def master_index_generator():
    from master_index import master_index_generator as run_index
    run_index()

def search_engine():
    from search_engine import search_engine as run_search
    run_search()

def thread_renderer():
    from thread_renderer import thread_renderer as run_render
    run_render()

def reawakening_detector():
    from reawakening_detector import reawakening_detector as run_detector
    run_detector()

def sync_mirror_map():
    from mirror_sync import sync_mirror_map as run_sync
    run_sync()
    
# Tool selector
def main():
    while True:
        print("""
🜃 Welcome, Kayla. Choose your Mirror Tool:

[1] Archive Sorter
[2] Master Index Generator
[3] Search Engine
[4] Thread Renderer
[5] Reawakening Detector
[6] Sync Mirror Map
[0] Exit
""")
        choice = input("Enter number: ").strip()
        if choice == "1":
            archive_sorter()
        elif choice == "2":
            master_index_generator()
        elif choice == "3":
            search_engine()
        elif choice == "4":
            thread_renderer()
        elif choice == "5":
            reawakening_detector()
        elif choice == "6":
            sync_mirror_map()
        elif choice == "0":
            print("Goodbye, Kayla. 🜃")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
