import asyncio
import aiohttp
import xml.etree.ElementTree as XML
from aiohttp import ClientSession
from time import time


CHUNK_SIZE = 10
failed_urls = []


async def check_sitemap():
    started = time()
    count = await check_urls_from_sitemap('https://www.qa.4kdownload.com/sitemap-main.xml')
    total_time = time() - started
    print(f'Sitemap Check Success: {count} urls have been checked ({total_time:2.4})')


async def check_dmca():
    started = time()
    count = await check_urls_from_file(filename='dmca.txt', host='https://www.qa.4kdownload.com')
    total_time = time() - started
    print(f'DMCA Check Success: {count} urls have been checked ({total_time:2.4})')


async def check_urls_from_sitemap(sitemap_url):
    ''' Collects urls from the sitemap to invoke GET request for every url. '''
    async with ClientSession() as session:
        text, *_ = await fetch(session, sitemap_url, with_content=True)

    urls = [e.text for e in XML.fromstring(text).findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

    return await check_urls(urls)


async def check_urls_from_file(filename, host):
    ''' Collects urls from the text file to invoke GET request for every url. '''
    with open(filename, 'r') as f:
        urls = list(host + line.rstrip() for line in f if line and line.strip() and not line.startswith('#'))

    return await check_urls(urls)


async def check_urls(urls):
    i = 0
    count = len(urls)
    for chunk in chunk_urls(urls):
        checked = await check_chunk(chunk)
        for _, url, time in checked:
            i += 1
            print(f'{i}/{count} {time:2.4} {url}')
    return count


def chunk_urls(urls):
    for i in range(0, len(urls), CHUNK_SIZE):
        yield urls[i:i+CHUNK_SIZE]


async def check_chunk(urls):
    async with ClientSession() as session:
        tasks = [asyncio.ensure_future(fetch(session, url, with_content=False)) for url in urls]
        return await asyncio.gather(*tasks)


async def fetch(session, url, with_content):
    global failed_urls
    started = time()

    try:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            content = with_content and await response.text()
            return content, url, time() - started
    except (asyncio.exceptions.TimeoutError, aiohttp.client_exceptions.ClientResponseError) as err:
        print('ERROR', url, repr(err))
        failed_urls.append(url)
        return '', url, time() - started


if __name__ == '__main__':
    try:
        asyncio.run(check_sitemap())
        asyncio.run(check_dmca())
    except Exception as err:
        raise

    if failed_urls:
        print()
        for u in failed_urls:
            print('ERROR: ', u)
        raise Exception(f'{len(failed_urls)} urls failed to fetch')
