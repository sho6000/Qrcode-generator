# One-Click Installer

The one-click installer sets up a full Sunbird-ED deployment on your cloud infrastructure. It provisions the cluster, installs all services, and configures the platform automatically — you just need to prepare a few things before running it.

---

## Before you begin

Make sure the following are ready before starting the installation.

### Required

| Requirement | Description |
|-------------|-------------|
| Domain name | A registered domain that will point to your Sunbird-ED instance |
| SSL certificate | A FullChain certificate — includes the private key, certificate, and CA bundle |
| Google OAuth credentials | Used for user authentication — [set up here](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id) |
| Google reCAPTCHA v3 credentials | Used to protect public-facing forms — [set up here](https://www.google.com/recaptcha/admin) |
| Email service provider | Any SMTP-compatible email service for sending platform emails |

### Optional

| Requirement | Description |
|-------------|-------------|
| MSG91 API token | Required if you want to send OTPs via SMS during registration or password reset |
| YouTube API token | Required if you want users to upload video content via YouTube URL |

---

## Required tools

Install the following tools on the machine you'll run the installer from.

| Tool | Description |
|------|-------------|
| `jq` | Command-line JSON processor — [install](https://jqlang.github.io/jq/download/) |
| `yq` | Command-line YAML processor — [install](https://github.com/mikefarah/yq#install) |
| `rclone` | Cloud storage sync tool — [install](https://rclone.org/) |
| `OpenTofu` | Infrastructure provisioning tool — [install](https://opentofu.org/docs/intro/install/) |
| `Terragrunt` | Wrapper for OpenTofu to manage environments — [install](https://terragrunt.gruntwork.io/docs/getting-started/install/) |
| `kubectl` | Kubernetes command-line tool — [install](https://kubernetes.io/docs/tasks/tools/) |
| `helm` | Kubernetes package manager — [install](https://helm.sh/docs/intro/quickstart/#install-helm) |
| `Postman CLI` | Runs the post-install API setup — [install](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/) |
| Python 3 | Required for helper scripts |
| PyJWT | Python package — install via `pip install PyJWT` |

For cloud-specific tools such as the Azure CLI, AWS CLI, or gcloud, follow the instructions in the provider-specific README inside the repository.

> The installer has been verified with **OpenTofu v1.11.4** and **Terragrunt v0.77.5**. If you run into issues with other versions, try these.

---

## Installation

### 1. Clone the repository

Start by cloning the installer repository to your local machine. You can find it at `github.com/project-sunbird/sunbird-ed-installer`.

### 2. Set up your environment directory

Inside the repository, navigate to your cloud provider's folder under `opentofu/`. Copy the `template` directory and give it the name of your environment — for example, `demo`, `dev`, `staging`, or `prod`.

### 3. Configure global values

Open `global-values.yaml` inside your environment directory and fill in your domain, SSL certificate, OAuth credentials, and other required values. Refer to the provider-specific README for field-by-field guidance.

### 4. Log in to your cloud provider

Authenticate with your cloud provider using its CLI before running the installer. Each provider has its own login command — refer to your provider's documentation if needed.

### 5. Run the installer

From inside your environment directory, run `./install.sh`. The installer will provision your infrastructure, deploy all services, and configure the platform. This may take a while depending on your cloud provider and network speed.

> **Note:** The installer will back up and overwrite the rclone and kubeconfig files on your machine if they already exist. Existing versions are saved with a `.bak` extension.

---

## Default users

The installer creates the following users automatically. You can update passwords using the **Forgot Password** flow, or create new users via the admin API.

| Role | Email | Default password |
|------|-------|-----------------|
| Admin | admin@yopmail.com | Admin@123 |
| Content Creator | contentcreator@yopmail.com | Creator@123 |
| Content Reviewer | contentreviewer@yopmail.com | Reviewer@123 |
| Book Creator | bookcreator@yopmail.com | Bookcreator@123 |
| Book Reviewer | bookreviewer@yopmail.com | bookReviewer@123 |
| Public User 1 | user1@yopmail.com | User1@123 |
| Public User 2 | user2@yopmail.com | User2@123 |

> Update default passwords after your first login.

---

## SSL certificate setup

### Using Let's Encrypt

To enable automatic SSL certificate management, set `lets_encrypt_ssl` to `true` in your `global-values.yaml`. When enabled, a Kubernetes CronJob handles certificate issuance and renewal automatically.

After each renewal, fetch the updated certificate values from the `nginx-public-ingress` ConfigMap and update the `proxy_private_key` and `proxy_certificate` fields in your `global-values.yaml`.

### Using a custom certificate

If you're managing your own SSL certificate, set `lets_encrypt_ssl` to `false` in your `global-values.yaml` and provide your certificate and private key under `proxy_certificate` and `proxy_private_key`.

---

## Destroying the deployment

To tear down all provisioned infrastructure, navigate to your environment directory and run `./install.sh destroy_tf_resources`.

> This permanently removes all resources provisioned by the installer for that environment. Make sure you have backups before proceeding.