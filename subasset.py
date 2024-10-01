import subprocess
from pathlib import Path

cwd = Path.cwd()
sublister_file_name = "sublister.txt"
assetfinder_file_name = "assetfinder.txt"
compiled_file_name = "subdomains.txt"

def run_sublister(domain: str):
    subprocess.run(['sublist3r', '-d', domain, '-o', 'sublister.txt'])

def run_assetfinder(domain: str):
    with open(assetfinder_file_name, 'w') as f:
        subprocess.run(['assetfinder', '-subs-only', domain], stdout=f)

def sort():
    with open(compiled_file_name, 'w') as f:
        subprocess.run(['sort', '-u', sublister_file_name, assetfinder_file_name], stdout=f)


domain = input("Enter domain: ")
run_sublister(domain)
run_assetfinder(domain)
sort()