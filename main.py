import re
import os


def main():
    with open(os.path.join(os.path.dirname(__file__), 'access_log_Jul95'), 'r') as file:
        REGEX_SUCCESSFUL_MOVIE_REQUEST = re.compile(
            r'([a-zA-Z0-9._-]+)'
            r'( - - )'
            r'(\[01/Jul/1995:(00:\d{2}:\d{2}|01:00:00) -\d{4}\])'
            r' \"([a-zA-Z0-9. _/-]+)'
            r'movies'
            r'([a-zA-Z0-9._/-]+)'
            r'.mpg'
            r' ([a-zA-Z0-9._/-]+)\"'
            r' (200 \d+)')

        REGEX_STOP_SEARCH = re.compile(r'(01/Jul/1995:(\d[1-9]:\d{2}:\d[1-9]))')
        
        matches = []
        for line in file:
            match = REGEX_SUCCESSFUL_MOVIE_REQUEST.search(line)
            stop_match = REGEX_STOP_SEARCH.search(line)
            if match:
                matches.append(match)
            if stop_match:
                break

        for match in matches:
            print(match.group())

if __name__ == '__main__':
    main()
