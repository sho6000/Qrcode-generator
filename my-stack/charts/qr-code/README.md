# QR Code Generator Helm Chart

A Helm chart for deploying the QR Code Generator application with PostgreSQL on Kubernetes.

## Features

- Streamlit-based QR code generator web application
- PostgreSQL database integration
- Cross-namespace service communication
- Persistent volume support
- LoadBalancer service for external access
- Configurable database credentials
- Resource limits and health checks

## Prerequisites

- Kubernetes 1.19+
- Helm 3.x
- PostgreSQL database (separate deployment)

## Installation

```bash
# Add this repository
helm repo add qr-app https://sho6000.github.io/helm-charts/
helm repo update

# Install the chart
helm install my-app qr-app/qr-app -n my-namespace --create-namespace

# Or with custom values
helm install my-app ./app -f my-values.yaml
```

## Configuration

| Parameter | Description | Default |
|-----------|-------------|---------|
| `replicaCount` | Number of app replicas | `1` |
| `image.repository` | Image repository | `shoun6000/qr-generator` |
| `image.tag` | Image tag | `latest` |
| `service.type` | Service type | `LoadBalancer` |
| `service.port` | Service port | `8501` |
| `resources.requests.memory` | Memory request | `256Mi` |
| `resources.limits.memory` | Memory limit | `512Mi` |

## Environment Configuration (ConfigMap)

The ConfigMap is rendered from `envConfig` in values.yaml and injected via `envFrom`.

```yaml
envConfig:
  DB_HOST: db-postgresql.qr-db.svc.cluster.local
  DB_PORT: "5432"
  POSTGRES_USER: admin
  POSTGRES_DB: qr_database
```

## Secrets Configuration (Secret)

The Secret is rendered from `secretConfig` in values.yaml (base64 encoded) and injected via `envFrom`.

```yaml
secretConfig:
  POSTGRES_PASSWORD: admin
```

## Usage with Override File

Create a custom values file (example: `my-secret.yaml`):

```yaml
envConfig:
  DB_HOST: db-postgresql.qr-db.svc.cluster.local
  DB_PORT: "5432"
  POSTGRES_USER: myuser
  POSTGRES_DB: mydatabase

secretConfig:
  POSTGRES_PASSWORD: mypassword
```

Deploy with overrides:
```bash
helm install my-app ./app -f my-secret.yaml
```

## Uninstall

```bash
helm uninstall my-app -n my-namespace
```

## License

MIT

## Support

For issues and questions, visit the GitHub repository.
