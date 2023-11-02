import json
import traceback
from settings import logger
from aiohttp import ClientSession, ClientTimeout


async def http_client(method="GET", url=None, headers=None, params=None):
    try:
        async with ClientSession(headers=headers, timeout=ClientTimeout(total=3.0)) as session:
            async with session.request(method=method, url=url, params=params) as response:
                text = await response.text()
                logger.info(f"Response: {text}")
                return json.loads(text)
    except Exception as e:
        logger.error(traceback.format_exc())
        return {}
