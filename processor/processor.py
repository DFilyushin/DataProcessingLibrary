from processor.context import Context


class AbstractProcessor:
    """Abstract processor (the process interface)"""
    def execute(self, context: Context):
        """Executes some action."""
        raise NotImplementedError
