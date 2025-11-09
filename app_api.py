from fastapi import FastAPI
from scanners import nmap_scan, nikto_scan, nessus_scan
from pydantic import BaseModel

app = FastAPI(title="cyberdudebivash threat analyser007 API")

class ScanRequest(BaseModel):
    target: str
    nessus_access_key: str = None
    nessus_secret_key: str = None
    nessus_policy_id: int = 1

@app.post("/scan/nmap")
def api_nmap(scan: ScanRequest):
    return nmap_scan(scan.target)

@app.post("/scan/nikto")
def api_nikto(scan: ScanRequest):
    return nikto_scan(scan.target)

@app.post("/scan/nessus")
def api_nessus(scan: ScanRequest):
    if not scan.nessus_access_key or not scan.nessus_secret_key:
        return {"error": "Nessus keys required"}
    return nessus_scan(scan.target, scan.nessus_access_key, scan.nessus_secret_key, scan.nessus_policy_id)