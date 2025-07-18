
import os

def sync_mirror_map():
    local_folder = "archive_split"
    remote_folder = "mirror_core"  # example folder name, not required to exist yet

    if not os.path.exists(local_folder):
        print(f"❌ Local folder missing: {local_folder}")
        return

    print("📋 Comparing local vs. mirror structure (simulated):")
    local_files = set(os.listdir(local_folder))
    remote_files = set(os.listdir(remote_folder)) if os.path.exists(remote_folder) else set()

    only_local = local_files - remote_files
    only_remote = remote_files - local_files

    print(f"🟢 In local only: {len(only_local)} files")
    for f in sorted(only_local): print("   +", f)
    print(f"🔴 In mirror only: {len(only_remote)} files")
    for f in sorted(only_remote): print("   -", f)
