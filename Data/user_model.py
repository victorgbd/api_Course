# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = Usersfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class User:
    id: int
    username: str
    password: str

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        username = from_str(obj.get("username"))
        password = from_str(obj.get("password"))
        return User(id, username, password)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["username"] = from_str(self.username)
        result["password"] = from_str(self.password)
        return result


def Usersfromdict(s: Any) -> List[User]:
    return from_list(User.from_dict, s)


def Userstodict(x: List[User]) -> Any:
    return from_list(lambda x: to_class(User, x), x)

