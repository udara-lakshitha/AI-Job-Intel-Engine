import httpx
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

async def get_content(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        async with httpx.AsyncClient(headers = headers, timeout = 10) as client:
            response = await client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            unwanted = ["script", "style", "nav", "header", "footer"]
            for tag in soup(unwanted):
                tag.decompose()

            clean_text = soup.get_text()
            return clean_text
    except Exception as e:
        logger.error(f"Something went wrong, {e}")
        raise e
