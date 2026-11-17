# Implementation Handoff — HyperBoostX V3 Unified

## Objective

Convert this **browser prototype** into the **real native Windows application**, preserving all features that existed in HyperBoostX V1–V2 and implementing the new V3 architecture. Source baseline: `https://github.com/jxxzy/HyperBoostX`, action reference `docs/UI_ACTION_MAP_v2.10.0.md`; visual baseline: this prototype. Do not claim this HTML is a finished optimizer.

## Non-negotiable parity contract

- The prototype catalog includes **73 V3 modules** and an explicit crosswalk for **73 V2 menu names**. They are not necessarily the same 73 capabilities.
- V2 documented **606 action buttons**. Obtain the true V2 action map and enumerate every ActionId/command/endpoint; the current prototype does **not** include that entire 606-action registry.
- For each V1–V2 feature document: `legacy source → V3 ModuleId → new ActionId → implementation → current state → expected state → privilege → preview → backup → apply → verify → rollback → evidence → automated test → hardware lab test`. Missing fields are blockers, not partial credit.
- Do not delete or collapse high-risk legacy flows (HyperBalance, Advanced Mic Mixer, NVIDIA Copilot, Camera Tracking, System Reality Guard, Defender Scan Guard, protected apps, restore point manager, license/cloud) without preserving actual capabilities or recording an explicit accepted scope decision.
- Use 73 V3 modules as the navigation baseline, but additional submenu/tool entries are allowed if needed to preserve historical behavior accurately.

## Design and UX

Replicate the UI layout and page-specific content with native WPF/WinUI components, support desktop scaling, high DPI, full keyboard use, light/dark themes, localization id-ID/en-US, onboarding, native title bar, accessible UI. Do not ship a WebView pretending to be a system optimizer.

## Backend, security, and safety

Use typed IPC with a least-privilege Windows worker and allowlisted actions. Do not allow arbitrary shell/PowerShell strings from UI or AI. Protect Defender, anti-cheat, cooling/pump/fan, drivers, personal data, and service dependencies. Preview real current values, show compatibility, request admin only when needed, create backups when supported, apply only on consent, verify real results, log failures, and support cancel/undo/rollback per action. Unsupported hardware must show N/A, not fabricated values.

## Validation / release gates

- Every visible button must have a real handler, stable ActionId, functional validation, and deterministic error state; no placeholder masquerading as complete.
- Validate V1/V2 parity with feature migration matrix and real runtime traces, not just route navigation.
- Run unit, integration, UI automation, install/uninstall/portable/upgrade, signed-package policy, admin/nonadmin, Windows 10/11, low-end/high-end/OEM, offline/reboot/crash/rollback tests.
- Capture redacted before/after evidence with hardware/environment metadata; never claim guaranteed FPS or ping improvements.
- Report exactly what is verified versus blocked. Only release stable when all mandatory gates pass.

## Current prototype truth

Dashboard telemetry, command review, reports, research values, activity, AI responses, and all buttons are sample interactions. This repo has **no Windows backend, no real AI provider, no native installer, no elevated worker, and no real benchmark instrumentation**.
