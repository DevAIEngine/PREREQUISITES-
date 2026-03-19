#!/bin/bash
# make_episode.sh
# Target: The Nomadic Administrator (Cell Phone / Termux / Cloud Shell)
# Usage: ./make_episode.sh "https://docs.google.com/document/d/YOUR_SCRIPT_URL"

SCRIPT_URL=$1
PROJECT_ID=$(uuidgen | cut -d'-' -f1)

echo "🎬 Starting Google Universe Cinematic Engine (GUCE) - Assembly Line"
echo "Project ID: $PROJECT_ID"
echo "Source Script: $SCRIPT_URL"

if [ -z "$SCRIPT_URL" ]; then
  echo "❌ Error: Please provide a Google Docs Script URL."
  echo "Usage: ./make_episode.sh 'https://docs.google.com/document/d/...'"
  exit 1
fi

echo "🚀 Connecting to Cloud Run Orchestrator (us-west2)..."
# In production, this curl triggers the FastAPI OrchestrationAssemblyLine
# POST /api/orchestration/publish
curl -X POST https://guce-engine-0446134261-uc.a.run.app/api/orchestration/publish \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "'$PROJECT_ID'",
    "script_url": "'$SCRIPT_URL'",
    "mode": "FULL_CASCADE"
  }'

echo ""
echo "✅ Episode assembly initiated! The AI Swarm is currently:"
echo "   1. Pre-generating 1,000 Free Gemini Images into Google Slides"
echo "   2. Rendering the 5-Minute Core Video via Google Vids"
echo "   3. Expanding to the 30-Minute VeoChainer Documentary"
echo "   4. Extracting 3x YouTube Shorts (Vertical 9:16)"
echo "   5. Synthesizing Multilingual Audio Podcasts for Spotify"

echo ""
echo "📊 Track progress in your Google Sheets Narration Library or check the Drive Manifest: GUCE_$PROJECT_ID"
