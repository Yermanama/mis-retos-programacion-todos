""" * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 * imagen de 1920*1080px."""

from fractions import Fraction
import requests
from PIL import Image
from io import BytesIO

response = requests.get('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')

response.raise_for_status()

imagen = Image.open(BytesIO(response.content))

width, height = imagen.size

aspect_ratio = Fraction(width/height).limit_denominator(10)

print(f'La ratio de la foto es {aspect_ratio}')

