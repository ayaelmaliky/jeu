from _typeshed import Incomplete

class RoutesSystem:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, metrics: Incomplete | None = None, debug: Incomplete | None = None, health: Incomplete | None = None
    ) -> None: ...
    @property
    def metrics(self): ...
    @metrics.setter
    def metrics(self, metrics) -> None: ...
    @property
    def debug(self): ...
    @debug.setter
    def debug(self, debug) -> None: ...
    @property
    def health(self): ...
    @health.setter
    def health(self, health) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...