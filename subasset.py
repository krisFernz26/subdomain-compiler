import subprocess

sublister_file_name = "sublister.txt"
assetfinder_file_name = "assetfinder.txt"
compiled_file_name = "subdomains.txt"

def run():
    # Ask for the domain to enumerate
    domain = input("Enter domain: ")
    # Run Sublist3r
    subprocess.run(['sublist3r', '-d', domain, '-o', 'sublister.txt'])
    # Outupt assetfinder results to file
    with open(assetfinder_file_name, 'w') as f:
        subprocess.run(['assetfinder', '-subs-only', domain], stdout=f)
    # Sort results from sublist3r and assetfinder to a file
    with open(compiled_file_name, 'w') as f:
        subprocess.run(['sort', '-u', sublister_file_name, assetfinder_file_name], stdout=f)


run()