import re
import os


def main():
    with open(os.path.join(os.path.dirname(__file__), 'access_log_Jul95'), 'r') as file:
        REGEX_SUCCESSFUL_MOVIE_REQUEST = re.compile(
            r'([a-zA-Z0-9._-]+)'
            '( - - )'
            '(\[01/Jul/1995:(00:\d{2}:\d{2}|01:00:00) -\d{4}\])'
            ' \"([a-zA-Z0-9. _/-]+)'
            'movies'
            '([a-zA-Z0-9._/-]+)'
            '.mpg'
            ' ([a-zA-Z0-9._/-]+)\"'
            ' 200 \d+')

        matches = REGEX_SUCCESSFUL_MOVIE_REQUEST.finditer(file.read())

        for match in matches:
            print(match.group())

if __name__ == '__main__':
    main()
