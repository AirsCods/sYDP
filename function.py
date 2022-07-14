import requests

img_url = 'https://proprikol.ru/wp-content/uploads/2019/12/kartinki-pro-tuman-49.jpg'
video_url = 'https://openseauserdata.com/files/9f1e2635a6679000fb1b8db992d3552f.mp4#t=0.001'

def download_img(url=''):

    try:
        response = requests.get(url=url)

        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)

        return 'Img successfully downloaded!'

    except Exception as response_error:
        print(response_error)


def download_video(url=''):

    try:
        response = requests.get(url=url)

        with open('req_video.mp4', 'wb') as file:
            file.write(response.content)

        return 'Video successfully downloaded!'

    except Exception as response_error:
        print(response_error)


def main():
    print(download_img(url=img_url))
    print(download_video(url=video_url))


if __name__ == "__main__":
    print("___ON!")
    main()
