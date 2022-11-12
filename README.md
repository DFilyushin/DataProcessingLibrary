# DataProcessingLibrary

Python port for [Skivsoft.Processor](https://github.com/skivsoft/Skivsoft.Processor)

Simple data processing library.

The key features are:
* Easy idea for running tasks step-by-step
* Synchronous and asynchronous way for executing steps
* Support SOLID


## Example of usage


```Python
from uuid import uuid4
from processor.processor import AbstractProcessor, Context
from processor.group import ProcessorGroup


class HelloContext(Context):
    def __init__(self):
        self.name = None

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name


class InputName(AbstractProcessor):
    def execute(self, context: HelloContext):
        context.set_name(uuid4().hex)


class OutputGreeting(AbstractProcessor):
    def execute(self, context: HelloContext):
        print(f'Hello, {context.get_name()}!')


def run_processor():
    hello_context = HelloContext()
    steps = [
        InputName(),
        OutputGreeting(),
    ]
    processor = ProcessorGroup(steps)
    processor.execute(hello_context)


if __name__ == '__main__':
    run_processor()
```
