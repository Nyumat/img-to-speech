# Nyumat 3/24/2020
from PIL import Image
from pytesseract import image_to_string
from gtts import gTTS

""" Code Snippets from documentation for reference

Image to text one liner

tex = image_to_string(Image.open('MYPATH'))

print(tex)

Output: "IMAGE"

Image to speech one liner

gTTS('coding is coding.').save('sound.mp3')

Output: a new file in the directory called 'sound.mp3' that says "Image"

"""

def image_to_sound(PATH):
      try:  # First need to convert the image to text.
      # We will be using Pillow to load the image and pytesseract to convert it into a string
            render_image = Image.open(PATH)
            decoded_text = image_to_string(render_image)
            purge_text = ' '.join(decoded_text.split('\n'))
            print(f"Given image in text form is: {purge_text}.") 
            audio_french = gTTS(purge_text, lang='en') # Then the Google Text-to-Speech module (gTTS) to create/save the .mp3.          
            audio_french.save('french.mp3')
            return True
      except Exception as thrownError:
            print(">> Error thrown while executing. '\n'", thrownError)
            return
# Now I called the function with the path to the image as an argument
image_to_sound('image2.jpg')
input()