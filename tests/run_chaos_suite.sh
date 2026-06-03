#!/bin/bash

echo "================================="
echo "Running Chaos Validation Suite"
echo "================================="

TESTS=(
  "chaos/pod-chaos.yaml"
  "chaos/cpu-stress.yaml"
  "chaos/memory-stress.yaml"
  "chaos/network-delay.yaml"
  "chaos/packet-loss.yaml"
)

for TEST in "${TESTS[@]}"
do
  echo ""
  echo "Running $TEST"

  kubectl apply -f $TEST

  echo "Waiting for recovery..."
  sleep 30

  ./tests/validate_recovery.sh

  kubectl delete -f $TEST --ignore-not-found=true

  echo "Completed $TEST"
done

echo ""
echo "Chaos Validation Suite Finished"
