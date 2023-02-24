'''

Step 1. Sort folder to be in order from smaller number in name to the largest number in name, I should already have
code for this from the other project. This way everything will be in order.

Step 2. Logic: For image in folder: if circle detected (returns boolean of true) then add that to the front of an anki
card.  For each image after that in the folder, add that to the back of the anki card until the next
circle is detected.

LOGIC:

for image in folder:
    if circle == true:
        1. create a new anki card
        2. add that single image (puzzle) to the front of the anki card
            2a. use image reference and add that reference to the anki "media files" path list
    else:
        1. add the image (answer) to the back of that newly created anki card
        2. add a space after each image (using CSS?)

Step 3. If above logic doesn't work, will need to save these as image numbers separately first, then add them
to the front and back of anki cards based on the puzzle and answer number



'''