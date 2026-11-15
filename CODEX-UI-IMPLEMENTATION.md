# HyperBoostX V3 — Production UI/UX implementation contract

**Product:** HyperBoostX V3 · **Brand:** NEXORAID · **Developer:** MR.4NONY

The attached HTML is a self-contained, non-mutating interactive design prototype. It is not a production optimizer or a replacement for the master development task. Its 73 design routes are proposed navigation, not the current verified legacy feature count. The current repository remains the source of truth. Implement production UI in the existing desktop framework (WPF/MVVM if present); do not ship the prototype as a shell or remove existing capabilities. Implement actual bindings, services, safety validation, and runtime verification. Continue until deliverables are built and validated in the available environment.

## 1. Identity
- Primary product lockup: HyperBoostX **V3**, small `by NEXORAID`.
- Brand footer: `NEXORAID / SYSTEM LAB` and `Developed by MR.4NONY`.
- Preserve exact capitalization and punctuation. Display attribution on splash, About, installer welcome, documentation, application file metadata where appropriate, and a discreet sidebar footer. Do not invent copyright year, URL, registered trademark, official partner endorsement, or release status.
- One unified edition; no Free/Pro/VIP badges or feature locks.
- Prototype monogram N is a proposed design; if authoritative brand assets exist in repo, use them. Avoid vendor trademarks as decoration suggesting endorsement.
- Tagline proposal: Make every resource count.

## 2. Design tokens
| Role | Dark | Light |
|---|---|---|
| Background | #0B1017 | #EEF3F8 |
| Surface | #111923 | #FFFFFF |
| Elevated panel | #151F2B | #F5F8FB |
| Border | #273647 | #D8E2EC |
| Text | #E8F0F7 | #172333 |
| Muted text | #8DA1B4 | #526679 |
| Primary accent | #5EEAD4 | #087E72 |
| Secondary accent | #67A9FF | #1769BC |
| Accent surface | #173C3B | #DEF6EF |
| Warning | #F6C16B | #98600A |
| Danger | #FC8493 | #B32642 |

Use Segoe UI (system fallback); tabular numbers for telemetry. 30 px page title, 22–24 px section hero, 15–16 px card headings, 13–14 px body, 11–12 px metadata. 4/8 px spacing base; 8–12 px radii. Thin line icons with shared stroke; consolidate inconsistent icons. Restrained glow and gradient; no perpetual motion. Do not encode state by color alone. Validate contrast for actual foreground/background combinations. System theme plus persistent dark and light overrides. Respect reduced motion, high contrast and OS DPI.

## 3. Layout and navigation
- Desktop target design 1440×900, minimum usable viewport 1024×600 subject to real DPI tests. Compact sidebar (~252 px expanded, ~64 px collapsed), header (~56 px), content page scroll independent of navigation. Responsive reflow for narrow window. Choose layout via effective WPF device-independent units, not fixed physical pixels.
- Header: product mark, global search (Ctrl+K), mode selector, notifications, theme, help/About, native window controls. Keyboard accelerators must not collide with OS shortcuts.
- Sidebar: collapsible module groups, route selection, search and favorites; remember last category and page; current page visible and announced. Footer: exact attribution.
- Main: breadcrumbs, purpose statement, state/capability summary, primary CTA, domain-specific workspace, evidence and history, contextual help. Shared status bar for worker health, pending restart and monitoring opt-in. Do not display a fake online/healthy status.
- `navigation.json` defines all 73 proposed routes with modules, actions and capability concepts. Merge it with discoverable legacy routes; generate mapping to actual ViewModels and action IDs. Never drop a route just to match 73.

## 4. Production page anatomy (not a generic table everywhere)
| Module | Required domain UI |
|---|---|
| Dashboard | Real telemetry metric tiles; charts with time/unit/legend; hardware summary; readiness score methodology; recent activity; safe quick actions. |
| Smart Scan | Scope selection, phase progress, cancel, findings grouped by severity; evidence drilldown; recommendation checklist. |
| One Click Boost | Plan preview grouped by risks and conflicts; compatibility, required privilege, backup; user approves eligible operations only. |
| AI Assistant / Provider | Chat transcript; context consent panel; provider/model selector; connection test; structured recommendations mapped to registered actions. Offline mode must be distinguished from generative provider. |
| CPU/GPU/RAM | Real sensor cards; per-process table; availability badges; supported policy form; separate measured and inferred data; exclusion editors. |
| Power / Profiles | Filterable profile cards, detailed selected actions, AC/DC state, diff, apply and restore. |
| Tweaks | Searchable catalog; category, risk and applied filters; current and desired values; multi-select; action details drawer. |
| Gaming | Game artwork only where licensed/available, otherwise icons; library list, executable path, launch state, session controls, per-game profiles and restore. |
| FPS / Stutter | Frame-time timeline, sample count, average FPS, lows and measurement limitations; event correlation, comparison. |
| Hardware / Drivers | Component tree, actual vendor and device identifiers, versions and health evidence; official guidance; capability matrix. |
| Windows / Services / Tasks / Startup | Filter/sort tables with dependencies, protected states, reversible controls, before/after diffs. |
| Storage / Cleanup | Volume tree, capacity bars, preview file candidates, exclusions, size estimate vs actual reclaimed bytes. |
| Network | Adapter list, traffic, endpoint input, DNS and latency history, active remote-session warning before resets. |
| Creator / Audio / Webcam | Encoder capabilities and workload; endpoint inventory; active-session protections; no unapproved camera/mic access. |
| LCD / RGB / MSI | Detected utilities and measurable resource overhead; cooldown, threshold, allowlist and critical cooling dependencies. |
| Security / Privacy | Read-only security status; consent toggles; privacy export/delete; no weakening protections. |
| Automation | Trigger-condition-action editor, validation, opt-in enable, pause, history, emergency stop. |
| Backup / Restore | Snapshot list, scope, integrity, age, comparison, conflict resolution and verified rollback. |
| Benchmark / Research | Actual test configuration, repetitions, A/B/C/D conditions, charts and raw exports; missing data and regressions. |
| Test Center | PASS/FAIL/BLOCKED/SKIPPED/NOT RUN/UNSUPPORTED, timestamps, evidence, filters and safe diagnostics. |
| Settings / License / About | Theme, language, verbosity, monitoring, privacy, local state and exact branding; no fictional online entitlement. |
| Webhook / Plugin / Updates | Real configuration and connection state; permissions and trust; redaction preview; signed package status. |

