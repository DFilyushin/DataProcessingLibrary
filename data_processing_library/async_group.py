from collections.abc import Sequence

from data_processing_library.context import Context
from data_processing_library.async_processor import AbstractAsyncProcessor


class AsyncProcessorGroup(AbstractAsyncProcessor):
    def __init__(self, processors: Sequence[AbstractAsyncProcessor]):
        self.processors = processors

    async def execute(self, context: Context):
        for processor in self.processors:
            await processor.execute(context)
