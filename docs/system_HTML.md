.doc { font-family: var(--font-sans); color: var(--color-text-primary); max-width: 860px; margin: 0 auto; padding: 2rem 1rem 4rem; } .hero { border-left: 3px solid #7F77DD; padding: 1rem 1.25rem; background: var(--color-background-secondary); border-radius: 0 var(--border-radius-lg) var(--border-radius-lg) 0; margin-bottom: 2rem; } .hero-label { font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: .08em; color: #534AB7; margin-bottom: 6px; } .hero h1 { font-size: 22px; font-weight: 500; margin: 0 0 6px; } .hero p { font-size: 14px; color: var(--color-text-secondary); margin: 0; line-height: 1.6; } .analogy { display: flex; gap: 12px; background: var(--color-background-secondary); border-radius: var(--border-radius-lg); border: 0.5px solid var(--color-border-tertiary); padding: 1rem 1.25rem; margin-bottom: 2rem; align-items: flex-start; } .analogy-icon { font-size: 22px; flex-shrink: 0; margin-top: 2px; } .analogy-body { font-size: 14px; color: var(--color-text-secondary); line-height: 1.7; } .analogy-body strong { color: var(--color-text-primary); } .node-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 1.5rem; } .node-card { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1rem 1.25rem; } .node-card-label { font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: .07em; color: var(--color-text-secondary); margin-bottom: 10px; } .node-stat { display: flex; justify-content: space-between; align-items: center; padding: 7px 0; border-bottom: 0.5px solid var(--color-border-tertiary); font-size: 14px; } .node-stat:last-child { border-bottom: none; } .node-stat .k { color: var(--color-text-secondary); } .node-stat .v { font-weight: 500; } .node-stat .v.accent { color: #534AB7; } .section-title { font-size: 18px; font-weight: 500; margin: 2rem 0 .4rem; display: flex; align-items: center; gap: 10px; } .section-num { font-size: 11px; font-weight: 500; background: #EEEDFE; color: #534AB7; border-radius: 20px; padding: 3px 10px; } .section-sub { font-size: 14px; color: var(--color-text-secondary); margin: 0 0 1.25rem; line-height: 1.6; } .callout { display: flex; gap: 10px; border-radius: var(--border-radius-md); padding: .875rem 1rem; font-size: 13px; line-height: 1.6; margin: 1rem 0 1.5rem; align-items: flex-start; } .callout-icon { font-size: 15px; flex-shrink: 0; } .callout.tip { background: #EEEDFE; color: #3C3489; border-left: 3px solid #7F77DD; border-radius: 0 var(--border-radius-md) var(--border-radius-md) 0; } .callout.ok { background: #E1F5EE; color: #085041; border-left: 3px solid #1D9E75; border-radius: 0 var(--border-radius-md) var(--border-radius-md) 0; } .what-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 10px; margin-bottom: 1.5rem; } .what-card { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: .875rem 1rem; } .what-card .wc-count { font-size: 22px; font-weight: 500; margin-bottom: 4px; } .what-card .wc-name { font-size: 13px; font-weight: 500; margin-bottom: 4px; } .what-card .wc-desc { font-size: 12px; color: var(--color-text-secondary); line-height: 1.5; } .wc-db .wc-count { color: #534AB7; } .wc-flink .wc-count { color: #0F6E56; } .wc-svc .wc-count { color: #185FA5; } .wc-mon .wc-count { color: #BA7517; } .wc-bk .wc-count { color: #993C1D; } .usage-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 1rem; } .metric { background: var(--color-background-secondary); border-radius: var(--border-radius-md); padding: .875rem 1rem; } .metric .mk { font-size: 12px; color: var(--color-text-secondary); margin-bottom: 4px; } .metric .mv { font-size: 20px; font-weight: 500; } .metric .ms { font-size: 12px; color: var(--color-text-secondary); margin-top: 2px; } .disk-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px,1fr)); gap: 8px; margin-bottom: 1.5rem; } .disk-pill { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-md); padding: .625rem .875rem; display: flex; justify-content: space-between; align-items: center; font-size: 13px; } .disk-pill .dp-name { color: var(--color-text-secondary); } .disk-pill .dp-val { font-weight: 500; } .disk-pill.total { background: #EEEDFE; border-color: #AFA9EC; } .disk-pill.total .dp-name { color: #3C3489; } .disk-pill.total .dp-val { color: #3C3489; } .disk-pill.opt .dp-val { color: var(--color-text-secondary); } .headroom-bar-wrap { margin-bottom: 1.5rem; } .hb-row { margin-bottom: 14px; } .hb-labels { display: flex; justify-content: space-between; font-size: 12px; color: var(--color-text-secondary); margin-bottom: 5px; } .hb-labels strong { color: var(--color-text-primary); } .hb-track { height: 10px; background: var(--color-background-secondary); border-radius: 20px; overflow: hidden; } .hb-fill { height: 100%; border-radius: 20px; } .hb-cpu { background: #7F77DD; width: 65%; } .hb-ram { background: #1D9E75; width: 31%; } .addon-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px,1fr)); gap: 12px; margin-bottom: 1.5rem; } .addon-card { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1rem 1.25rem; } .addon-badge { display: inline-block; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: .06em; padding: 2px 8px; border-radius: 20px; margin-bottom: 8px; } .badge-dial { background: #EEEDFE; color: #534AB7; } .badge-disc { background: #E1F5EE; color: #0F6E56; } .badge-vid { background: #E6F1FB; color: #185FA5; } .addon-name { font-size: 15px; font-weight: 500; margin-bottom: 4px; } .addon-desc { font-size: 13px; color: var(--color-text-secondary); margin-bottom: 12px; line-height: 1.5; } .addon-stat { display: flex; justify-content: space-between; font-size: 12px; padding: 5px 0; border-bottom: 0.5px solid var(--color-border-tertiary); } .addon-stat:last-child { border-bottom: none; } .addon-stat .ak { color: var(--color-text-secondary); } .addon-stat .av { font-weight: 500; } .compare-table { width: 100%; border-collapse: collapse; font-size: 13px; margin-bottom: 1.5rem; } .compare-table th { font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: .07em; color: var(--color-text-secondary); padding: 8px 12px; border-bottom: 0.5px solid var(--color-border-tertiary); text-align: left; } .compare-table td { padding: 10px 12px; border-bottom: 0.5px solid var(--color-border-tertiary); font-size: 13px; color: var(--color-text-secondary); } .compare-table td:first-child { font-weight: 500; color: var(--color-text-primary); } .compare-table .highlight td { background: #EEEDFE; } .compare-table .highlight td:first-child { color: #3C3489; } .compare-table .highlight td { color: #3C3489; } .val-base { color: #534AB7 !important; font-weight: 500 !important; } .val-all { color: #0F6E56 !important; font-weight: 500 !important; } .val-cap { color: var(--color-text-secondary) !important; } .summary-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; } .sum-card { border-radius: var(--border-radius-lg); padding: 1rem 1.25rem; border: 0.5px solid var(--color-border-tertiary); background: var(--color-background-primary); } .sum-card .sc-label { font-size: 12px; font-weight: 500; text-transform: uppercase; letter-spacing: .07em; color: var(--color-text-secondary); margin-bottom: 10px; } .sum-card .sc-row { display: flex; justify-content: space-between; font-size: 13px; padding: 4px 0; border-bottom: 0.5px solid var(--color-border-tertiary); } .sum-card .sc-row:last-child { border-bottom: none; } .sum-card .sc-row .k { color: var(--color-text-secondary); } .sum-card .sc-row .v { font-weight: 500; } .divider { border: none; border-top: 0.5px solid var(--color-border-tertiary); margin: 2rem 0; }

Sunbird-ED · DevOps Docs

# System Requirements

What you need before you start — explained plainly, no prior DevOps knowledge assumed.

💡

**New to cloud infrastructure?** Think of this like checking a game's system requirements — except instead of your laptop, you're renting two powerful computers in the cloud. The installer handles all the setup; you just need the right size machines ready.

What is a "node" and why two?

A **node** is a cloud virtual machine — a rented computer in the cloud. Sunbird needs two of them working as a team, managed by a system called **Kubernetes** that keeps all the software coordinated and running.

🍳 Node 1 — the kitchen

RunsDatabases & processors

ExamplesYugabyteDB, Kafka, Flink

RoleStores & processes all data

🍽️ Node 2 — front of house

RunsWeb services & APIs

ExamplesPortal, LMS, Keycloak

RoleHandles user traffic

- - -

01 Minimum Requirements

The least you need to run the full platform — databases, background jobs, all web services, monitoring, and backups — on your two rented nodes.

Each node (VM) spec

Azure VM typeStandard\_B16as\_v2

CPU per node16 vCPU

RAM per node64 GB

Combined cluster total

Total nodes2

Total CPU32 vCPU

Total RAM128 GB

💡 **vCPU** = "virtual CPU" — a unit of processing power. More vCPUs means more things can run simultaneously without slowing down.

What gets installed on these nodes

4

Databases

Stores users, courses, content, and settings

5

Background jobs

Handles certificates, notifications, events

14

App services

The APIs and portals users interact with

4

Monitoring

Dashboards for system health & logs

1

Backup system

Auto-backups your data (Velero)

Resource usage across those two nodes

CPU reserved

~21 cores

of 32 total

RAM reserved

~40 GB

of 128 GB total

Disk needed

~219 GB

across all services

💡 **Reserved vs. maximum:** "Reserved" is the guaranteed slice for each service — like booking a seat. "Maximum" is the burst ceiling. Services can briefly exceed their reserved amount on burstable VM types.

Where does the 219 GB of storage go?

YugabyteDB120 GB

Elasticsearch25 GB

Prometheus25 GB

Loki (logs)25 GB

Kafka24 GB

Total~219 GB

Redis (optional)+25 GB

- - -

02 Recommended Requirements

The recommended setup is the **exact same 2-node cluster**. No upgrade needed. These two tiers exist to show transparency — the minimum is what's used, and the recommended confirms there's comfortable room to grow.

How much headroom is left after the base install?

CPU used: **~21 of 32 cores (65%)**11 cores free

RAM used: **~40 of 128 GB (31%)**88 GB free

✅ You're using under a third of available RAM at baseline. That's a healthy buffer for traffic spikes, add-ons, and future growth — all without touching your node configuration.

- - -

03 Requirements with Add-ons Enabled

Add-ons are extra features that are off by default. You can turn them on after installation. Even enabling all three at once doesn't require any new nodes.

Optional

DIAL

Links QR codes to digital learning content. Scan a code, land on the right course.

Adds1 service + 2 jobs

Extra CPU+0.5 / +5 cores

Extra RAM+2 GB / +9 GB

Extra diskNone

Optional

Discussion Forum

Adds community discussion threads and group management, powered by NodeBB.

Adds3 services

Extra CPU+0.3 / +3 cores

Extra RAM+0.3 GB / +4 GB

Extra diskNone

Optional

Video Streaming

Converts uploaded videos into HLS format for smooth adaptive playback on any device.

Adds1 background job

Extra CPU+0.2 / +2 cores

Extra RAM+1 GB / +4 GB

Extra diskNone

Base vs. all add-ons vs. your cluster capacity

| Resource | Base only | \+ All add-ons | Cluster capacity |
| --- | --- | --- | --- |
| CPU reserved | ~21 cores | ~22 cores | 32 cores ✅ |
| CPU max burst | ~50 cores | ~60 cores | 32 cores (burstable) |
| RAM reserved | ~40 GB | ~43 GB | 128 GB ✅ |
| RAM max | ~74 GB | ~91 GB | 128 GB ✅ |
| Disk (storage) | ~219 GB | ~219 GB | Per cloud provider |

✅ All add-ons together add just ~1 extra CPU core and ~3 GB of RAM. Your cluster stays well within capacity — no infrastructure changes needed.

- - -

Quick summary

Base installation

Nodes2

CPU used~21 cores

RAM used~40 GB

Disk~219 GB

Base + all add-ons

Nodes2 (same)

CPU used~22 cores

RAM used~43 GB

Disk~219 GB

Node capacity

Nodes2

Total CPU32 cores

Total RAM128 GB

DiskPer cloud