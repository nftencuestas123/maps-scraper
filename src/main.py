from src.scraping import run_scraper
from src.utils import export_results
from src.config import COUNTRY, CITY, NEIGHBORHOOD

if __name__ == "__main__":
    results = run_scraper(COUNTRY, CITY, NEIGHBORHOOD)
    export_results(results, formato="csv")
    print("Scraping finalizado y resultados exportados.")
