#!/bin/bash
# IAM Permissions & Cloud Run Deployment Script
# Target Project: gen-lang-client-0446134261
# Target SA: guce-sa@gen-lang-client-0446134261.iam.gserviceaccount.com

SA="guce-sa@gen-lang-client-0446134261.iam.gserviceaccount.com"
PROJECT="gen-lang-client-0446134261"

echo "Applying IAM Roles to $SA..."

gcloud projects add-iam-policy-binding $PROJECT \
  --member="serviceAccount:$SA" \
  --role="roles/aiplatform.user"

gcloud projects add-iam-policy-binding $PROJECT \
  --member="serviceAccount:$SA" \
  --role="roles/drive.editor"

gcloud projects add-iam-policy-binding $PROJECT \
  --member="serviceAccount:$SA" \
  --role="roles/sheets.editor"

gcloud projects add-iam-policy-binding $PROJECT \
  --member="serviceAccount:$SA" \
  --role="roles/secretmanager.secretAccessor"

gcloud projects add-iam-policy-binding $PROJECT \
  --member="serviceAccount:$SA" \
  --role="roles/run.invoker"

echo "IAM Roles Applied. Verifying..."
gcloud projects get-iam-policy $PROJECT \
  --filter="bindings.members:serviceAccount:$SA" \
  --flatten="bindings[].role"

echo "Deploying to Cloud Run..."
gcloud builds submit --tag gcr.io/$PROJECT/guce-engine .

gcloud run deploy guce-engine \
  --image gcr.io/$PROJECT/guce-engine \
  --region us-west2 \
  --service-account $SA \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_CLOUD_PROJECT=$PROJECT

echo "Deployment Complete!"