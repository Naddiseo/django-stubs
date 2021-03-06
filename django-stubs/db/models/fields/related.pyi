from typing import Type, Union, TypeVar, Any, Generic, List, Optional, Dict, Callable, Tuple, Sequence, TYPE_CHECKING
from uuid import UUID

from django.db import models
from django.db.models import Field, Model, QuerySet
from django.db.models.fields.mixins import FieldCacheMixin
from django.db.models.query_utils import PathInfo, Q

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager

_T = TypeVar("_T", bound=models.Model)

class RelatedField(FieldCacheMixin, Field):
    one_to_many: bool = ...
    one_to_one: bool = ...
    many_to_many: bool = ...
    many_to_one: bool = ...
    def related_model(self) -> Union[Type[Model], str]: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    opts: Any = ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, str]]: ...
    def get_forward_related_filter(self, obj: Model) -> Dict[str, Union[int, UUID]]: ...
    def get_reverse_related_filter(self, obj: Model) -> Q: ...
    @property
    def swappable_setting(self) -> Optional[str]: ...
    name: Any = ...
    verbose_name: Any = ...
    def set_attributes_from_rel(self) -> None: ...
    def do_related_class(self, other: Type[Model], cls: Type[Model]) -> None: ...
    def get_limit_choices_to(self) -> Dict[str, int]: ...
    def formfield(self, **kwargs: Any) -> Field: ...
    def related_query_name(self) -> str: ...
    @property
    def target_field(self) -> Field: ...

class ForeignObject(RelatedField): ...

class ForeignKey(RelatedField, Generic[_T]):
    def __init__(self, to: Union[Type[_T], str], on_delete: Any, related_name: str = ..., **kwargs): ...
    def __get__(self, instance, owner) -> _T: ...

class OneToOneField(RelatedField, Generic[_T]):
    def __init__(self, to: Union[Type[_T], str], on_delete: Any, related_name: str = ..., **kwargs): ...
    def __get__(self, instance, owner) -> _T: ...

class ManyToManyField(RelatedField, Generic[_T]):
    many_to_many: bool = ...
    many_to_one: bool = ...
    one_to_many: bool = ...
    one_to_one: bool = ...
    rel_class: Any = ...
    description: Any = ...
    has_null_arg: Any = ...
    db_table: Any = ...
    swappable: Any = ...
    def __init__(
        self,
        to: Union[Type[_T], str],
        related_name: Optional[str] = ...,
        related_query_name: Optional[str] = ...,
        limit_choices_to: Optional[Callable] = ...,
        symmetrical: Optional[bool] = ...,
        through: Optional[Union[str, Type[Model]]] = ...,
        through_fields: Optional[Tuple[str, str]] = ...,
        db_constraint: bool = ...,
        db_table: None = ...,
        swappable: bool = ...,
        **kwargs: Any
    ) -> None: ...
    def __set__(self, instance, value: Sequence[_T]) -> None: ...
    def __get__(self, instance, owner) -> RelatedManager[_T]: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, str]]: ...
    def get_path_info(self, filtered_relation: None = ...) -> List[PathInfo]: ...
    def get_reverse_path_info(self, filtered_relation: None = ...) -> List[PathInfo]: ...
    m2m_db_table: Any = ...
    m2m_column_name: Any = ...
    m2m_reverse_name: Any = ...
    m2m_field_name: Any = ...
    m2m_reverse_field_name: Any = ...
    m2m_target_field_name: Any = ...
    m2m_reverse_target_field_name: Any = ...
    def contribute_to_related_class(self, cls: Type[Model], related: RelatedField) -> None: ...
    def set_attributes_from_rel(self) -> None: ...
    def value_from_object(self, obj: Model) -> List[Model]: ...
    def save_form_data(self, instance: Model, data: QuerySet) -> None: ...
