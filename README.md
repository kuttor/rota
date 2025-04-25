# rota

A Python CLI tool for managing versioned files in AWS S3 buckets. Built with boto3, rota helps you:

- Clean up old versions
- Generate version reports
- Rotate versioned files

## 🚀 Installation

```bash
pip install git+https://github.com/kuttor/rota.git
```

## 🔧 Configuration

- Default location: `$XDG_CONFIG_HOME/rota/rota.conf`  
- Custom location: `export ROTA_CONFIG_FILE=/path/to/rota.conf`

## 📦 Features

- **Counts**: Easily upload files to specified S3 buckets.
- **Sorts**: Retrieve files from S3 buckets to your local machine.
- **Compares**: View the contents of your S3 buckets.
- **Deletes**: Remove objects from your S3 buckets.
- **Profile Management**: Utilize different AWS profiles for various environments.
