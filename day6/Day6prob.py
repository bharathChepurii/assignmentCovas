import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin

async def fetch(session, url):
    print(f"Fetching: {url}")
    async with session.get(url) as resp:
        return await resp.text()

async def get_links(session, url):
    html = await fetch(session, url)
    if not html:
        return []  # No content found
    soup = BeautifulSoup(html, "html.parser")
    links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True)]
    return links[:5]  

async def download_links(url):
    async with aiohttp.ClientSession() as session:
        print(f"Processing main page: {url}")
        links = await get_links(session, url)
        tasks = []
        for link in links:
            print(f"Queuing download: {link}")
            tasks.append(fetch(session, link))

        contents = await asyncio.gather(*tasks)
        for i, page_content in enumerate(contents):
            if page_content:
                print(f"Downloaded: {links[i]}")  


async def main():
    url = "https://google.com" 
    await download_links(url)

asyncio.run(main())

