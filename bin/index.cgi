#!/bin/bash
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

### VARIABLES ###
md="$contentsdir/posts/template/main.md"

### OUTPUT ###
pandoc --template="$viewdir/template.html" \
     -f markdown_github+yaml_metadata_block "$md"
