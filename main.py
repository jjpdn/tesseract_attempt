import os
import ocr_methods
from googletrans import Translator
from glob import glob

image_dir = os.path.join(".","images","*.*")
output_dir = os.path.join(".","output")

image_files = glob(image_dir)

translator = Translator()

for image_path in sorted(image_files):
    text = ocr_methods.parse_image(image_path)
    print("orig: \n", text)
    #text = text.replace("|","").replace("\\","").replace("/","").replace("}","")
    trans_text = translator.translate(text, src="ID")
    print("trans: \n", trans_text.text)

