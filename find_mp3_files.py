import os


def find_files(current_path,):
    track_list = list()
    for f in os.scandir(current_path):
        if f.is_file() and f.path.split('.')[-1].lower() == 'mp3':
            track_list.append(os.path.basename(f.path))
    return track_list
