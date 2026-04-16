# Enabling Add-ons

Add-ons are optional features that are disabled by default. They can be enabled at any time after the base installation is complete. No additional infrastructure is required — the base cluster has enough capacity to run all add-ons simultaneously.

---

## Available add-ons

| Add-on | Description | How to enable |
|--------|-------------|---------------|
| DIAL | QR code–based content linking | Flag in `global-values.yaml` + deploy add-on scripts |
| Discussion Forum | Community discussion threads and group management | Deploy add-on scripts |
| Video Stream Generator | Converts uploaded videos into a streamable format | Deploy add-on scripts |
| Asset Enrichment | Automatic enrichment of uploaded video and image assets | Flag in `global-values.yaml` |

---

## DIAL

DIAL (Digital Infrastructure for Augmented Learning) enables QR code–based content linking. Learners can scan a QR code and be taken directly to the linked course or resource.

Enabling DIAL requires two things — setting a flag in your config so core services know DIAL is present, and deploying the DIAL add-on scripts separately.

**Step 1 — Update `global-values.yaml`**

Set `deployed_dial_addon` to `true`. This tells the core services to include DIAL-specific routing and configuration.

**Step 2 — Deploy the add-on**

Run the add-on deployment scripts located in the `addons/dial` directory of the installer repository.

> Set this flag before or alongside deploying the DIAL add-on. Core services need to be redeployed with the flag enabled for the integration to work.

---

## Discussion Forum

The Discussion Forum add-on adds community discussion threads and group management to the platform, powered by NodeBB.

To enable it, run the add-on deployment scripts located in the `addons/` directory. No changes to `global-values.yaml` are required.

---

## Video Stream Generator

The Video Stream Generator converts uploaded videos into HLS (HTTP Live Streaming) format, enabling smooth adaptive playback across devices and network conditions.

To enable it, run the add-on deployment scripts located in the `addons/` directory. No changes to `global-values.yaml` are required.

---

## Asset Enrichment

Asset Enrichment automatically processes uploaded video and image assets — generating thumbnails and extracting metadata to improve content discoverability.

To enable it, set `enable_asset_enrichment` to `true` in your `global-values.yaml` and redeploy. It is disabled by default.

---

## Quick reference

| Add-on | `global-values.yaml` flag | Deploy scripts required |
|--------|--------------------------|------------------------|
| DIAL | `deployed_dial_addon: true` | Yes — `addons/dial` |
| Discussion Forum | Not required | Yes — `addons/` |
| Video Stream Generator | Not required | Yes — `addons/` |
| Asset Enrichment | `enable_asset_enrichment: true` | No |