#!/bin/bash
S="$1"; cd "$S/run"
run(){ id="$1"; [ -s "$S/out/$id.txt" ] && return; timeout 900 claude -p --model opus --tools "" --strict-mcp-config --system-prompt "You are a careful reviewer of technical writing." < "$S/prompts/$id.txt" > "$S/out/$id.txt" 2> "$S/out/$id.err"; }
export -f run; export S
ls "$S/prompts" | sed 's/\.txt$//' | xargs -P 6 -I{} bash -c 'run {}'
echo done; ls "$S/out"/*.txt | wc -l; wc -w "$S/out"/*.txt | tail -1
