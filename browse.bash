#!/usr/bin/env bash
img2ascii() {
    echo "<pre><span style=\"font-family:monospace;font-size:8px;letter-spacing:0;line-height:0.45;align:center;\">`python ~/code/img2ascii/img2ascii.py $@`</spn></pre>" | browser
}
