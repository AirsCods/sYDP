def progress(self, percent):
    if percent['status'] == 'downloading':
        result = round(percent['downloaded_bytes'] / percent['total_bytes'] * 100, 1)

        print(round(percent['downloaded_bytes'] / percent['total_bytes'] * 100, 1))
        self.receiv.emit(result)


def on_progress(self, stream: Stream, chunk: bytes, bytes_remaining: int) -> None:
    filesize = stream.filesize
    bytes_received = filesize - bytes_remaining
    percent = round(100.0 * bytes_received / float(filesize), 1)
    self.receiv.emit(percent)
    print(bytes_received, filesize)