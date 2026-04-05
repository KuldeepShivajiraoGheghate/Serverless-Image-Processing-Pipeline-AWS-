# ☁️ Serverless Image Processing Pipeline — AWS

![AWS](https://img.shields.io/badge/AWS-Lambda-orange?logo=amazonaws)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![S3](https://img.shields.io/badge/Amazon-S3-green?logo=amazons3)
![Pillow](https://img.shields.io/badge/Pillow-10.4.0-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A fully serverless, event-driven image processing pipeline built on AWS.
When an image is uploaded to S3, it **automatically triggers** a Lambda function
that resizes the image and saves it to a separate output bucket —
with zero manual intervention.

---

## 📐 Architecture
```
User Uploads Image
│
▼
┌─────────────────────┐
│   S3 Input Bucket   │  image-upload-bucket-kuldeep
│   (Trigger Source)  │
└────────┬────────────┘
│  S3 PUT Event
▼
┌─────────────────────┐
│   AWS Lambda        │  image-processing-lambda
│   Python 3.12       │  Pillow for resizing
└────────┬────────────┘
│  Processed Image
▼
┌─────────────────────┐
│   S3 Output Bucket  │  processed-image-bucket-kuldeep
│   processed/        │
└─────────────────────┘
```
---

## ✨ Features

- ✅ Fully Serverless — No servers to manage
- ✅ Event-Driven — Auto-triggers on every image upload
- ✅ Image Resizing — Resizes to 200x200 using Pillow
- ✅ Zero Cost on Idle — Pay only when processing
- ✅ CloudWatch Logging — Full logs for every execution
- ✅ Free Tier Friendly — Runs within AWS Free Tier

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Amazon S3 | Store input and output images |
| AWS Lambda | Serverless compute |
| Python 3.12 | Lambda runtime |
| Pillow 10.4.0 | Image resizing |
| boto3 | AWS SDK for Python |
| CloudWatch | Logging and monitoring |

---

## 📁 Project Structure
```
serverless-image-pipeline/
│
├── src/
│   └── lambda_function.py      ← Main Lambda handler
│
├── docs/
│   └── screenshots/            ← Project screenshots
│
├── tests/
│   └── test_lambda.py          ← Unit tests
│
├── build.ps1                   ← Windows build script
├── requirements.txt            ← Python dependencies
├── .gitignore                  ← Git ignore rules
└── README.md                   ← Project documentation
```
---

## 🚀 Deployment Guide

### Step 1 — Create S3 Buckets
Create 2 buckets in AWS S3 (same region):
- `image-upload-bucket-kuldeep` — Input bucket
- `processed-image-bucket-kuldeep` — Output bucket

### Step 2 — Create Lambda Function
- Name: `image-processing-lambda`
- Runtime: Python 3.12
- Architecture: x86_64

### Step 3 — Add S3 Permissions
Attach `AmazonS3FullAccess` policy to Lambda IAM role.

### Step 4 — Build Deployment ZIP
```powershell
.\build.ps1
```

### Step 5 — Upload ZIP to Lambda
Upload `deployment.zip` via Lambda Console → Code → Upload from .zip

### Step 6 — Add S3 Trigger
- Bucket: `image-upload-bucket-kuldeep`
- Event: PUT
- Suffix: .jpg

---

## 🔍 CloudWatch Logs Output
[START] Processing file: photo.jpg
[INFO]  Source Bucket: image-upload-bucket-kuldeep
[STEP 1] Downloading image from S3...
[STEP 1] Download complete!
[STEP 2] Resizing image to 200x200...
[STEP 2] Resized from (3840, 2160) to (200, 200)
[STEP 3] Uploading to output bucket...
[STEP 3] Upload complete!
[DONE] Image processed successfully!

---

## ⚠️ Common Issues

| Error | Cause | Fix |
|---|---|---|
| `No module named PIL` | Wrong Pillow build | Run build.ps1 again |
| `cannot import _imaging` | Windows Pillow on Linux | Use manylinux platform flag |
| `Access Denied` | Missing S3 permissions | Attach AmazonS3FullAccess |
| Image not appearing | Wrong bucket name | Check OUTPUT_BUCKET variable |

---

## 💡 What I Learned

- ✔ Event-driven architecture on AWS
- ✔ Serverless computing with Lambda
- ✔ S3 bucket policies and event notifications
- ✔ IAM roles and permissions
- ✔ CloudWatch monitoring and debugging
- ✔ Python packaging for Linux on AWS
- ✔ Platform compatibility (Windows vs Linux)

---

#👨‍💻 Author

Kuldeep Gheghate  
Computer Engineering Student – PCCOE 

---

> ⭐ If this helped you, please give it a star!

