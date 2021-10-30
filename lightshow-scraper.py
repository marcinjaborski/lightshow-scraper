from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import base64


def generate_link():
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(6))


def get_images_from_lightshow(wd, no_images):
    images_saved = 0
    while images_saved < no_images:
        url = generate_link()
        wd.get("https://prnt.sc/" + url)
        try:
            allow_cookies = wd.find_element(By.CLASS_NAME, "css-47sehv")
            allow_cookies.click()
        except Exception:
            pass
        try:
            image = wd.find_element(By.CLASS_NAME, "under-image").find_element(By.TAG_NAME, 'img')
            image_base64_text = image.get_attribute("src")
            image_base64_text = image_base64_text[image_base64_text.index(',') + 1:]
            save_image(image_base64_text, f"{url}.jpg")
            images_saved += 1
        except Exception:
            print(f"Could not get base64 representation from {url}")


def save_image(image_base64, file_name):
    with open(f"imgs/{file_name}", "wb") as f:
        f.write(base64.decodebytes(bytes(image_base64, 'utf-8)')))


if __name__ == "__main__":
    PATH = "C:\\Users\\Marcin\\PycharmProjects\\lightshow-scraper\\chromedriver.exe"
    wdriver = webdriver.Chrome(PATH)
    get_images_from_lightshow(wdriver, 10)
    # get_images_from_lighshow(wdriver, math.inf)
    wdriver.quit()
