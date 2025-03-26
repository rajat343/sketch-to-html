import sys
import os
from argparse import ArgumentParser
from os.path import basename
import urllib
from PIL import Image


from groups.Plr import *

def arguements():
  parser = ArgumentParser()
  parser.add_argument('--png_path',dest='png_path', help='png_path to generate the code')
  parser.add_argument('--output_folder', dest='output_path',required=True)
  parser.add_argument('--model_json_file', dest='json_file',required=True)
  parser.add_argument('--model_weights_file', dest='weights_file',required=True)
  parser.add_argument('--style',dest='style',default='default')
  parser.add_argument('--verbose',dest='verbose', default=1)

  return parser



print("Do you want to Take 1.PhoneCameraPic\t2.Input Pic Manually ")
choice=input()
parser = arguements()
values= parser.parse_args()
if choice==1:
	urllib.urlretrieve("http://192.168.43.76:8080/shot.jpg","./index.jpg")
	Image.open("./index.jpg").save("./index.png")
	png_path="./index.png"
else:
		
	
	png_path = values.png_path
print(png_path)
	
output_path = values.output_path
style=values.style
json_file = values.json_file
weights_file = values.weights_file
verbose = values.verbose
if not os.path.exists(output_path):
	os.makedirs(output_path)
plr = Plr(json_path=json_file,weights_path = weights_file)
plr.convert_image(output_path, png_path=png_path, verbose=verbose, style=style)
