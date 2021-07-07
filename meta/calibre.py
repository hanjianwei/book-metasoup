import subprocess


class Calibre:
    def __init__(self):
        pass

    def add_book(self, book):
        pass

    def update(self, bookid, book):
        pass

    def search_isbn(self, isbn):
        p = subprocess.run(
            'calibredb search "isbn:{}"'.format(isbn), shell=True, capture_output=True
        )
        return p.stdout.decode("utf-8").strip() if p.returncode == 0 else None
