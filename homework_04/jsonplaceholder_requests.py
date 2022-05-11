"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(session, url):
    async with session.get(url) as response:
        respons_json = await response.json()
        return respons_json

async def fetch_users_data():
    async with ClientSession() as session:
        return await fetch_json(session, USERS_DATA_URL)

async def fetch_posts_data():
    async with ClientSession() as session:
        return await fetch_json(session, POSTS_DATA_URL)
