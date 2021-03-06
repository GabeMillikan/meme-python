# meme-python
 
Lets you easily generate text-based memes on images or gifs.
```py
import meme

output = meme.generate(
    image='nerd.png',
    text='POV: You don\'t use meme-python'
)

output.show()
```
![example](examples/output/meme.png)

## Setup
1. `pip install meme-python`
    - *Attention Windows users:* Most python installations use the `py` version manager, so pip is accessed like `py -m pip install meme-python`
    - *Attention Linux/MacOS users:* Most computers default to using Python version 2.x, you will need to speficially use Python 3.x like `pip3 -m pip install meme-python`
2. That's it! You're ready to go! Just `import meme` and follow one of the [examples](https://github.com/GabeMillikan/meme-python/blob/main/examples/simple.py).

## Development Setup
If you just want to use the library, then this step is unnecessary! Just use the steps listed above in the **Setup** section.
1. Clone this repository (or download it as a .zip package)
2. `pip install -r requirements.txt`
    - *Attention Windows users:* Most python installations use the `py` version manager, so pip is accessed like `py -m pip install -r requirements.txt`
    - *Attention Linux/MacOS users:* Most computers default to using Python version 2.x, you will need to speficially use Python 3.x like `pip3 -m pip install -r requirements.txt`

## Docs
TODO
