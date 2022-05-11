"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.models import engine, Base, User, Post, Session
from homework_04.jsonplaceholder_requests import fetch_posts_data, fetch_users_data


async def create_schemas():

    async with engine.begin() as con:
        await con.run_sync(Base.metadata.drop_all)
        await con.run_sync(Base.metadata.create_all)


async def add_users(users_list: list, session: AsyncSession):

  users = [
    User(name=user['name'], username=user['username'], email=user['email'])
    for user in users_list
  ]

  session.add_all(users)
  await session.commit()


async def add_posts(posts_list: list, session: AsyncSession):

  posts = [
    Post(user_id=post['userId'], title=post['title'], body=post['body'])
    for post in posts_list
  ]

  session.add_all(posts)
  await session.commit()


async def async_main():

  await create_schemas()

  users_data, posts_data = await asyncio.gather(
    fetch_users_data(),
    fetch_posts_data(),
  )

  async with Session() as session:

    await add_users(users_data, session)
    await add_posts(posts_data, session)


def main():
  asyncio.run(async_main())


if __name__ == "__main__":
    main()
