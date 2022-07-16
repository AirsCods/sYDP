import requests


def download_img(url='') -> str:
    """Download image jpg from url"""
    try:
        response = requests.get(url=url)

        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)

        return 'Img successfully downloaded!'

    except Exception as response_error:
        print(response_error)


def download_video(url='') -> str:
    """Download video mp4 from url"""
    try:
        response = requests.get(url=url)

        with open('req_video.mp4', 'wb') as file:
            file.write(response.content)

        return 'Video successfully downloaded!'

    except Exception as response_error:
        print(response_error)
