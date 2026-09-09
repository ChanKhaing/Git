Markdown
# 🚀 GitLab CI/CD Self-Hosted Runner Setup Guide

This documentation provides a step-by-step guide to setting up and troubleshooting a self-hosted **GitLab Shell Runner** on a local Linux machine.

---

## 🛠️ Prerequisites
* **OS:** Linux (Ubuntu/Debian)
* **Tools:** `git`, `gitlab-runner`, `bash`
* **Account:** GitLab.com Account (No Credit Card Verification needed)

---

## 📌 Step 1: Create a Project Runner in GitLab

1. Go to your GitLab Repository: **Settings > CI/CD > Runners**.
2. Click **New project runner**.
3. **Configuration:**
   * Leave **Tags** empty (optional).
   * Check **"Run untagged jobs"** (Critical ⚠️).
4. Click **Create runner** and copy the generated **`glrt-xxxxx`** Registration Token.

---

## 📌 Step 2: Register & Configure Runner (Local Terminal)

If you encounter `403 Forbidden` errors or outdated registration tokens, reset the configuration first:

```bash
# 1. Force remove old local configuration
sudo rm -f /etc/gitlab-runner/config.toml

# 2. Register the new runner
sudo gitlab-runner register
Interactive Registration Prompts:
GitLab instance URL: https://gitlab.com

Token: Paste your glrt-xxxxx token

Description: my-local-runner

Tags: (Press Enter to skip)

Maintenance Note: (Press Enter to skip)

Executor: shell

📌 Step 3: Start the Runner Service
Ensure the runner service is active in the background:

Bash
# Install and start the system service
sudo gitlab-runner install
sudo gitlab-runner start

# Check the service status
sudo gitlab-runner status


#before you are testing on the gitlab.com,you need to do one thing 
sudo gitlab-runner run 
# just  leave this terminal alone and don't shut down 
#now you can start cicd test on gitlab.com