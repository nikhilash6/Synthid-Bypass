# Comfyui-SynthidBypass

Bundled custom node pack for the SynthID-Bypass v2 workflow.

This folder is laid out as a standard ComfyUI custom node package so it can be copied directly into `ComfyUI/custom_nodes/Comfyui-SynthidBypass`.

## Included nodes

### `Synthid-Bypass-Facedetailer`

A model-swap face detailer built on the Impact Pack SEGS detail flow, with direct `MODEL`, `CLIP`, `VAE`, `POSITIVE`, and `NEGATIVE` inputs plus simplified adaptive denoise controls.

Core inputs:

- `image` (`IMAGE`)
- `segs` (`SEGS`)
- `model` (`MODEL`)
- `clip` (`CLIP`)
- `vae` (`VAE`)
- `positive` / `negative` (`CONDITIONING`)
- standard sampling controls such as `steps`, `cfg`, `sampler_name`, `scheduler`, and `denoise`

Adaptive denoise settings:

- `adaptive_mode`: `largest_face` or `per_face`
- `adaptive_ratio`: target face ratio for base denoise
- `adaptive_denoise_min` / `adaptive_denoise_max`: clamp range

Formula:

`applied_denoise = clamp(base_denoise * (face_ratio / adaptive_ratio), min, max)`

Outputs:

- `segs` (`SEGS`): enhanced segments
- `cnet_images` (`IMAGE[]`): control previews
- `denoise_values` (`FLOAT[]`): applied denoise per segment
- `denoise_report` (`STRING`): per-segment denoise log

### `Synthid-Bypass-AdaptiveDenoise`

A lightweight helper node that computes a denoise value from image resolution only.

Inputs:

- `image` (`IMAGE`)
- `adaptive_level` (`INT`)
- `denoise_min` (`FLOAT`)
- `denoise_max` (`FLOAT`)

Outputs:

- `denoise` (`FLOAT`)
- `width` / `height` (`INT`)
- `pixel_ratio` (`FLOAT`)
- `report` (`STRING`)

## Installation

1. Install with one of these layouts:
   - Copy this folder into `ComfyUI/custom_nodes/Comfyui-SynthidBypass`.
   - Or clone the full Synthid-Bypass repo directly into `ComfyUI/custom_nodes/`; the repo root contains a compatibility loader that exposes the same nodes.
2. Make sure the dependencies below are installed.
3. Restart ComfyUI.

This package currently has no extra Python dependencies of its own beyond what ComfyUI and the required custom node packs already provide.

## Dependencies

- [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [RES4LYF](https://github.com/ClownsharkBatwing/RES4LYF) if you want the exact sampler/scheduler combination used in the v2 release workflow

The v2 workflow also relies on external node packs listed in the main repository README.

## Troubleshooting

- Search for `Synthid-Bypass-AdaptiveDenoise` after restarting ComfyUI. If it is missing, the package did not load.
- `Install Missing Custom Nodes` in ComfyUI Manager does not currently install this bundled node pack from the workflow repo. Use one of the manual install layouts above.
- Avoid nested folders like `.../Comfyui-SynthidBypass/Comfyui-SynthidBypass/...`.
- If `SEGSDetailerModelSwap` errors on load, verify that `ComfyUI-Impact-Pack` is installed and enabled.

## Typical usage

1. Build face masks or SEGS with Impact Pack tooling.
2. Run `Synthid-Bypass-AdaptiveDenoise` to choose a resolution-aware denoise level.
3. Feed face SEGS into `Synthid-Bypass-Facedetailer`.
4. Paste the updated SEGS back with `SEGSPaste`.

## Files

- `__init__.py`
- `segs_detailer_modelswap.py`
- `requirements.txt`
- `README.md`
