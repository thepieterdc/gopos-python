#!/bin/sh

set -e

# Start a GoPos container.
docker run -p 8000:8000 -d ghcr.io/thepieterdc/gopos:2.0.0