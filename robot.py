import sys
import asyncio

async def robot(start_num=0):
    num = start_num
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)

if __name__ == "__main__":
    start_num = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    asyncio.run(robot(start_num))