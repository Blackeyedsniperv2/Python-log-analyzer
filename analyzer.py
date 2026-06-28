def login_attempts():
    from collections import Counter
    failed_attempts = 0
    successful_logins = 0
    failed_user = []
    successful_user = []
    with open("sample.log", "r") as log_file:
        for line in log_file:
            parts =line.split()
            username = parts[8]
            if "Failed password" in line:
                failed_attempts += 1
                failed_user.append(username)

            elif "Accepted password" in line:
                successful_logins += 1
                successful_user.append(username)

    users_failed_attemps = Counter(failed_user)
    users_successful_logins = Counter(successful_user)

    print("Number of failed logins:", failed_attempts)
    print("Number of successful logins:", successful_logins)
    print("Failed user attempts:")
    for user, attempts in users_failed_attemps.items():
        print(f"{user}: {attempts}")
    print("Successful user attempts:")
    for user, attempts in users_successful_logins.items():
        print(f"{user}: {attempts}")

def ip_addresses():
    from collections import Counter
    failed_ips = []
    successful_ips = []
    failed_attempts = 0
    successful_attempts = 0


    with open("sample.log", "r") as log_file:

        for line in log_file:
            parts =line.split()
            ip = parts[10]
            if "Failed password" in line:
                failed_ips.append(ip)
                failed_attempts += 1
            elif "Accepted password" in line:
                successful_ips.append(ip)
                successful_attempts += 1
    ip_failed_attempts = Counter(failed_ips)
    ip_successful_attempts = Counter(successful_ips)

    print("Number of failed IPs:", failed_attempts)
    print("Number of successful IPs:", successful_attempts)
    print("Failed IP attempts:")
    for ip, attempts in ip_failed_attempts.items():
        print(f"{ip}: {attempts}")
    print("Successful IP attempts:")
    for ip, attempts in ip_successful_attempts.items():
        print(f"{ip}: {attempts}")
