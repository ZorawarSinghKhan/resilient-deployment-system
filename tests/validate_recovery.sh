#!/bin/bash

echo "Checking application recovery..."

READY_PODS=$(kubectl get pods -l app=chaos-app \
  --field-selector=status.phase=Running \
  --no-headers | wc -l)

echo "Running Pods: $READY_PODS"

if [ "$READY_PODS" -ge 2 ]; then
    echo "PASS: Application recovered successfully"
    exit 0
else
    echo "FAIL: Application did not recover"
    exit 1
fi
