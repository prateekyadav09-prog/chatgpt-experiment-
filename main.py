"""
Faculty & Research Vacancy Tracker
Main Entry Point
"""

import pandas as pd
from datetime import datetime

from config import OUTPUT_CSV

# Future scraper imports
# from scraper import collect_vacancies


def collect_vacancies():
    """
    Placeholder until scraper.py is implemented.
    """
    vacancies = []
    return vacancies


def save_results(vacancies):
    """
    Save results to CSV.
    """

    columns = [
        "Date Found",
        "Organisation",
        "Position",
        "Subject",
        "Location",
        "Last Date",
        "Advertisement Link",
        "Status",
    ]

    df = pd.DataFrame(vacancies, columns=columns)
    df.to_csv(OUTPUT_CSV, index=False)

    print(f"Saved {len(df)} vacancies to {OUTPUT_CSV}")


def main():
    print("=" * 60)
    print("Faculty & Research Vacancy Tracker")
    print("=" * 60)

    print("Started:", datetime.now())

    vacancies = collect_vacancies()

    save_results(vacancies)

    print("Finished:", datetime.now())


if __name__ == "__main__":
    main()