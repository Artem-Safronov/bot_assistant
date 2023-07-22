import json
import aiohttp


async def http_client(url=None, headers=None, params=None):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url, params=params) as response:
            text = await response.text()
            return json.loads(text)
