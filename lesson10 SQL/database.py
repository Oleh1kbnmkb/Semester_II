import asyncpg
import asyncio

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
    
    
    
  async def register_student(self, name, age, email):
    sql = f"""
      INSERT INTO students (name, age, email) VALUES ({name}, {age}, {email})
    """
    await self.pool.execute(sql)