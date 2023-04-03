# https://pillow.readthedocs.io/en/stable/index.html
# https://realpython.com/image-processing-with-the-python-pillow-library/
# pip install Pillow

from PIL import Image, ImageFilter  # 라이브러리를 임포트 한다.

original = Image.open("gogh.png") # 하드 드라이브에서 이미지를 읽어 들인다.
print(original.mode)
blurred = original.filter(ImageFilter.BLUR) # 이미지를 흐리게, 경계선 검출 CONTOUR
blurred.save("gogh_blurred.png")

gray_img = original.convert("L")
gray_img.save("gogh_gray.png")

# original.show() # 두 이미지를 디스플레이 한다.
# blurred.show()
