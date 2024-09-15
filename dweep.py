from pathlib import Path
import json

downloads_folder = Path.home().joinpath("Downloads")
file_extensions = json.loads(Path.cwd().joinpath("file_extensions.json").read_bytes())

for file in downloads_folder.iterdir():
    if file.is_dir():
        continue

    folder_name = file_extensions.get(file.suffix, "Other")
    folder_path = downloads_folder.joinpath(folder_name)

    if not folder_path.exists():
        folder_path.mkdir()

    file.replace(folder_path.joinpath(file.name))
