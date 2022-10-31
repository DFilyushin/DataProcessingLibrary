from processor.context import Context


class AbstractAsyncProcessor:
    """Abstract asynchronous processor (The process interface)"""
    async def execute(self, context: Context):
        """Executes some action asynchronously"""
        raise NotImplementedError
