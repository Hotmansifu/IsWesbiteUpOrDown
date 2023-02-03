import sys
import requests
import socket
import datetime

def check_site_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def main():
    website = input("Enter the website you want to check (e.g., https://www.google.com): ")
    
    if not (website.startswith("http://") or website.startswith("https://")):
        print("Error: Invalid URL, it should start with http:// or https://")
        sys.exit(1)
    
    status = check_site_status(website)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = "site_status.txt"
    
    try:
        with open(file_name, "a") as file:
            if status:
                hostname = website.replace("http://", "").replace("https://", "")
                try:
                    ip_address = socket.gethostbyname(hostname)
                    file.write(f"[{now}] {website} is up, IP address: {ip_address}\n")
                    print(f"{website} is up, IP address: {ip_address}")
                except:
                    file.write(f"[{now}] {website} is up, but IP address could not be retrieved\n")
                    print(f"{website} is up, but IP address could not be retrieved")
            else:
                file.write(f"[{now}] {website} is down\n")
                print(f"{website} is down")
    except PermissionError:
        print("Error: Permission denied when opening the file.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
