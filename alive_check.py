import requests


def check_alive(subdomains: set) -> set:

    alive_hosts = set()

    headers = {
        "User-Agent": "SubPulse/0.1"
    }

    for sub in subdomains:

        urls = [
            f"https://{sub}",
            f"http://{sub}"
        ]

        for url in urls:
            try:
                response = requests.get(
                    url,
                    headers=headers,
                    timeout=3,
                    allow_redirects=True
                )

                if response.status_code < 500:
                    alive_hosts.add(sub)
                    break

            except requests.RequestException:
                continue

    return alive_hosts
