from typing import Callable, Dict, List, Optional, Tuple, Any

from django.template.base import Template
from django.template.exceptions import TemplateSyntaxError

from .base import BaseEngine

class Jinja2(BaseEngine):
    app_dirs: bool
    dirs: List[str]
    name: str
    template_context_processors: List[Callable]
    template_dirs: Tuple[str]
    app_dirname: str = ...
    context_processors: List[str] = ...
    def __init__(self, params: Dict[str, Any]) -> None: ...
    def from_string(self, template_code: str) -> Template: ...
    def get_template(self, template_name: str) -> Template: ...

class Origin:
    name: str = ...
    template_name: Optional[str] = ...
    def __init__(self, name: str, template_name: Optional[str]) -> None: ...

def get_exception_info(exception: TemplateSyntaxError) -> Dict[str, Any]: ...
