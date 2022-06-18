import meme

output = meme.generate(
    image='static/nerd.jpg',
    text='test',
    output='output/meme.jpg'
)

print(output)
