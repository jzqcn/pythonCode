import asyncio
import re
import argparse
import logging

import aiohttp
import async_timeout
from urllib.parse import urlparse, urljoin
import csv


class Crawler:
    def __init__(self, urls, max_redirects=5, max_tries=5, max_tasks=10, output_file=None):
        self.urls = urls
        self.base_url = urlparse(urls[0]).scheme + "://" + urlparse(urls[0]).netloc
        self.max_redirects = max_redirects
        self.max_tries = max_tries
        self.max_tasks = max_tasks
        self.tlds = ("com", "edu", "gov", "int", "mil", "net", "org", "biz", "info", "me", "mobi", "name", "tv",
                     "ly", "io", "ai", "co")
        self.tasks = set()
        self.done = {}
        self.session = aiohttp.ClientSession()
        self.output_file = output_file if output_file else "results.csv"
        logging.basicConfig(filename='crawler.log', level=logging.WARNING)

    async def crawl(self):
        for url in self.urls:
            task = asyncio.ensure_future(self.fetch(url))
            self.tasks.add(task)
        while self.tasks:
            done, self.tasks = await asyncio.wait(self.tasks, return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                ## will raise exception for any error from task
                try:
                    res = await task
                    url = urlparse(res.url).geturl()
                    self.done[url] = True
                    print(f'{url} fetched. Total done: {len(self.done)}')
                    self.parse_links(res)
                except Exception as e:
                    logging.warning(f'{task} got error {e.__class__} {str(e)}')
        await self.session.close()

    async def fetch(self, url, redirect_count=0, try_count=0):
        logging.debug(f'{url} ({redirect_count}, {try_count})')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        async with async_timeout.timeout(10):
            async with self.session.get(url, headers=headers, allow_redirects=False) as response:
                if response.status in (300, 301, 302, 303, 307):
                    if redirect_count >= self.max_redirects:
                        raise Exception(f'Maximum ({self.max_redirects}) redirects exceeded for {url}')
                    redirect_url = response.headers.get('location')
                    next_url = urljoin(url, redirect_url)
                    return await self.fetch(next_url, redirect_count + 1, 0)
                if not response.status == 200:
                    if try_count < self.max_tries:
                        return await self.fetch(url, redirect_count, try_count + 1)
                    else:
                        raise aiohttp.ClientError(f'Fetching {url} failed with status {response.status}')
                return response

    def get_links(self, html):
        urls = set()
        for url in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
            parts = urlparse(url)
            if parts.scheme not in ("http", "https", "ftp", "ftps", ""):
                continue
            netloc = parts.netloc or self.base_url
            if not re.match(rf'[a-z0-9][a-z0-9-]*\.[{"|".join(self.tlds)}]', netloc, re.I):
                continue
            if url.startswith('//'):
                url = 'http:' + url
            elif url.startswith('/'):
                url = 'http://' + self.base_url + url
            if self.base_url not in url:
                continue
            fragment = parts.fragment
            if '?' in url:
                url = url[:url.find('?')]
            urls.add(url)

        return urls

    def parse_links(self, response):
        url = urlparse(response.url).geturl()

        html = response.body.decode("utf-8", errors="ignore")
        urls = self.get_links(html)
        for u in urls:
            # do not handle so frequently visited or already processed urls
            if u in self.done:
                continue
            self.done[u] = False

            # limit parallelism across domains
            if urlparse(u).netloc != urlparse(url).netloc:
                continue

            print(f'New link found: {u}')
            task = asyncio.ensure_future(self.fetch(u))
            self.tasks.add(task)

            # store link in csv file
            with open(self.output_file, 'a', newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([url, u])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--urls', nargs='+', required=True, help='url(s) to crawl')
    parser.add_argument('-r', '--max_redirects', type=int, default=5, help='maximum redirect jumps (default=5)')
    parser.add_argument('-t', '--max_tries', type=int, default=5, help='maximum times to try loading a URL (default=5)')
    parser.add_argument('-j', '--max_tasks', type=int, default=10, help='maximum concurrent tasks (default=10)')
    parser.add_argument('-o', '--output_file', default="results.csv", help='output file name (default=results.csv)')
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    crawler = Crawler(args.urls, args.max_redirects, args.max_tries, args.max_tasks, args.output_file)
    loop.run_until_complete(crawler.crawl())
