# SubPulse

SubPulse is a Python-based passive subdomain enumeration and alive host detection tool designed as a modular reconnaissance pipeline. The goal of the project is to build a structured and extensible reconnaissance tool rather than a single monolithic script.

SubPulse focuses on passive intelligence gathering using publicly available data sources and provides optional live host detection for reconnaissance workflows.

---

## Features

### Passive Subdomain Enumeration
- Uses Certificate Transparency logs from crt.sh
- Fetches and parses JSON results
- Extracts domains from:
  - `common_name`
  - `name_value`
- Data cleaning:
  - Removes wildcard prefixes (`*.`)
  - Removes invalid entries and emails
  - Converts results to lowercase
  - Deduplicates results using Python sets
- Retry logic for unstable responses (502 / 503 / timeout)

### Alive Host Detection (Optional)
- Enabled using `--alive` flag
- Attempts HTTPS first, then HTTP fallback
- Hosts considered alive if:
  - HTTP status code < 500
- Handles redirects and forbidden responses
- Does not modify original enumeration results

### Output System
- Terminal output
- File output support
- UTF-8 encoding for Windows compatibility
- Summary display with statistics

### Banner System
- Dynamic banner display
- Automatically adjusts width to terminal size
- Displays active target information

---

## Project Structure
```
SubPulse/
│
├── main.py
├── banner.py
├── subDomain_enum.py
├── alive_check.py
├── output.py
├── requirements.txt
└── README.md
```
---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SubPulse.git
cd SubPulse
```
### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
```
Activate Environment
### Windows
```bash
venv\Scripts\activate\
```
### Linux / macOS
```bash
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## Usage
### Basic Enumeration
```bash
python main.py -d example.com
```
### Enumeration with Alive Host Detection
```bash
python main.py -d example.com --alive
```
### Save Output to File
```bash
python main.py -d example.com --alive -o alive.txt
```
---

## CLI Arguments

| Argument | Description |
|-----------|-------------|
| `-d`, `--domain` | Target domain (required) |
| `--alive` | Enable alive host filtering |
| `-o`, `--output` | Save results to file |

---

## Design Philosophy

- Modular architecture
- Separation of logic and output
- Passive reconnaissance only
- Graceful handling of unreliable external sources
- Single-domain execution model

---

## Known Limitations

- crt.sh may return inconsistent results due to source instability
- External API failures may affect enumeration results
- Alive detection currently runs sequentially
- Large domain scans may take time

---

## Planned Improvements

- Multiple passive data sources  
- Threaded or asynchronous alive checking  
- DNS resolution stage  
- JSON and CSV output formats  
-  Result caching  
- Progress indicators

---

### Requirements
- Python 3.8 or higher

---

### Disclaimer
- This tool is intended for educational purposes and authorized security testing only. Users are responsible for complying with applicable laws and regulations.




