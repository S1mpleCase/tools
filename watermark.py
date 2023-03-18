from PIL import Image, ImageDraw, ImageFont

# Load the image
img = Image.open("/Users/adam/Desktop/011.png")

# Create the watermark image
watermark_size = (120,50)
watermark = Image.new("RGBA", watermark_size, (255, 255, 255, 0))
draw = ImageDraw.Draw(watermark)
text = "仅供车险使用"
font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 20)
text_size = draw.textsize(text, font=font)
text_position = ((watermark.width - text_size[0]) // 2, (watermark.height - text_size[1]) // 2)
draw.text(text_position, text, font=font, fill=(0, 0, 0, 128))

# Rotate the watermark image
watermark = watermark.rotate(45, expand=True)

# Tile the watermark image across the entire image
tile_size = (img.width // watermark.width + 1, img.height // watermark.height + 1)
tile = Image.new("RGBA", (watermark.width * tile_size[0], watermark.height * tile_size[1]), (255, 255, 255, 0))
for y in range(tile_size[1]):
  for x in range(tile_size[0]):
    tile_position = (x * watermark.width, y * watermark.height)
    tile.alpha_composite(watermark, tile_position)

# Combine the tile and the original image
img.alpha_composite(tile)

# Save the watermarked image
img.save("/Users/adam/Desktop/011_watermarked.png")
