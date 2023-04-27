#!/bin/sh

cmd="$1"

echo "sdp command: [$cmd]"

if [[ "$cmd" == "sdp" ]]; then
  sdp
elif [[ "$cmd" == "sdpd" ]]; then
  sdpd
elif [[ "$cmd" == ""]]
  echo "ERROR: Must pass a cmd argument."
  exit 1
else
  echo "ERROR: Unknown command provided: $cmd"
  exit 1
done