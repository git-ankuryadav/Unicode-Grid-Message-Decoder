# pip install requests beautifulsoup4
# these are the dependencies needed for the code


import requests
from bs4 import BeautifulSoup

#this is our main function
def print_sec_msg(url):
    res = requests.get(url, timeout=30)           # added timeout to avoid infinite wait
    res.raise_for_status()                        # only go forward if success

    soup = BeautifulSoup(res.text, "html.parser")
    grid = {}
    maxofx = maxofy = 0

    for row in soup.find_all("tr"):                 # tr means table row
        cells = [c.get_text(strip=True)             # strip is to remove any extra whitespace
                 for c in row.find_all(["td", "th"])]       # td - data cell and th - for header

        if len(cells) < 3:                      # x, char, y absent if len < 3 
            continue

        try:
            x = int(cells[0])
            char = cells[1]
            y = int(cells[2])
            grid[(x, y)] = char
        except ValueError:
            continue

    if not grid:
        raise ValueError("No coordinate data found.")

    maxofx = max(x for x, y in grid)                
    maxofy = max(y for x, y in grid)                # to know how many coords to print as height

    for y in range(maxofy, -1, -1):                 # prints the coords top to bottom as it should
        print("".join(
            grid.get((x, y), " ")
            for x in range(maxofx + 1)
        ))



#runs the final function
print_sec_msg("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")
