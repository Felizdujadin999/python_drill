import pathlib
from pathlib import Path

package = pathlib.Path.home()
new_folder = package / "Practice Files Folder"
new_folder.mkdir(exist_ok=True)

document_folder = new_folder / "documents"
document_folder.mkdir(exist_ok=True)

sub_folder2 = document_folder / "sub folder"
sub_folder2.mkdir(exist_ok=True)

file_paths = [
    document_folder / "images1.png",
    document_folder / "images2.gif",
    document_folder / "images3.png",
    document_folder / "images4.jpg"
]
for file in file_paths:
    file.touch(exist_ok=True)

image_folder = new_folder / "Images"
image_folder.mkdir(exist_ok=True)

source = document_folder / "images1.png"
destination = image_folder / "images1.png"
source.replace(destination)

source = document_folder / "images2.gif"
destination = image_folder / "images2.gif"
source.replace(destination)

source = document_folder / "images3.png"
destination = image_folder / "images3.png"
source.replace(destination)

source = document_folder / "images4.jpgg"
destination = image_folder / "images4.jpg"
source.replace(destination)

