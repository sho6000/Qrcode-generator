# System Requirements

Sunbird-ED is deployed entirely on cloud infrastructure. Before running the installer, make sure your cloud environment is provisioned and ready.

---

## Minimum requirements

Sunbird-ED runs on a two-node Kubernetes cluster. The installer sets everything up automatically — you just need the nodes ready on your cloud provider.

### Supported cloud providers

| Provider | Description |
|----------|-------------|
| Microsoft Azure | Reference platform — tested and verified with the installer |
| Amazon Web Services | Supported — provision equivalent VM types to the Azure reference |
| Google Cloud Platform | Supported — provision equivalent VM types to the Azure reference |

### Node specification

Each node should meet the following specification. Both nodes must be identical.

| Specification | Requirement |
|---------------|-------------|
| VM type (Azure) | `Standard_B16as_v2` |
| vCPU per node | 16 vCPU |
| RAM per node | 64 GB |

### Databases

All databases are installed and managed automatically within the cluster. No external database setup is required.

| Database | Purpose |
|----------|---------|
| YugabyteDB | Primary distributed database for all platform data |
| Elasticsearch | Powers content search and discovery across the platform |
| JanusGraph | Graph database for knowledge and content relationships |
| Redis | Optional caching layer — disabled by default |

### What else runs on the cluster

Beyond databases, the cluster also runs the following:

| Component | Description |
|-----------|-------------|
| Background processors | Handles certificate generation, notifications, and event processing |
| Application services | The APIs and web portals that users and admins interact with |
| Monitoring stack | Dashboards and alerting for system health and logs |
| Backup system | Automated backup and disaster recovery |

---

## Recommended requirements

The recommended setup uses the same two-node cluster as the minimum. No additional nodes or upgrades are needed.

The cluster is sized to leave comfortable headroom beyond what the base platform uses. This means you can enable add-ons, absorb traffic spikes, and grow — all without touching your infrastructure.

---

## Requirements with add-ons enabled

Add-ons are optional features that are disabled by default. They can be enabled at any time after the base installation.

Even with all add-ons running at once, **no additional nodes are required**. The base cluster has enough capacity to handle them comfortably.

### Available add-ons

**DIAL**

Enables QR code–based content linking. Learners can scan a code and land directly on the linked course or resource.

**Discussion Forum**

Adds community discussion threads and group management to the platform, powered by NodeBB.

**Video Streaming**

Converts uploaded videos into a streamable format for smooth playback across devices and network conditions.

> All add-ons are self-contained — they run inside the existing cluster and do not require additional storage or infrastructure.

---

For further reference, please visit [ReadME](https://github.com/Sunbird-Spark/sunbird-spark-installer/blob/develop/INFRA_DETAILS.md).