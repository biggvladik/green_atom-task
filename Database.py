import aiosqlite

async def select_active_process():
    async with aiosqlite.connect("test.db") as db:
        cursor = await db.execute(f"SELECT * FROM  test_table")
        res = await cursor.fetchall()
        return res

async def insert_start_process(items:list):
    async with aiosqlite.connect("test.db") as db:
        for item in items:
            cursor = await db.execute(f"INSERT  INTO  test_table (PID,date_start,number_start) VALUES (?,?,?)",(item['PID'],item['date_start'],item['number_start']))
        res = await db.commit()


async def insert_stop_process(items:list):
    async with aiosqlite.connect("test.db") as db:
        for item in items:
            cursor = await db.execute(f"UPDATE test_table SET date_end = ? WHERE PID = ? and date_end is NULL",(item['date_end'],item['PID']))
            cursor = await db.execute(f"UPDATE test_table SET time = strftime('%s', date_end) - strftime('%s', date_start)")

        res = await db.commit()


async def select_all_process():
    async with aiosqlite.connect("test.db") as db:
        cursor = await db.execute(f"SELECT * FROM  test_table")
        res = await cursor.fetchall()
        return res