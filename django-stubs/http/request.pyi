# Stubs for django.http.request (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
from io import BytesIO
from typing import Any, BinaryIO, Dict, Iterable, Iterator, List, Optional, overload, Pattern, Tuple, Union

from django.core.files import uploadhandler, uploadedfile
from django.utils.datastructures import MultiValueDict, ImmutableList
from django.urls import ResolverMatch

RAISE_ERROR = ...  # type: object
host_validation_re = ...  # type: Pattern

class UnreadablePostError(IOError): ...
class RawPostDataException(Exception): ...

UploadHandlerList = Union[List[uploadhandler.FileUploadHandler], ImmutableList[uploadhandler.FileUploadHandler]]

class HttpRequest(BytesIO):
    GET = ...  # type: QueryDict
    POST = ...  # type: QueryDict
    COOKIES = ...  # type: Dict[str, str]
    META = ...  # type: Dict[str, str]
    FILES = ...  # type: MultiValueDict[str, uploadedfile.UploadedFile]
    path = ...  # type: str
    path_info = ...  # type: str
    method = ...  # type: Optional[str]
    resolver_match = ...  # type: ResolverMatch
    content_type = ...  # type: Optional[str]
    content_params = ...  # type: Optional[Dict[str, str]]
    def __init__(self) -> None: ...
    def get_host(self) -> str: ...
    def get_port(self) -> str: ...
    def get_full_path(self, force_append_slash: bool = ...) -> str: ...
    def get_full_path_info(self, force_append_slash: bool = ...) -> str: ...
    def get_signed_cookie(
        self, key: str, default: Any = ..., salt: str = ..., max_age: Optional[int] = ...
    ) -> Optional[str]: ...
    def get_raw_uri(self) -> str: ...
    def build_absolute_uri(self, location: str = ...) -> str: ...
    @property
    def scheme(self) -> Optional[str]: ...
    def is_secure(self) -> bool: ...
    def is_ajax(self) -> bool: ...
    encoding = ...  # type: Optional[str]
    upload_handlers = ...  # type: UploadHandlerList
    def parse_file_upload(
        self, META: Dict[str, str], post_data: BinaryIO
    ) -> Tuple["QueryDict", MultiValueDict[str, uploadedfile.UploadedFile]]: ...
    @property
    def body(self) -> bytes: ...
    def close(self) -> None: ...
    def read(self, *args: Any, **kwargs: Any) -> bytes: ...
    def readline(self, *args: Any, **kwargs: Any) -> bytes: ...
    def xreadlines(self) -> Iterator[bytes]: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def readlines(self) -> List[bytes]: ...  # type: ignore

class QueryDict(MultiValueDict[str, str]):
    encoding = str  # type: Any
    def __init__(
        self, query_string: Union[str, bytes, None] = None, mutable: bool = False, encoding: Optional[str] = None
    ) -> None: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __copy__(self) -> "QueryDict": ...
    def __deepcopy__(self, memo: Dict[int, object]) -> "QueryDict": ...
    def setlist(self, key: str, list_: List[str]) -> None: ...
    def setlistdefault(self, key: str, default_list: List[str] = None) -> List[str]: ...
    def appendlist(self, key: str, value: str) -> None: ...
    def pop(self, key: str, default: List[str] = None) -> List[str]: ...  # type: ignore
    def popitem(self) -> Tuple[str, str]: ...
    def clear(self) -> None: ...
    def setdefault(self, key: str, default: Optional[str] = None) -> str: ...
    def copy(self) -> "QueryDict": ...
    def urlencode(self, safe: Optional[str] = None) -> str: ...

@overload
def bytes_to_text(s: bytes, encoding: str) -> str: ...
@overload
def bytes_to_text(s: str, encoding: str) -> str: ...
@overload
def bytes_to_text(s: None, encoding: str) -> None: ...
def split_domain_port(host: str) -> Tuple[str, str]: ...
def validate_host(host: str, allowed_hosts: Iterable[str]) -> bool: ...
