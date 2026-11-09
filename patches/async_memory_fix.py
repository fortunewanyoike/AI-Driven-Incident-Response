# Fixed async memory accumulation using weak references and bounded semaphores
import asyncio
import weakref

class BoundedWorkerPool:
    def __init__(self, max_size=100):
        self.semaphore = asyncio.Semaphore(max_size)
        self.active_tasks = weakref.WeakSet()

    async def execute(self, coro):
        async with self.semaphore:
            task = asyncio.create_task(coro)
            self.active_tasks.add(task)
            return await task
