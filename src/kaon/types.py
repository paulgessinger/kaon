from typing import (
    Union,
    Dict,
    Any,
    List,
    Tuple,
    Optional,
    Type,
    Callable,
    Text,
    Iterable,
    ByteString,
)

from types import TracebackType
from flask import Response

_ExcInfo = Tuple[
    Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType]
]
_StartResponse = Callable[
    [str, List[Tuple[str, str]], Optional[_ExcInfo]], Callable[[bytes], Any]
]
_WSGICallable = Callable[[Dict[Text, Any], _StartResponse], Iterable[bytes]]

_Status = Union[str, int]
_Headers = Union[Dict[Any, Any], List[Tuple[Any, Any]]]
_Body = Union[Text, ByteString, Dict[Text, Any], Response, _WSGICallable]

ViewFuncReturnType = Union[
    _Body,
    Tuple[_Body, _Status, _Headers],
    Tuple[_Body, _Status],
    Tuple[_Body, _Headers],
]
VR = ViewFuncReturnType
