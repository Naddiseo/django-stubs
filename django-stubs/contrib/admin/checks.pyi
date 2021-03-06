from typing import Any, List

from django.contrib.admin.options import BaseModelAdmin, InlineModelAdmin, ModelAdmin
from django.core.checks.messages import Error

def check_admin_app(app_configs: None, **kwargs: Any) -> List[str]: ...
def check_dependencies(**kwargs: Any) -> List[Error]: ...

class BaseModelAdminChecks:
    def check(self, admin_obj: BaseModelAdmin, **kwargs: Any) -> List[Error]: ...

class ModelAdminChecks(BaseModelAdminChecks):
    def check(self, admin_obj: ModelAdmin, **kwargs: Any) -> List[Error]: ...

class InlineModelAdminChecks(BaseModelAdminChecks):
    def check(self, inline_obj: InlineModelAdmin, **kwargs: Any) -> List[Any]: ...

def must_be(type: Any, option: Any, obj: Any, id: Any): ...
def must_inherit_from(parent: Any, option: Any, obj: Any, id: Any): ...
def refer_to_missing_field(field: Any, option: Any, model: Any, obj: Any, id: Any): ...
