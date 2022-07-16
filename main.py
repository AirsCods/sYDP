# This is main file for my project
from moduls import load_file

img_url: str = 'https://proprikol.ru/wp-content/uploads/2019/12/kartinki-pro-tuman-49.jpg'
video_url: str = 'https://openseauserdata.com/files/9f1e2635a6679000fb1b8db992d3552f.mp4#t=0.001'


def main():
    """Main start"""
    print(load_file.download_img(url=img_url))
    print(load_file.download_video(url=video_url))


if __name__ == "__main__":
    print("___ON!")
    main()
