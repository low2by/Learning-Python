import asyncio
import numpy as np 

async def main():
    print('Hello ...')
    print(np.__version__)
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())

if __name__ == "main":
    main()