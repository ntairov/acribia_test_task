import aiohttp
import asyncio
import aiofiles
from pathlib import Path
from .models import StatusCodeField


def write_into_db(data):
    p = StatusCodeField.objects.create(status=data)
    p.save()
    return


def write_status_codes_into_file(data):

    with open('status.txt', 'a+') as file:
        file.write(f'{data}\n')


async def make_requests(session, url):
    async with session.head(url, allow_redirects=False) as response:
        assert response.status == 200
        print(f'Server response from {url}: {response.status} OK')
        data = f'Server response from {url}: {response.status} OK'
        write_status_codes_into_file(data)
        write_into_db(data)


async def main(url):
    tasks = []
    data_folder = Path(__file__).resolve().parents[1].joinpath("data/new_cleaned_data.txt")

    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(data_folder, mode='r') as f:
            async for line in f:
                concatenated_url = url + line.strip()
                task = asyncio.create_task(make_requests(session, concatenated_url))
                tasks.append(task)
        await asyncio.gather(*tasks)
