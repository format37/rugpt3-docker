#!/bin/bash
mkdir -p ./transformers
sudo docker run -it --rm \
    --network host \
    --gpus device=0 \
    -v $(pwd)/transformers:/custom_cache \
    -e TRANSFORMERS_CACHE=/custom_cache \
    rugpt-3.5:latest
