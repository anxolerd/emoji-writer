Emoji-writer
============

Transforms your text into emoji image. The primary usage is to throw short words
written in emoji to slack.

Usage
-----

.. code-block:: bash

    ./replacer.py 'Yay'  # use default emojis
    ./replacer.py 'Yay' --fg '👍' --bg '◼'

Notes
-----

Currently works only with latin alphabet. No numerics. No punctuation.
