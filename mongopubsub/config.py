from dataclasses import dataclass


@dataclass(frozen=True)
class MongoConfig:
    """
    MongoDB configuration

    Attributes
    ----------
    capped: bool
        Whether the collection should be capped.
    size: int
        The size of the collection in bytes (50mb by default)
    max: int
        The maximum number of documents in the collection (5000 by default)

    """
    database: str = "mongopubsub"
    collection: str = "topics_channel"
    capped: bool | None = True
    size: int | None = 1024 * 1024 * 50
    max: int | None = 5000

    @classmethod
    def from_dict(cls, d: dict) -> 'MongoConfig':
        return cls(**d)
