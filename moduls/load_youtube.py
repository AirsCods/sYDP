from pytube import YouTube
from pytube import Playlist


def download_playlist(url: str, type_to_load: str) -> None:
    p = Playlist(url=url)
    # print(*p, sep='\n')
    for url in p.video_urls:
        print(url)
        downloader(url=url, type_to_load=type_to_load)
    print(f'Download playlist complete: {p.title}')


def downloader(url: str, type_to_load: str) -> None:
    """Load file in youtube"""
    print('Start to load!')
    try:
        yt_object = YouTube(url=url)
        if type_to_load == 'audio':
            yt_object.streams.filter(type=type_to_load, abr='128kbps').first().\
                download(output_path='../load_file/audio', filename=f'{yt_object.title}.mp3')
            print(f'Audio file was download: {yt_object.title}')

        elif type_to_load == 'video':
            yt_object.streams.filter(progressive=True, res='720p').first().\
                download(output_path='../load_file/video', filename=f'{yt_object.title}.mp4')
            print(f'Video file was download: {yt_object.title}')

    except Exception as error:
        print("Whats wrong!!!")
        print(error)


if __name__ == '__main__':
    print('ON')