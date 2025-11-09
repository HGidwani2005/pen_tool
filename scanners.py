import nmap
import subprocess
import json
from tenable.io import TenableIO
import os

def nmap_scan(target, args='-sV -O'):  # Default: service version and OS detection
    scanner = nmap.PortScanner()
    result = scanner.scan(target, arguments=args)
    return {'tool': 'Nmap', 'result': result}

def nikto_scan(target):
    try:
        output = subprocess.check_output(['nikto', '-h', target, '-Format', 'json'])
        result = json.loads(output)
    except Exception as e:
        result = {'error': str(e)}
    return {'tool': 'Nikto', 'result': result}

def nessus_scan(target, access_key, secret_key, policy_id=1):  # policy_id: Use a basic scan policy
    try:
        tio = TenableIO(access_key, secret_key)
        scan_config = {
            'name': f'Scan for {target}',
            'description': 'Automated scan',
            'targets': [target],
            'policy_id': policy_id  # Replace with your policy ID
        }
        scan = tio.scans.create(**scan_config)
        tio.scans.launch(scan['id'])
        # Note: Scanning is async; poll for results in production
        status = tio.scans.status(scan['id'])
        results = tio.scans.results(scan['id'])  # Simplified; fetch full results as needed
    except Exception as e:
        results = {'error': str(e)}
    return {'tool': 'Nessus', 'result': results}