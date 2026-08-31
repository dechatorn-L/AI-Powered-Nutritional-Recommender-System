# 🎨 UI/UX Design System & Style Guide (HealthTech Enterprise)

This document specifies the visual identity, navigation architecture, color palette, typography, and component specifications for the **NutriPulse Intelligence** web interface.

---

## 1. Visual Identity & Design Philosophy

The interface adopts a **HealthTech Enterprise / Precision Clinical Dashboard** aesthetic inspired by industry leaders such as Linear, Stripe, Apple Health, and Vercel:
- **Single-Tier Enterprise Top Navigation**: High-density horizontal navigation bar with brand identity, sliding active indicators, clinical health status pill, and discrete utilities (theme & language toggles).
- **Zero Decorative Emojis**: Replaced all emojis in tabs, headers, buttons, and badges with crisp, high-precision **Vector SVG icons**.
- **Structured Bento Grid Layouts**: Clean modular card architecture with hairline borders (`rgba(255, 255, 255, 0.07)` in dark mode, `rgba(226, 232, 240, 0.9)` in light mode), subtle glassmorphic backdrop filters (`blur(20px)`), and controlled elevation shadows.
- **Data-Dense Micro-Typography**: Plus Jakarta Sans for executive headings, Inter for high-legibility body text, and JetBrains Mono for quantified metrics.

---

## 2. Color Palette & Tokens

### 2.1 Core Accents

| Token | Hex Code | Description |
|---|---|---|
| `--brand-emerald` | `#10b981` | Primary clinical accent / Grade A (Healthy) indicator |
| `--brand-emerald-dark` | `#059669` | Hover states & solid buttons |
| `--brand-cobalt` | `#3b82f6` | Secondary analytical accent & baseline vector comparison |
| `--brand-amber` | `#f59e0b` | Warning states / Grade B (Moderate) indicator |
| `--brand-ruby` | `#ef4444` | Critical limit states / Grade C (Limit) indicator |
| `--brand-indigo` | `#6366f1` | Atwater energy consistency callout highlight |
| `--brand-cyan` | `#06b6d4` | Micronutrient & gradient end-stop |

### 2.2 Theme Surface Tokens

| Token | Dark Mode (`theme-dark`) | Light Mode (`theme-light`) |
|---|---|---|
| `--bg-app` | `#080c14` (Obsidian Titanium) | `#f8fafc` (Clean Slate) |
| `--bg-surface` | `#0e1422` (Charcoal Surface) | `#ffffff` (Pure White) |
| `--bg-surface-elevated` | `#141c2e` (Elevated Bento Card) | `#f1f5f9` (Subtle Card Tint) |
| `--border-subtle` | `rgba(255, 255, 255, 0.07)` | `rgba(226, 232, 240, 0.9)` |
| `--text-main` | `#f8fafc` (Crisp Light) | `#0f172a` (Deep Slate Ink) |
| `--text-muted` | `#94a3b8` (Muted Slate) | `#475569` (Charcoal) |
| `--text-dim` | `#64748b` (Subtle Label) | `#94a3b8` (Secondary Label) |

---

## 3. Navigation Architecture

```
+------------------------------------------------------------------------------------------------------+
| [NutriPulse INTELLIGENCE]  (🔍 Similarity) (🎯 Optimizer) (🧪 Grade AI) (📊 2D PCA) (📈 Analytics) |
|                                                      [● 1,014 Items · 98.0% Acc]  [TH/EN]  [🌙/☀️]   |
+------------------------------------------------------------------------------------------------------+
```

- **Brand Wrapper (Left)**: Minimal geometric pulse mark with brand title and intelligence badge.
- **Primary Feature Tabs (Center)**: Clean segmented pill navigation bar with SVG icons and active state elevation.
- **Utility Group (Right)**: Live system status pill, compact segmented language toggle (TH/EN), and theme switcher button.

---

## 4. Component Patterns

### 4.1 Command Search Bar
- Prefix search vector icon with instant input clearing button.
- Clean dropdown for retrieval count (Top 3, Top 5, Top 8, Top 10).
- Discovery chips with subtle border hover states.

### 4.2 Candidate Bento Cards
- Vector match proximity bar (`0% - 100%`) with gradient emerald-cyan fill.
- Inline 4-column nutrient metrics table with monospace font.
- High-protein, low-carb, and low-calorie tag badges.

### 4.3 Diagnostic Lab Panel
- Precision numeric matrix inputs with inline measurement unit tags (`g`, `mg`, `kcal`).
- Benchmark test case pills (`Clean Grade A`, `Balanced Grade B`, `High-Sugar Grade C`, `High-Lipid Grade C`).
- Large circular Grade Badge (`A`, `B`, `C`) with glowing radial gradient rim.
- Posterior class probability progress bars for all 3 classes.
