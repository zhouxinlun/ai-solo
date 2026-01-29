#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: solo-notify.sh <ROLE> <TEXT>"
  echo "ROLE: PM | ARCH | BE | FE | QA"
}

role="${1:-}"
text="${*:2}"

if [[ -z "${role}" || -z "${text}" ]]; then
  usage
  exit 1
fi

case "${role}" in
  PM|ARCH|BE|FE|QA) ;;
  *)
    echo "Error: role must be one of PM|ARCH|BE|FE|QA"
    exit 1
    ;;
esac

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
notify_script="${root_dir}/docs/notify_role.py"

if [[ ! -f "${notify_script}" ]]; then
  echo "Error: notify_role.py not found at ${notify_script}"
  exit 1
fi

python "${notify_script}" "${role}" "${text}"
