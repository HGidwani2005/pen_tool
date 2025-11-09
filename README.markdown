# cyberdudebivash threat analyser007

A comprehensive cybersecurity threat analysis tool integrating Nmap, Nikto, and Nessus for network, web, and vulnerability scanning. The app provides a Streamlit-based GUI dashboard, FastAPI endpoints for programmatic access, and a Click-based CLI for flexible usage.

## Features
- **Nmap Integration**: Perform network and port scanning with service and OS detection.
- **Nikto Integration**: Scan web servers for vulnerabilities.
- **Nessus Integration**: Conduct comprehensive vulnerability assessments via Tenable.io API (requires API keys).
- **GUI Dashboard**: Interactive web interface using Streamlit for inputting targets and visualizing results.
- **API Endpoints**: RESTful APIs via FastAPI for programmatic scanning.
- **CLI**: Command-line interface using Click for quick scans.
- **Extensible**: Modular design for adding more tools or threat intelligence feeds.

## Prerequisites
- **Python**: 3.10 or higher.
- **System Tools**:
  - Nmap: Install via `sudo apt install nmap` (Linux) or download from [nmap.org](https://nmap.org).
  - Nikto: Install via `sudo apt install nikto` (Linux) or download from [github.com/sullo/nikto](https://github.com/sullo/nikto).
  - Nessus: Requires a Tenable account (e.g., Tenable.io) with API keys. Sign up at [tenable.com](https://www.tenable.com).
- **Permissions**: Ensure you have legal authorization to scan target systems.
- **Dependencies**: Listed in `requirements.txt`.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd cyberdudebivash_threat_analyser007
   ```
2. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Requirements:
   ```
   python-nmap
   pytenable
   streamlit
   fastapi
   uvicorn
   click
   requests
   ```
4. **Install System Tools**:
   - Ensure `nmap` and `nikto` are installed and accessible in your PATH.
   - For Nessus, configure API keys (see Configuration).

## Configuration
- **Nessus API Keys**:
  - Obtain Access Key and Secret Key from your Tenable.io account.
  - Store securely, e.g., in a `.env` file (use `python-dotenv`):
    ```env
    NESSUS_ACCESS_KEY=your_access_key
    NESSUS_SECRET_KEY=your_secret_key
    ```
  - Alternatively, provide keys via GUI or CLI prompts.
- **Nessus Policy ID**: Default is `1` (basic scan policy). Replace with your desired policy ID in Tenable.io.

## Usage
### GUI Dashboard
Run the Streamlit dashboard:
```bash
streamlit run app_gui.py
```
- Open `http://localhost:8501` in your browser.
- Enter target (e.g., `example.com` or `192.168.1.1`), select tool, provide Nessus keys if needed, and click "Run Scan".
- Results display as JSON; open ports visualized for Nmap (extend with Plotly for richer charts).

### API
Run the FastAPI server:
```bash
uvicorn app_api.py:app --reload
```
- Access Swagger UI at `http://localhost:8000/docs`.
- Endpoints:
  - `POST /scan/nmap`: Run Nmap scan.
  - `POST /scan/nikto`: Run Nikto scan.
  - `POST /scan/nessus`: Run Nessus scan (requires API keys and policy ID).
- Example request:
  ```bash
  curl -X POST "http://localhost:8000/scan/nmap" -H "Content-Type: application/json" -d '{"target":"example.com"}'
  ```

### CLI
Run scans via command line:
```bash
python cli.py --help
```
- Commands:
  - `python cli.py nmap <target>`: Run Nmap scan.
  - `python cli.py nikto <target>`: Run Nikto scan.
  - `python cli.py nessus <target> --access-key <key> --secret-key <key> [--policy-id <id>]`: Run Nessus scan.
- Example:
  ```bash
  python cli.py nmap example.com
  ```

## Project Structure
```
cyberdudebivash_threat_analyser007/
├── scanners.py       # Core scanning logic (Nmap, Nikto, Nessus)
├── app_gui.py       # Streamlit GUI dashboard
├── app_api.py       # FastAPI server for API endpoints
├── cli.py           # Click-based CLI
├── requirements.txt # Dependencies
├── README.md        # This file
```

## Best Practices
- **Security**: Store API keys in environment variables or a secure vault.
- **Legal**: Only scan systems you own or have explicit permission to scan.
- **Error Handling**: Check logs for tool-specific errors (e.g., Nikto may fail if target is unreachable).
- **Enhancements**:
  - Aggregate results across tools for unified threat reports.
  - Add visualizations (e.g., Matplotlib/Plotly in GUI).
  - Integrate threat intelligence APIs (e.g., VirusTotal).
- **Testing**: Use local VMs (e.g., Metasploitable) for safe testing.

## Limitations
- **Nessus**: Requires a paid Tenable.io account for API access. Consider OpenVAS for an open-source alternative.
- **Async Scanning**: Nessus scans are asynchronous; polling for results is simplified here. Implement robust polling for production.
- **Performance**: Scanning large networks may require optimization (e.g., async task queues).

## Contributing
Contributions are welcome! Submit pull requests or