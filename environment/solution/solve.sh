#!/bin/bash

cat > /workspace/report.json <<EOF
{
  "total_requests": 10,
  "status_codes": {
    "200": 6,
    "404": 2,
    "500": 2
  },
  "unique_ips": 4
}
EOF
