from collections.abc import Sequence

from processor.context import Context
from processor.async_processor import AbstractAsyncProcessor


class AsyncProcessorGroup(AbstractAsyncProcessor):
    def __init__(self, processors: Sequence[AbstractAsyncProcessor]):
        self.processors = processors

    async def execute(self, context: Context):
        for processor in self.processors:
            await processor.execute(context)
