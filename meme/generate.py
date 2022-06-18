from typing import Optional
from . import utils

def generate_fitted_text(
    image: utils.PotentialImage=None,
    text: str=None,
    font: Optional[utils.PotentialFont]=None,
) -> utils.FittedText:
    image = utils.get_image(image)
    font = utils.get_font(font)
    
    return 'hello'

def generate(
    image: utils.PotentialImage=None,
    text: str=None,
    font: Optional[utils.PotentialFont]=None,
    output: Optional[utils.PotentialPath]=None
):
    image = utils.get_image(image)
    font = utils.get_font(font)
    fitted_text = generate_fitted_text(
        image=image,
        font=font,
        text=text
    )
    
    return fitted_text
