import sys
from pathlib import Path
import shutil
import clean_folder.scan
import clean_folder.normalize

def file_processing(path, root_folder, destination):
    destination_folder = root_folder/destination
    destination_folder.mkdir(exist_ok=True)
    try:
        path.replace(destination_folder / clean_folder.normalize.normalize(path.name))
    except PermissionError:
        print(f"Dont' have permission to file '{path.name}'")

def archive_processing(path, root_folder, destination):
    destination_folder = root_folder/destination
    destination_folder.mkdir(exist_ok=True)

    extension = clean_folder.scan.get_extension(path.name)

    new_name = clean_folder.normalize.normalize(path.name.replace(extension, ''))

    archive_folder = root_folder/destination/new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(archive_folder))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()

def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass

def get_folder_objects(root_path):
    for folder in root_path.iterdir():
        if folder.is_dir():
            remove_empty_folders(folder)
            try:
                folder.rmdir()
            except OSError:
                pass

def main():
    path = sys.argv[1]
    print(f'Start in {path}')
    folder_path = Path(path)

    clean_folder.scan.scan(folder_path)

    for file in clean_folder.scan.images:
        file_processing(file, folder_path, 'images')

    for file in clean_folder.scan.documents:
        file_processing(file, folder_path, 'documents')

    for file in clean_folder.scan.audio:
        file_processing(file, folder_path, 'audio')

    for file in clean_folder.scan.video:
        file_processing(file, folder_path, 'videos')

    for file in clean_folder.scan.no_extensions:
        file_processing(file, folder_path, 'unknown extensions')

    for file in clean_folder.scan.archives:
        archive_processing(file, folder_path, 'archives')

    get_folder_objects(folder_path)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f'Start in {path}')

    arg = Path(path)
    main(arg.resolve())