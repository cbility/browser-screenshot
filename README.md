
# Browser Screenshot Utility

Automate browser screenshots for a list of URLs using Playwright.

**Prerequisites:**
- Python 3.8+ (available from [Microsoft Store](https://apps.microsoft.com/detail/9NCVDN91XZQP) )

- [uv](https://docs.astral.sh/uv/getting-started/installation) (for fast Python package management)

## Installation

First, clone this repository locally. Open a command line in the directory where you would like to store it and run 
```powershell
git clone https://github.com/cbility/browser-screenshot
```
then
```powershell
cd .\browser-screenshot\
```

To install the project run:

```powershell
uv install
uv run playwright install
```



## Configuration

1. Create a CSV file at `config/urls.csv` containing one URL or domain per line. Example:

	```csv
	example.com
	duckduckgo.com
	https://github.com
	```

2. The script will automatically prepend `https://` to domains that do not start with `http://` or `https://`.

## Usage

Run the screenshot script from the project root:

```powershell
uv run -m src.main
```

## Output

- Screenshots are saved to the `screenshots/` directory.
- Each screenshot is named as `<domain>_<timestamp>.png`.
- The script prints the relative path to each saved screenshot.

## Example Output

```
Starting browser screenshot for the following URLs:
 - https://example.com
 - https://duckduckgo.com
Navigating to https://example.com...
Taking screenshot and saving to screenshots/example_com_20251029_124021.png...
Navigating to https://duckduckgo.com...
Taking screenshot and saving to screenshots/duckduckgo_com_20251029_124022.png...
```
