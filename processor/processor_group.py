from collections.abc import Sequence
from processor.context import Context
from processor.processor import AbstractProcessor


class ProcessorGroup(AbstractProcessor):
    """The group of processors."""
    def __init__(self, processors: Sequence[AbstractProcessor]):
        """Initializes a new instance of the ProcessorGroup class."""
        self.processors = processors

    def execute(self, context: Context):
        """Executes all child processors"""
        for processor in self.processors:
            processor.execute(context)
