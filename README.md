name: Auto Update README

on:
  push:
    paths:
      - README.md

jobs:
  notify-readme-update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Notify on README update
        run: echo "README.md was updated in this push!"
