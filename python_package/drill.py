from pathlib import Path

file_path = Path.cwd() / "my_folder"
file_path.mkdir(exist_ok=True)
new_file_path = file_path / "my_file.txt"
new_file_path.touch()

print("Exists -", file_path.exists())
print("Exists -", new_file_path.exists())
print(new_file_path)
print("Parent -", new_file_path.parent)
print("Name -", new_file_path.name)
print("Anchor -", new_file_path.anchor)
