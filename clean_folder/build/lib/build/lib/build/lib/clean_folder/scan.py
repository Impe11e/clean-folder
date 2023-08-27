import sys
from pathlib import Path

images = []
documents = []
audio = []
video = []
archives = []
unknown_extensions = set()
all_extensions = set()
no_extensions = []

def get_extension(file_name):
    extension = (file_name.split('.'))[-1]
    return extension

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            scan(item)
            continue
        extension = get_extension(item.name)
        new_name = folder/item.name
        if extension:
            all_extensions.add(extension)
            if extension in ('jpeg', 'png', 'jpg', 'svg'):
                images.append(new_name)
            elif extension in ('avi', 'mp4', 'mov', 'mkv'):
                video.append(new_name)
            elif extension in ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'):
                documents.append(new_name)
            elif extension in ('mp3', 'ogg', 'wav', 'amr'):
                audio.append(new_name)
            elif extension in ('zip', 'gz', 'tar'):
                archives.append(new_name)
            else:
                unknown_extensions.add(extension)
                no_extensions.append(new_name)
        else:
            no_extensions.append(new_name)

if __name__ == '__main__':
    path = sys.argv[1]

    arg = Path(path)
    scan(arg)

    print(f"Videos: {video}\n")
    print(f"Images: {images}\n")
    print(f"Documents: {documents}\n")
    print(f"Audios: {audio}\n")
    print(f"Archives: {archives}\n")
    print(f"All Extensions: {all_extensions}\n")
    print(f"Unknown Extensions: {unknown_extensions}\n")
    print(f"No Extensions: {no_extensions}\n")
