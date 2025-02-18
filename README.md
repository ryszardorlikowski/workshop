## 🔐 Secret Management with SOPS

### Installation
```bash
# For Linux (Debian/Ubuntu):
sudo apt-get install sops age

# For macOS (using Homebrew):
brew install sops age
```

### 🔑 Generating Keys
```bash
# 1. Create key pair
age-keygen -o age.key

# 2. Store private key securely
mv age.key ~/.ssh/ && chmod 600 ~/.ssh/age.key

# 3. Configure SOPS
echo 'creation_rules:
  - path_regex: .*\.enc$
   "'$(cat age.key.pub)'"' > .sops.yaml
    
# or use copy-paste
```

### 🔒 Encrypting Files
```bash
# Encrypt file
sops --encrypt --config .sops.yaml  --input-type dotenv --output-type dotenv .env.prod > .env.prod.enc
```

### 🔓 Decrypting Files
```bash
export SOPS_AGE_KEY_FILE=~/.ssh/age.key
# Decrypt file
sops --decrypt --input-type dotenv --output-type dotenv .env.prod.enc > .env
```