## 5. Interaction, safety, and lifecycle
1. Read-only scan → source and timestamp → findings → recommended actions.
2. Mutation → validate capabilities and parameters → preview exact before/after state, risks, restart and privilege → approve → backup (when required) → execute through registered action engine → independently verify → evidence/history → rollback if available.
3. Distinguish already applied, success, verification failed, partially applied, cancelled, blocked, permission denied, unsupported, restart required and rolled back. Do not equate process exit or HTTP 200 with outcome.
4. Use inline progress with real phase names and cancel mechanics; do not invent percentage or completion time. Keep UI responsive. Pending restart state persists correctly.
5. Failed actions show explanation, error identifier, troubleshooting, retry only where safe and rollback/recovery options. Do not auto-retry unrepeatable mutations.
6. Expose plain-language details before a destructive action; show affected files/configurations, rollback limitations and explicit consent. Safety Guard applies to Beginner, Advanced and Expert alike. Expert cannot bypass safety.
7. Sections must handle first run, loading, no results, missing sensors, unsupported device, backend offline, denied permission, UAC cancellation, no internet, invalid input, pending reboot, and failed verification.
8. Production UI must use real runtime sources; display N/A/Unknown/Not tested with reason instead of fake metrics. The HTML deliberately labels sample dashboard readings; remove these from production. Do not ship simulation as functional UI.

## 6. Additional required screens and overlays
- Splash: product mark, `HyperBoostX V3`, `by NEXORAID`, `Developed by MR.4NONY`, real startup phase; no false splash progress.
- First run wizard: welcome, compatibility, privacy, safety and restore, optional providers, initial scan. Skip optional integrations; no forced registration.
- Global command palette; notification center; action details; confirmation; backup and progress dialog; cancellation; verify result; rollback conflict dialog; error details; export preview; update confirmation; recovery UI.
- Installer: branding, compatibility, installation location, progress, actual success/failure, optional launch; preserve real uninstaller support. About: build revision, version, runtime, license notices, exact developer credit.
- UI language architecture: English initial labels, Indonesian resource dictionary; code-independent strings, no concatenation of localized sentences, local number/date formats. Actual language switching only if fully wired and tested.

## 7. WPF/MVVM handoff
- Derive theme ResourceDictionaries and reusable styles from token table; avoid duplicated page-specific styles. If another desktop stack is already approved, implement equivalent resources there.
- Define ViewModels with typed observable status, async commands, cancellation, capability gating, validation and disposal. Map UI routes to registered feature IDs, commands to registered action IDs. Add separate services for telemetry, scan, evidence/history and preference persistence. Marshal UI updates to dispatcher and coalesce high-frequency samples.
- Implement reusable controls: AppShell, SidebarGroup, SearchPalette, MetricCard, TelemetryChart, StatusBadge, FeatureCard, DataTable, FilterBar, EmptyState, CapabilityWarning, ActionPlanPreview, ApprovalDialog, OperationProgress, EvidencePanel, RestoreConflictDialog, Toast/Notifications.
- Use resource-based icon paths; preserve credits and titles without hardcoding release status. Virtualize large tables and navigation; debounce search; stop polling hidden pages; respect battery and monitoring settings. No unnecessary WebView/browser runtime added just for appearance.
- The prototype is not a XAML source file. Recreate domain-specific views and wire actual handlers; do not paste HTML into WPF and claim completion.

## 8. QA acceptance
- Generate route coverage from repository and compare to legacy map plus proposed navigation. Verify each visible route opens and unsupported routes provide explanation. Validate 100% of visible actionable controls are mapped to navigation, read-only handler or approved real action; no dead controls.
- Validate keyboard focus, search, themes, DPI 100/125/150/200%, scaling and resize, readable text, scrolling, accessibility labels, no clipped dialogs, error handling and evidence display. Exercise localization and long Indonesian labels. Test collapsed and expanded sidebar.
- Test first-run and returning-user flows, standard and admin accounts, denied UAC, missing sensors, offline providers, concurrent sessions, rollback, crash/restart recovery and cleanup previews. Test actual mutations only in safe isolated Windows environments.
- Capture actual screenshots of final installed product (dark/light dashboard, Gaming, AI, tweak catalog, backup/rollback, Test Center, About, installer and failure states). Report tested vs blocked clearly.
- Measure idle combined resource use and startup; no decorative animations harming low-spec target. Compare same build/revision and conditions.
- Package validated installer(s) and evidence per master task; do not classify as Stable without real Windows validation. The HTML prototype is a design reference only.

## 9. Delivery
Deliver updated project files, real XAML/resources/ViewModels (or equivalent current stack), route/action mapping, UI tests, screenshot evidence, release artifacts, and a UI readiness report. Do not stop at mockups or documentation. Keep `DEVELOPMENT_PROGRESS.md` updated. No public publishing or destructive repository operations without authorization.
