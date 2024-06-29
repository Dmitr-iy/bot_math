import aiomysql


class Request:
    def __init__(self, connector: aiomysql.pool):
        self.connector = connector

    async def add_data(self, user_id, user_name):
        query = "INSERT INTO datausers (user_id, user_name) VALUES (%s, %s) " \
                "ON DUPLICATE KEY UPDATE user_name = %s;"
        try:
            async with self.connector.cursor() as cursor:
                await cursor.execute(query, (user_id, user_name, user_name))
                await self.connector.commit()
        except aiomysql.Error as e:
            print(f"Error inserting data: {e}")
            await self.connector.rollback()
