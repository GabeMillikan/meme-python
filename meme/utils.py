# Pillow imports
import PIL.Image, PIL.ImageDraw, PIL.ImageFont
from PIL.Image import Image as PillowImage
from PIL.ImageFont import ImageFont as PillowImageFont

# other imports
import textwrap
import pathlib
from dataclasses import dataclass, field
from typing import Optional, Iterable

# common type aliases
Number = int | float

# classes
@dataclass
class Point:
    x: Number
    y: Number

@dataclass
class Range:
    min: Number
    max: Number
    
    def __init__(self, min: Number=None, max: Number=None):
        if min > max:
            min, max = max, min
        
        self.min, self.max = min, max
    
    def __in__(self, x: Number):
        return self.min <= x <= self.max

@dataclass
class Rectangle:
    x: Number
    y: Number
    width: Number
    height: Number
    
    x1: Number = field(repr=False)
    y1: Number = field(repr=False)
    x2: Number = field(repr=False)
    y2: Number = field(repr=False)
    
    left: Number = field(repr=False)
    right: Number = field(repr=False)
    top: Number = field(repr=False)
    bottom: Number = field(repr=False)
    
    top_left: Number = field(repr=False)
    tl: Number = field(repr=False)
    
    top_right: Number = field(repr=False)
    tr: Number = field(repr=False)
    
    bottom_right: Number = field(repr=False)
    br: Number = field(repr=False)
    
    bottom_left: Number = field(repr=False)
    bl: Number = field(repr=False)
    
    def __init__(self, x: Number=None, y: Number=None, width: Number=None, height: Number=None):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.x1, self.y1, self.x2, self.y2 = self.x, self.y, self.x + self.width, self.y + self.height
        
        self.top, self.right, self.bottom, self.left = self.y1, self.x2, self.y2, self.x1
        self.top_left = self.tl = Point(self.left, self.top)
        self.top_right = self.tr = Point(self.right, self.top)
        self.bottom_right = self.br = Point(self.right, self.bottom)
        self.bottom_left = self.bl = Point(self.left, self.bottom)
        
        self.area = self.width * self.height
    
    @classmethod
    def contain(cls, rectangles: Iterable['Rectangle']):
        '''
        Builds the smallest Rectangle that contains all of the provided rectangles.
        '''
        assert len(rectangles) > 0, 'You must provide at least one rectangle.'
        
        inf = float('inf')
        top, right, bottom, left = -inf, -inf, inf, inf
        
        for rectangle in rectangles:
            top = max(top, rectangle.top)
            right = max(right, rectangle.right)
            bottom = min(bottom, rectangle.bottom)
            left = min(left, rectangle.left)
        
        return cls(
            x=left,
            y=bottom,
            width=right - left,
            height=top - bottom
        )

@dataclass
class FittedLine:
    text: str
    bounds: Rectangle

@dataclass
class FittedText:
    font_size: int
    lines: list[FittedLine]
    bounds: Rectangle

# other type aliases
PotentialPath = pathlib.Path | str
PotentialImage = PillowImage | PotentialPath
PotentialFont = PillowImageFont | PotentialPath
MemeCaption = str | FittedText

def get_image(image: PotentialImage) -> PillowImage:
    '''
    If `image` is already a Pillow image, returns it unchanged.
    Otherwise, assumes that `image` represents a file path and
    `Image.open()`s it.
    '''
    if isinstance(image, PillowImage):
        return image
    else:
        return PIL.Image.open(image)

def get_font(font: PotentialFont) -> PillowImageFont:
    '''
    If `font` is already a Pillow image font, returns it unchanged.
    Otherwise, assumes that `font` represents a file path and
    `ImageFont.open()`s it.
    '''
    if isinstance(font, PillowImageFont):
        return font
    else:
        return PIL.ImageFont.open(font)

def fit_text(
    text: str=None, # What text should be fitted?
    font: PillowImageFont=None, # What font will be used to render the text?
    bounds: Rectangle=None, # the resultant fitted text will fit within this rectangle
    horizontal_center: bool=True, # horizontally center each line?
    vertical_center: bool=False, # vertically center the entire text block within the bounds?
    font_size: Optional[float | Range]=None, # (optional) if provided, then the font_size will be constrained to this
    line_height: float=0.5 # how much extra space should be added between each line, as a multiplier of the font size
) -> FittedText:
    '''
    Determines the best FittedText attributes for text to fit within the provided `bounds`.
    '''
    raise NotImplementedError('TODO')
