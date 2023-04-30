import os
import genanki
import cv2
from detectLastMove import detect_circles

my_model = genanki.Model(
    345670,
    'Test Model',
    fields=[

        {'name': 'ImageFront'},
        {'name': 'ImageBack'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{ImageFront}}', # 'qfmt' stands for question format, don't change this
            'afmt': '{{ImageFront}}<hr id="answer"><br>{{ImageBack}}',  # hr id="answer" -> auto jump to answer
        },
    ],
      css = """
           .card {
              font-family: arial;
              font-size: 20px;
              text-align: center;
              color: black;
              background-color: white;
            }
          """
    # Original CSS that was likely distorting the images

    # css="""
    #     img {
    #         max-width: 100%;
    #         max-height: 100%;
    #     }
    #     """
)

my_deck = genanki.Deck(
    34689744,
    'Eric situation image2anki puzzles')  # this is the name of the deck that you see on Anki

#path_to_folder = r"C:\Users\nharw\Desktop\Extra folder of puzzles"
path_to_folder = r"C:\Users\nharw\Desktop\Screenshot Project\Stored Screenshots"

if os.path.exists(os.path.join(path_to_folder, 'desktop.ini')):
    os.remove(os.path.join(path_to_folder, 'desktop.ini'))
    print("desktop.ini removed")

sorted_images = os.listdir(path_to_folder)
sorted_images.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

my_package = genanki.Package(my_deck)
my_package.media_files = []  # need to add all image sources to this media files list

front_image = None
back_images = []

for image in sorted_images:

    full_file_path = os.path.join(path_to_folder, image)
    my_package.media_files.append(full_file_path)

    final_image = cv2.imread(full_file_path)

    if detect_circles(final_image):
        print("Add image to front of card", full_file_path)

        if front_image is not None:
            # create a note for the previous card with answer images on the back
            back_image_tags = ''.join([f'<img src="{b}"/>' for b in back_images])
            my_note = genanki.Note(
                model=my_model,
                fields=[f'<img src="{front_image}"/>', back_image_tags])
            my_deck.add_note(my_note)

            # clear the back_images list
            back_images = []

        # update the front image for the current card
        front_image = image
    else:
        # add the current image to the back images list
        back_images.append(image)

# create a note for the last card with answer images on the back (if any)
if front_image is not None and len(back_images) > 0:
    back_image_tags = ''.join([f'<img src="{b}"/>' for b in back_images])
    my_note = genanki.Note(
        model=my_model,
        fields=[f'<img src="{front_image}"/>', back_image_tags])
    my_deck.add_note(my_note)

my_package.write_to_file(r'C:\Users\nharw\PycharmProjects\images2Anki\anki_output\4-25-23-deck.apkg')
