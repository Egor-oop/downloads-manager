import os
from pathlib import Path

downloads_dir = Path().home() / 'Downloads'
media_suffixes = ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.png', '.jpg', '.jpeg', '.gif', '.mp3', '.ogg', '.wav']
document_suffixes = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.py', '.txt', '.rtf', '.ppt', '.pptx', '.html', '.zip']


def manage(media_dir: str, documents_dir: str) -> None:
    if not os.path.exists(media_dir):
        os.mkdir(media_dir)
    if not os.path.exists(documents_dir):
        os.mkdir(documents_dir)

    for path in os.listdir(downloads_dir):
        if os.path.splitext(path)[1].lower() in media_suffixes:
            os.replace(f'{downloads_dir}/{path}', f'{media_dir}/{path}')
        elif os.path.splitext(path)[1].lower() in document_suffixes:
            os.replace(f'{downloads_dir}/{path}', f'{documents_dir}/{path}')
