import argparse
from banner import show_banner ,show_target_banner
from subDomain_enum import get_subdomains
from alive_check import check_alive
from output import save_results ,print_results,print_summary


def main():

    parser = argparse.ArgumentParser(
        description="SubPulse - Passive Subdomain Enumeration Tool"
    )

    parser.add_argument(
        "-d",
        "--domain",
        required=True,
        help="Target domain"
    )
    parser.add_argument(
    "--alive",
    action="store_true",
    help="Check for reachable hosts"
)
    parser.add_argument(
    "-o",
    "--output",
    help="Save output to file"
)


    args = parser.parse_args()

    domain = args.domain
    alive = args.alive
    


    show_banner()
    show_target_banner(domain)

    success, subdomains = get_subdomains(domain)
    if not success:
      print("[!] crt.sh temporarily unavailable")
      return

    if not subdomains:
      print("[i] No subdomains found")
      return

    if alive:
     final_results = check_alive(subdomains)
    else:
      final_results = subdomains

    if args.output:
      save_results(final_results, args.output)
    else:
      print_results(final_results)

    print_summary(len(subdomains),len(final_results) if alive else None)

if __name__ == "__main__":
    main()
