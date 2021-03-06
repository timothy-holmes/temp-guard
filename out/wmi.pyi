from _typeshed import Incomplete

__VERSION__: Incomplete
__description__: str
__url__: str

def signed_to_unsigned(signed): ...

class SelfDeprecatingDict:
    dict_only: Incomplete
    dict: Incomplete
    list: Incomplete
    def __init__(self, dictlike) -> None: ...
    def __getattr__(self, attribute): ...
    def __iter__(self): ...
    def __getitem__(self, item): ...

class ProvideConstants:
    def __init__(self, comobj) -> None: ...
    def __getattr__(self, name): ...

obj: Incomplete
wbemErrInvalidQuery: Incomplete
wbemErrTimedout: Incomplete
wbemFlagReturnImmediately: Incomplete
wbemFlagForwardOnly: Incomplete

class x_wmi(Exception):
    info: Incomplete
    com_error: Incomplete
    def __init__(self, info: str = ..., com_error: Incomplete | None = ...) -> None: ...

class x_wmi_invalid_query(x_wmi): ...
class x_wmi_timed_out(x_wmi): ...
class x_wmi_no_namespace(x_wmi): ...
class x_access_denied(x_wmi): ...
class x_wmi_authentication(x_wmi): ...
class x_wmi_uninitialised_thread(x_wmi): ...

WMI_EXCEPTIONS: Incomplete

def handle_com_error(err: Incomplete | None = ...) -> None: ...

BASE: Incomplete

def from_1601(ns100): ...
def from_time(year: Incomplete | None = ..., month: Incomplete | None = ..., day: Incomplete | None = ..., hours: Incomplete | None = ..., minutes: Incomplete | None = ..., seconds: Incomplete | None = ..., microseconds: Incomplete | None = ..., timezone: Incomplete | None = ...): ...
def to_time(wmi_time): ...

class _wmi_method:
    ole_object: Incomplete
    method: Incomplete
    qualifiers: Incomplete
    provenance: Incomplete
    in_parameters: Incomplete
    out_parameters: Incomplete
    in_parameter_names: Incomplete
    out_parameter_names: Incomplete
    __doc__: Incomplete
    def __init__(self, ole_object, method_name): ...
    def __call__(self, *args, **kwargs): ...

class _wmi_property:
    property: Incomplete
    name: Incomplete
    value: Incomplete
    qualifiers: Incomplete
    type: Incomplete
    provenance: Incomplete
    def __init__(self, property) -> None: ...
    def set(self, value) -> None: ...
    def __getattr__(self, attr): ...

class _wmi_object:
    def __init__(self, ole_object, instance_of: Incomplete | None = ..., fields=..., property_map=...) -> None: ...
    def __lt__(self, other): ...
    def __getattr__(self, attribute): ...
    def __setattr__(self, attribute, value) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    keys: Incomplete
    def wmi_property(self, property_name): ...
    def put(self) -> None: ...
    def set(self, **kwargs) -> None: ...
    def path(self): ...
    def derivation(self): ...
    associated_classes: Incomplete
    def associators(self, wmi_association_class: str = ..., wmi_result_class: str = ...): ...
    def references(self, wmi_class: str = ...): ...

class _wmi_event(_wmi_object):
    event_type_re: Incomplete
    def __init__(self, event, event_info, fields=...) -> None: ...

class _wmi_class(_wmi_object):
    def __init__(self, namespace, wmi_class) -> None: ...
    def __getattr__(self, attribute): ...
    def to_csv(self, filepath: Incomplete | None = ...): ...
    def query(self, fields=..., **where_clause): ...
    __call__: Incomplete
    def watch_for(self, notification_type: str = ..., delay_secs: int = ..., fields=..., **where_clause): ...
    def instances(self): ...
    def new(self, **kwargs): ...

class _wmi_result:
    def __init__(self, obj, attributes) -> None: ...

class _wmi_namespace:
    def __init__(self, namespace, find_classes) -> None: ...
    classes: Incomplete
    def get(self, moniker): ...
    def handle(self): ...
    def subclasses_of(self, root: str = ..., regex: str = ...): ...
    def instances(self, class_name): ...
    def new(self, wmi_class, **kwargs): ...
    new_instance_of: Incomplete
    def query(self, wql, instance_of: Incomplete | None = ..., fields=...): ...
    def fetch_as_classes(self, wmi_classname, fields=..., **where_clause): ...
    def fetch_as_lists(self, wmi_classname, fields, **where_clause): ...
    def watch_for(self, raw_wql: Incomplete | None = ..., notification_type: str = ..., wmi_class: Incomplete | None = ..., delay_secs: int = ..., fields=..., **where_clause): ...
    def __getattr__(self, attribute): ...

class _wmi_watcher:
    wmi_event: Incomplete
    is_extrinsic: Incomplete
    fields: Incomplete
    def __init__(self, wmi_event, is_extrinsic, fields=...) -> None: ...
    def __call__(self, timeout_ms: int = ...): ...

PROTOCOL: str

def connect(computer: str = ..., impersonation_level: str = ..., authentication_level: str = ..., authority: str = ..., privileges: str = ..., moniker: str = ..., wmi: Incomplete | None = ..., namespace: str = ..., suffix: str = ..., user: str = ..., password: str = ..., find_classes: bool = ..., debug: bool = ...): ...
WMI = connect

def construct_moniker(computer: Incomplete | None = ..., impersonation_level: Incomplete | None = ..., authentication_level: Incomplete | None = ..., authority: Incomplete | None = ..., privileges: Incomplete | None = ..., namespace: Incomplete | None = ..., suffix: Incomplete | None = ...): ...
def get_wmi_type(obj): ...
def connect_server(server, namespace: str = ..., user: str = ..., password: str = ..., locale: str = ..., authority: str = ..., impersonation_level: str = ..., authentication_level: str = ..., security_flags: int = ..., named_value_set: Incomplete | None = ...): ...
def Registry(computer: Incomplete | None = ..., impersonation_level: str = ..., authentication_level: str = ..., authority: Incomplete | None = ..., privileges: Incomplete | None = ..., moniker: Incomplete | None = ...): ...
