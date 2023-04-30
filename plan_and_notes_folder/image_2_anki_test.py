import os
import genanki
import cv2
from detectLastMove import detect_circles


my_model = genanki.Model(
    24623724,
    'Test Model',
    fields=[

        {'name': 'ImageFront'},
        {'name': 'ImageBack'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{ImageFront}}', # 'qfmt' stands for question format, don't change this
            'afmt': '{{ImageFront}}''{{ImageBack}}',
        },
    ],
    css="""
        img {
            max-width: 100%;
            max-height: 100%;
        }
        """
)

my_deck = genanki.Deck(
    5683562,
    'Eric 2-23-2023')  # this is the name of the deck that you see on Anki

path_to_folder = r"C:\Users\nharw\Desktop\Extra folder of puzzles"
sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

my_package = genanki.Package(my_deck)
my_package.media_files = []  # need to add all image sources to this media files list

for image in sorted_images:           # see if these two lines properly appends the images into the media_files list

    full_file_path = os.path.join(path_to_folder, image)
    my_package.media_files.append(full_file_path)

# print(my_package.media_files)

    final_image = cv2.imread(full_file_path)

    # 2 lines below work
    if detect_circles(final_image):  # if detect_circles function returns true, then
        print("Add image to front of card", full_file_path)

        front_image = image

        my_note = genanki.Note(
            model=my_model,
            fields=[f'<img src="{front_image}"/>', '<img src="">'])   #  , '<img src="back_image"/>' '<img src="back_image"/>'

    # else:
    #     back_image = image

        my_deck.add_note(my_note)

        my_package.write_to_file(r'C:\Users\nharw\PycharmProjects\images2Anki\anki_output\test1.apkg')

