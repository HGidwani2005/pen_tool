import streamlit as st
from scanners import nmap_scan, nikto_scan, nessus_scan

st.title("cyberdudebivash threat analyser007 Dashboard")

target = st.text_input("Enter Target (e.g., example.com or 192.168.1.1)")
tool = st.selectbox("Select Tool", ["Nmap", "Nikto", "Nessus"])

if tool == "Nessus":
    access_key = st.text_input("Tenable Access Key", type="password")
    secret_key = st.text_input("Tenable Secret Key", type="password")
    policy_id = st.number_input("Nessus Policy ID", value=1)

if st.button("Run Scan"):
    if tool == "Nmap":
        result = nmap_scan(target)
    elif tool == "Nikto":
        result = nikto_scan(target)
    elif tool == "Nessus":
        result = nessus_scan(target, access_key, secret_key, policy_id)
    
    st.subheader(f"{tool} Scan Results")
    st.json(result['result'])  # Display as JSON; enhance with tables/charts
    # Example: For Nmap, visualize open ports
    if tool == "Nmap" and 'nmap' in result['result']:
        ports = [p for h in result['result']['scan'] for p in result['result']['scan'][h].get('tcp', {})]
        st.bar_chart({'Open Ports': ports})