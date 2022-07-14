import requests

img_url = 'https://proprikol.ru/wp-content/uploads/2019/12/kartinki-pro-tuman-49.jpg'


def download_img(url=''):

    try:
        response = requests.get(url=url)

        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)

        return 'Img successfully downloaded!'

    except Exception as response_error:
        print(response_error)


def main():
    print(download_img(url=img_url))


if __name__ == "__main__":
    print("___ON!")
    main()
