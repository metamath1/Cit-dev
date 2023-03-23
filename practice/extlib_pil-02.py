from PIL import Image, ImageFilter  # 라이브러리를 임포트 한다.
import argparse

######################################################################
# https://docs.python.org/ko/3/library/argparse.html
# 이 부분은 파이썬 파일을 실행할 때 옵션을 받을 수 있도록 하는 부분입니다.
# 현재 만들고 싶은 프로그램은 다음처럼 동작하게 하고 싶습니다.
#
# extlib_pil-02.py gogh.png -a b : gogh.png를 흐림화시켜 gogh_blur.png로 저장
# extlib_pil-02.py gogh.png -a g : gogh.png를 흑배화시켜 gogh_gray.png로 저장
#
# 이렇게 하기 위해서는 extlib_pil-02.py 뒤에 입력이미지 파일을 적을 수 있어야 하고
# 흐림화할지 흑백하 할지 결정할 수 있는 옵션 -ab, -ag 를 줄수 있어야 합니다.
# 꽤 복잡한 작업이지만 내부 라이브러리 argparser를 쓰면 비교적 간단하게
# 처리할 수 있습니다.
# 이정도로 이해하고 아래 코드는 그대로 두고 진행합니다.
parser = argparse.ArgumentParser(description='my first pillow app.')
parser.add_argument('image')
parser.add_argument('-a', '--action', choices=['b', 'g'], 
                    default='b', help='b: blur, g: grayscale')
args = parser.parse_args()
######################################################################


def blur(filename):
    # 여기 입력받은 이미지 파일을 블러 시켜 *_blur.png로 저장
    print('blur')
    

def gray(filename):
    # 여기 입력받은 이미지 파일을 흑백화 시켜 *_gray.png로 저장
    print('gray')
    
if __name__ == '__main__':
    # argparser는 다음처럼 커맨트 라인에 옵션으로 준 값을 저장합니다.
    # 입력된 이미지 파일이름: args.image
    # 입력된 처리 옵션: args.action
    if args.action == 'b':
        blur(args.image)
    else:
        gray(args.image)