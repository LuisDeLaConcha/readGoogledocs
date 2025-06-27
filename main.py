import requests
from bs4 import BeautifulSoup


def print_secret_message_from_gdoc(url):
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)
    response.raise_for_status()
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    text = body.get_text(separator='\n').strip()
    lines = [line.strip() for line in text.split('\n') if line.strip()]

    # Find the index of the first line that is an integer (start of data)
    start_idx = 0
    for i, line in enumerate(lines):
        try:
            int(line)
            start_idx = i
            break
        except ValueError:
            continue

    # Now parse triplets from start_idx
    triplets = []
    for i in range(start_idx, len(lines), 3):
        try:
            x = int(lines[i])
            char = lines[i + 1]
            y = int(lines[i + 2])
            triplets.append((x, y, char))
        except (ValueError, IndexError):
            # If anything goes wrong (bad format or incomplete data), stop parsing
            break

    max_x = max(x for x, y, c in triplets)
    max_y = max(y for x, y, c in triplets)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, c in triplets:
        grid[y][x] = c

    for row in grid:
        print(''.join(row))


# Use the published URL
print_secret_message_from_gdoc(
    "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub"
)
