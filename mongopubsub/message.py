from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    topic: str
    attributes: dict
    data: object

    def to_dict(self):
        return {
            "topic": self.topic,
            "attributes": self.attributes,
            "data": self.data,
        }

    @classmethod
    def from_dict(cls, param):
        return cls(
            topic=param["topic"],
            attributes=param["attributes"],
            data=param["data"],
        )
