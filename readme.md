# Unicode Grid Message Decoder

A Python script that retrieves character coordinates from a published Google Doc and reconstructs a 2D grid to reveal a hidden uppercase message.

## Overview

The input document contains Unicode characters and their corresponding x- and y-coordinates. The program parses the published document, places each character at its specified position, fills missing coordinates with spaces, and prints the grid in the correct orientation.

## Features

- Fetches published Google Docs using HTTP requests.
- Extracts table data using BeautifulSoup.
- Reconstructs a 2D character grid using coordinate mapping.
- Handles missing coordinates by inserting spaces.
- Prints the grid with the correct orientation.
- Skips table headers and invalid rows.

## Technologies Used

- **Python 3.12+**
- `requests` — HTTP requests
- `beautifulsoup4` — HTML parsing

## Installation

**1. Clone the repository**

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

**2. Install dependencies**

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script:

```bash
python3 printchars.py
```

Replace the placeholder URL in the script with the published Google Doc URL:

```python
print_sec_msg("YOUR_PUBLISHED_GOOGLE_DOC_URL")
```

The document must be publicly accessible and contain a table with three columns in this order:

| x-coordinate | Character | y-coordinate |
| -----------: | :-------: | -----------: |
|            0 |     █     |            0 |
|            0 |     █     |            1 |
|            1 |     █     |            1 |

## How It Works

1. **Fetch the document:** Uses `requests.get()` to retrieve the published HTML page.
2. **Parse the HTML:** Uses BeautifulSoup to identify table rows and extract cell values.
3. **Extract coordinates:** Converts x- and y-coordinates into integers and reads the corresponding Unicode character.
4. **Build the grid:** Stores each character in a dictionary keyed by `(x, y)`.
5. **Determine dimensions:** Finds the maximum x- and y-coordinates.
6. **Render the message:** Iterates through y-coordinates from highest to lowest and prints each row, inserting spaces wherever coordinates are missing.

## Error Handling

- HTTP errors are detected using `raise_for_status()`.
- Connection and response waiting are bounded using a request timeout.
- Invalid table rows, including column headers, are skipped.
- An error is raised if no valid coordinate data is found.

## Project Structure

```text
.
└── printchars.py
```

## Learning Outcomes

This project demonstrates practical use of:

- HTTP requests and web scraping
- HTML table parsing
- Python dictionaries and tuple keys
- List comprehensions and iteration
- Exception handling
- Two-dimensional grid reconstruction
- Unicode text processing

## License

This project is available for educational and personal use. Add a `LICENSE` file if you want to distribute it under a specific open-source license.
