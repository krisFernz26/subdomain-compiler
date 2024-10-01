import subprocess

sublister_file_name = "sublister.txt"
assetfinder_file_name = "assetfinder.txt"
compiled_file_name = "subdomains.txt"

def run():
    domain = input("Enter domain: ")
    subprocess.run(['sublist3r', '-d', domain, '-o', 'sublister.txt'])
    with open(assetfinder_file_name, 'w') as f:
        subprocess.run(['assetfinder', '-subs-only', domain], stdout=f)
    with open(compiled_file_name, 'w') as f:
        subprocess.run(['sort', '-u', sublister_file_name, assetfinder_file_name], stdout=f)


run()