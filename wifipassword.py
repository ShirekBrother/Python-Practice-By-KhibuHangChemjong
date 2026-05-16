import subprocess

def get_wifi_profiles():
    command = "netsh wlan show profiles"
    result = subprocess.check_output(command, shell=True).decode()
    profiles = []

    for line in result.split("\n"):
        if "All User Profile" in line:
            profile = line.split(":")[1].strip()
            profiles.append(profile)

    return profiles

def get_wifi_password(profile):
    try:
        command = f'netsh wlan show profile name="{profile}" key=clear'
        result = subprocess.check_output(command, shell=True).decode()

        for line in result.split("\n"):
            if "Key Content" in line:
                return line.split(":")[1].strip()
        return "No Password Found"
    except:
        return "Error retrieving password"

def main():
    print("Saved Wi-Fi Networks and Passwords:\n")
    profiles = get_wifi_profiles()

    for profile in profiles:
        password = get_wifi_password(profile)
        print(f"WiFi Name: {profile} | Password: {password}")

if __name__ == "__main__":
    main()