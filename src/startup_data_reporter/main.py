import sys
import os
import argparse
from startup_data_reporter.crew import crew
from dotenv import load_dotenv

load_dotenv(override=True)

def main():
    parser = argparse. ArgumentParser(description="Run startup data research.")
    parser.add_argument(" --startup_name", type=str, required=True, help="Name of the startup")
    parser.add_argument(" --country", type=str, required=True, help="Country where the startup is based")
    args = parser.parse_args()

    print(" Executing Crew tasks...\n")

    result = crew.kickoff(inputs={
        "startup_name": args.startup_name,
        "country": args.country
    })
  
    raw_output = getattr(result, "output", str(result))
    print("\n Final Markdown Output Preview:\n")
    print(raw_output)
    print("\n --- End of Preview --- \n")
    with open("startup_report.md", "w") as f:
        f.write(raw_output)

    print(" Markdown report written to 'startup_report.md'")


if __name__ == "__main__":
    main()
