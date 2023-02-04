from typing import Any, Dict

_global_config: Dict[str, Any] = {}


def register_option(
    key: str,
    val: object,
    doc: str = "",
) -> None:
    _global_config.update({key: val})


def get_option(
    key: str,
) -> object:
    assert key in _global_config, f"No such keys: {key}"
    return _global_config[key]


def set_option(
    key: str,
    val: object,
    doc: str = "",
) -> None:
    assert key in _global_config, f"No such keys: {key}"
    _global_config.update({key: val})


