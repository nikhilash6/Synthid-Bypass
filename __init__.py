"""Compatibility shim so the repo root can be dropped into ComfyUI/custom_nodes."""

from __future__ import annotations

import importlib.util
from pathlib import Path


_MODULE_PATH = (
    Path(__file__).resolve().parent
    / "custom_nodes"
    / "Comfyui-SynthidBypass"
    / "segs_detailer_modelswap.py"
)

_SPEC = importlib.util.spec_from_file_location("synthid_bypass_custom_nodes", _MODULE_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise RuntimeError(f"Unable to load Synthid-Bypass custom nodes from {_MODULE_PATH}")

_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

NODE_CLASS_MAPPINGS = _MODULE.NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = _MODULE.NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
