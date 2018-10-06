#!/bin/bash
time (for i in {1..1000}; do curl -i http://localhost:8002/v0/api & done; wait)

