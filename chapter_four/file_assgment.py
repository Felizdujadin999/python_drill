import pathlib
from pathlib import Path
# 1
package = pathlib.Path.home()
new_folder = package / "my_folder"
new_folder.mkdir(exist_ok=True)
# 2
file_paths = [
    new_folder / "file1.txt",
    new_folder / "file2.txt",
    new_folder / "image1.png"
]
for file in file_paths:
    file.touch(exist_ok=True)

image_folder = new_folder / "Images"
image_folder.mkdir(exist_ok=True)
# 3
source = new_folder / "image1.png"
destination = image_folder / "image1.png"
source.replace(destination)
# 4
delete_file = new_folder / "file1.txt"
delete_file.unlink(missing_ok=True)

delete_file2 = new_folder / "file2.txt"
delete_file2.unlink(missing_ok=True)

delete_file3 = image_folder / "image1.png"
delete_file3.unlink(missing_ok=True)
# 5
delete_folder = new_folder / "Images"
delete_folder.rmdir()

delete_folder2 = package / "my_folder"
delete_folder2.rmdir()
