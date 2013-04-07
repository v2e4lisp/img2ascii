#!/usr/bin/env bash
img2ascii() {
    echo "<pre><span style=\"font-size:0.1em;letter-spacing:0;line-height:0.45;\">`python ~/code/img2ascii/img2ascii.py $@`</spn></pre>" | browser
}
