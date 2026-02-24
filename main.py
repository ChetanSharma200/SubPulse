import argparse
import Scripts.banner as banner 
from Scripts.subDomain_enum import get_subdomains
from Scripts.alive_check import check_alive
import Scripts.output as output


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
    


    banner.show_banner()
    banner.show_target_banner(domain)

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
      output.save_results(final_results, args.output)
    else:
      output.print_results(final_results)

    output.print_summary(len(subdomains),len(final_results) if alive else None)

if __name__ == "__main__":
    main()
