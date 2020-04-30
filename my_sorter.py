import os
import mp3_tagger  # https://pypi.org/project/mp3-tagger/
from parse_argument import parse_arguments
from find_mp3_files import find_files
from music_info import MusicInfo


def rename(new_name, old_name, path_to_file):
    """
    Переименовывает файл
    :param new_name: новое имя файла
    :param old_name: старое имя файла
    :param path_to_file: путь до файла
    """
    mp3_old_name = os.path.join(path_to_file, old_name)
    mp3_new_name = os.path.join(path_to_file, new_name)
    os.rename(mp3_old_name, mp3_new_name)


def move_file(from_path, to_path, mp3_info, name):
    """
    Перемещает mp3 файл из одной директории в другую
    :param from_path: изначальное местоположение файла
    :param to_path: новое местоположение файла
    :param mp3_info: информация об mp3 файле.
    Содержит название трека, артиста и альбом
    :param name: имя файла
    :return: возвращает новый путь до файла
    """
    directory_old_path = os.path.join(from_path, name)
    directory_new_path = os.path.join(to_path, mp3_info.artist,
                                      mp3_info.album, name
                                      )
    if os.path.isfile(directory_new_path):
        os.remove(directory_new_path)
    os.renames(directory_old_path, directory_new_path)
    return directory_new_path


current_path = parse_arguments.src_dir
if os.path.exists(current_path):
    track_list = find_files(current_path)
else:
    print(f'Каталог не найден: {current_path}')

for track in track_list:

    path = os.path.join(current_path, track)

    try:
        mp3 = mp3_tagger.MP3File(path)
        mp3.set_version(mp3_tagger.VERSION_2)
        work_mp3_file = MusicInfo(mp3.song, mp3.artist, mp3.album)

        if not mp3.song:
            file_name = track
        else:
            file_name = f'{work_mp3_file.track} - {work_mp3_file.artist} - {work_mp3_file.album}.mp3'
            rename(file_name, track, current_path)

        if not mp3.artist or not mp3.album:
            print(f'Файл {file_name} не может быть перенесен, так как не имеет информации об артисте или альбоме')
            pass
        else:
            file_new_location = move_file(current_path, parse_arguments.dst_dir,
                                          work_mp3_file, file_name
                                          )
            print(f'{track} -> {file_new_location}')

    except PermissionError:
        print(f'нет доступа к файлу {track}')

print('Done')
