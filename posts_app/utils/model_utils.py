import os

from PIL import Image

from posts_app.posts_settings import ALLOWED_TEXT_FILE_EXTENSIONS, ALLOWED_IMAGE_EXTENSIONS


def attachment_file_path(instance, filename) -> str:
    name, extension = os.path.splitext(filename)
    filename = f"{name}{extension}"
    return os.path.join(f"uploads/{instance.owner.id}/attachments/", filename)


def process_image(image_path: str, max_width: int = 320, max_height: int = 240):
    with Image.open(image_path) as img:
        width, height = img.size

        if width > max_width or height > max_height:
            img.thumbnail((max_width, max_height))
            img.save(image_path)


def check_text_file_size(text_file_path: str, max_file_size: int = 100 * 1024):
    file_size = os.path.getsize(text_file_path)

    if file_size > max_file_size:
        raise ValueError("The size of the text file exceeds the maximum allowed size (100 KB).")


def check_attachment_extensions(
        file_path: str,
        allowed_extensions: tuple = None,
):
    _, extension = os.path.splitext(file_path)

    if not allowed_extensions:
        allowed_extensions = ALLOWED_TEXT_FILE_EXTENSIONS + ALLOWED_IMAGE_EXTENSIONS

    if extension not in allowed_extensions:
        raise ValueError("The file does not match an allowed extension.")
