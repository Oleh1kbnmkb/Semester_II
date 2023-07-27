import asyncpg
import asyncio
from aiogram.dispatcher.filters.state import StatesGroup, State

class Database():
  def __init__(self):
    loop = asyncio.get_event_loop()
    self.pool = loop.run_until_complete(
      asyncpg.create_pool(
        user = 'op663246',
        database='neondb',
        password='5ELlvIaWx3JK',
        host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
        port='5432'
      )
    )
    
    
    
  async def register_student(self, username, password, email):
    sql = f"""
      INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')
    """
    print(sql)
    await self.pool.execute(sql)
    
    
    
class Login(StatesGroup):
   set_username = State()
   set_password = State()
   
   
   
class Registration(StatesGroup):
   set_name = State()
   set_age = State()
   set_email = State()
   
   