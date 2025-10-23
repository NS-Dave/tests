#!/bin/bash
# File backup script example
# Creates a backup of a file with timestamp

backup_file() {
    local source_file="$1"
    
    if [ ! -f "$source_file" ]; then
        echo "Error: File '$source_file' not found"
        return 1
    fi
    
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local backup_name="${source_file}.backup_${timestamp}"
    
    cp "$source_file" "$backup_name"
    echo "Backup created: $backup_name"
}

main() {
    echo "File Backup Script Example"
    echo "Usage: $0 <filename>"
    echo ""
    echo "This script would create a timestamped backup of the specified file"
}

# Uncomment to use with a file argument
# if [ $# -eq 0 ]; then
#     main
# else
#     backup_file "$1"
# fi

main "$@"
