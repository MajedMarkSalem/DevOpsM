#!/usr/bin/env bash

function SourceFunctions() {
    . "./functions.sh"
}

function main() {
    SourceFunctions
    CheckPrereqs
    Initialize
    SourceVariables "global"
    SourceVariables "${scriptName}"
    RunScripts
}

if [[ -z "$1" ]]; then
    echo -e "Argument \"environment\" missing, exiting script"
    exit 1
else
    environment="$1"
fi

if [[ "$*" == *--pipeline* ]]; then
    runMode="Pipeline"
else
    runMode="Interactive"
fi

main
