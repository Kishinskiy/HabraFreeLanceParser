from fake_headers import Headers
from Parser import Parser


def main():
    header = Headers(
        browser="chrome",
        os="win",
        headers=True
    )

    parser = Parser(header.generate())

    parser.get_links_from_all_pages()


if __name__ == '__main__':
    main()

