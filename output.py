
def print_results(results: set):
    for item in sorted(results):
        print(item)

def save_results(results: set, filename: str):
    try:
        with open(filename, "w", encoding="utf-8") as f:

            for item in sorted(results):
                f.write(item + "\n")

        print(f"[+] Results saved to {filename}")

    except Exception as e:
        print(f"[!] Failed to write output file: {e}")

def print_summary(total: int, alive: int = None):
    print("\n[+] Summary")
    print(f"    Total Found : {total}")

    if alive is not None:
        print(f"    Alive Hosts : {alive}")
