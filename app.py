name: Snyk Security Scan

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  snyk:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Run Snyk auth
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        run: |
          pip install snyk
          snyk auth $SNYK_TOKEN

      - name: Run Snyk test
        run: snyk test --severity-threshold=high --json > snyk_report.json

      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: snyk-report
          path: snyk_report.json


args: --sarif-file-output=snyk.sarif
      - name: Print the Snyk sarif file
        run : cat snyk.sarif
