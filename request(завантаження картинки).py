import requests
image = requests.get('https://cdn.imgbin.com/8/24/25/imgbin-gon-freecss-fan-art-hunter-hunter-gon-freecss-XPeJ4rzJ3dp7MnGyAmAWmZS8W.jpg')
with open('new_image1.jpg', 'wb') as f:
    f.write(image.content)