from typing import Optional
from . import utils

def generate_fitted_text(
    image: utils.PotentialImage=None,
    text: str=None,
    font: Optional[utils.PotentialFont]=None,
    font_size: Optional[utils.FontSize]=None
) -> utils.FittedText:
    image = utils.get_image(image)
    font = utils.get_font(font)
    width, height = image.size
    
    if font_size is None:
        # generally, larger images should use a larger font size
        font_size = utils.get_font_size(
            max(8, min(256, width / 10, height / 5))
        )
    
    return utils.fit_text(
        text=text,
        font=font,
        bounds=utils.Rectangle(0, 0, width, float('inf')),
        font_size=font_size
    )

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
