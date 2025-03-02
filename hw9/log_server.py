"""#9"""

import re


def parse_log(file_path):
    """
    Читає лог-файл та підраховує кількість запитів з кожної IP-адреси.

    Arguments:
        file_path (str): Шлях до лог-файлу.

    Returns:
        dict: Словник з кількістю запитів для кожної IP-адреси.
    """
    ip_counts = {}

    log_pattern = re.compile(r'^(\S+) \S+ \S+ \[.*\] ".*" \d+ \d+ ".*" ".*"$')

    with open(file_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            match = log_pattern.match(line)
            if match:
                ip = match.group(1)
                ip_counts[ip] = ip_counts.get(ip, 0) + 1

    return ip_counts


if __name__ == "__main__":
    LOG_PATH = "server.log"
    ips = parse_log(LOG_PATH)
    print(ips)
