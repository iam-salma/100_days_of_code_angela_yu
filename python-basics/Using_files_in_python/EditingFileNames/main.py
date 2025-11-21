import os

# Set your main data folder path
data_folder = r"path/to/your/data"

renamed_count = 0
skipped_count = 0

# Walk through all subdirectories
for root, dirs, files in os.walk(data_folder):
    for filename in files:
        if ' ' in filename:
            # Replace spaces with underscores
            new_filename = filename.replace(' ', '_')
            
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, new_filename)
            
            # Check if source and destination are different
            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"✅ Renamed: {old_path} → {new_filename}")
                    renamed_count += 1
                except Exception as e:
                    print(f"❌ Error renaming {filename}: {e}")
            else:
                skipped_count += 1
        else:
            skipped_count += 1

print(f"\n📊 Summary: {renamed_count} files renamed, {skipped_count} files skipped")
