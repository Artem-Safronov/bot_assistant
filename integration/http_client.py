import json
import aiohttp


async def http_client(method="GET", url=None, headers=None, params=None):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=url, params=params) as response:
            text = await response.text()
            return json.loads(text)
