from pydantic import StringConstraints
from typing import Annotated

Username = Annotated[str, StringConstraints(min_length=1, max_length=50)]
MessageContent = Annotated[str, StringConstraints(min_length=1, max_length=1000)]