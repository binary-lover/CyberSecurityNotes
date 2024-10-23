#!/bin/bash

# Loop through rotation values from 0 to 26
for rotate in {0..26}; do
    echo "Rotation: $rotate"
    
    while IFS= read -r line; do
        for ((i = 0; i < ${#line}; i++)); do
            char=${line:$i:1}
            if [[ $char =~ [a-z] ]]; then
                # Rotate lowercase letters
                printf "\\$(printf '%03o' $((($(printf '%d' "'$char") - 97 + rotate) % 26 + 97)))"
            elif [[ $char =~ [A-Z] ]]; then
                # Rotate uppercase letters
                printf "\\$(printf '%03o' $((($(printf '%d' "'$char") - 65 + rotate) % 26 + 65)))"
            else
                # Non-alphabetical characters remain the same
                printf "%s" "$char"
            fi
        done
        echo
    done < encrypted.txt

    echo "------------------------"
done

