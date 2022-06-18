from typing import Optional
from . import utils

def generate(
    image: utils.PotentialImage=None,
    text: str=None,
    font: Optional[utils.PotentialFont]=None,
    output: Optional[utils.PotentialPath]=None
):
    image = utils.get_image(image)
    
    # TODO
    
    return image
