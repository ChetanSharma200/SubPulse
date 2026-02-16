# ->Fetch certificate data from crt.sh.
# ->Pa-rse JSON entries.
# ->Extract domain names from two fields.
# ->Clean bad entries (wildcards, emails, junk).
# ->Store unique results in a set.

import requests
import time

def get_subdomains(domain: str) -> (bool, set):

    url = f"https://crt.sh/?q={domain}&output=json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    data = None

    for attempt in range(3):
        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=(5, 60)
            )

            response.raise_for_status()
            data = response.json()
            break

        except requests.exceptions.HTTPError as e:
            if e.response and e.response.status_code == 503 and attempt < 2:
                print(f"[!] crt.sh unavailable (attempt {attempt+1}/3), retrying...")
                time.sleep(1)
                continue
            return False, set()

        except Exception:
            return False, set()

    if not data:
        return True, set()

    subdomains = set()

    for entry in data:
        cn = entry.get("common_name", "")
        names = entry.get("name_value", "")

        candidates = [cn] + names.split("\n")

        for name in candidates:

            if not name:
                continue

            name = name.strip().lower()
            name = name.replace("*.", "")

            if "@" in name:
                continue

            subdomains.add(name)

    return True, subdomains


