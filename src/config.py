import os
from dotenv import load_dotenv
load_dotenv()
COUNTRY = os.getenv("SCRAPER_COUNTRY", "Argentina")
CITY = os.getenv("SCRAPER_CITY", "Buenos Aires")
NEIGHBORHOOD = os.getenv("SCRAPER_NEIGHBORHOOD", "Palermo")
