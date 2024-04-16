import os
import streamlit as st
from tempfile import NamedTemporaryFile
from PIL import Image

import pytesseract_letter
import pytesseract_word
import easyocr_letter
import easyocr_word


def main():
    st.title(":red[OCR Handwriting Comparison]")
    st.sidebar.header("OCR Algorithm")
    with st.sidebar.expander("Instructions"):
        st.write("1. Select OCR Algorithm")
        st.write("2. Select comparison mode")
        st.write("3. Upload two images")
        st.write("4. Click the button to create a juxtaposed collage")
    options = st.sidebar.selectbox("Select the OCR Algorithm",
                                   ["Pytesseract", "EasyOCR"])

    if options == "Pytesseract":
        st.header("Pytesseract Algorithm")

        mode = st.radio("Select comparison mode",
                        ["letters", "words"])

        if mode == "letters":

            image_extensions = ["png", "jpg", "jpeg", "webp"]

            image_path_1 = st.file_uploader("Upload image 1", type=image_extensions)
            if image_path_1:
                show_image = st.checkbox("Show image 1", key="checkbox_1")
                if show_image:
                    st.image(image_path_1, use_column_width=True)
                with NamedTemporaryFile(delete=False) as temp_file_1:
                    temp_file_1.write(image_path_1.getvalue())
                    file_path_1 = temp_file_1.name

            image_path_2 = st.file_uploader("Upload image 2", type=image_extensions)
            if image_path_2:
                show_image = st.checkbox("Show image 2", key="checkbox_2")
                if show_image:
                    st.image(image_path_2, use_column_width=True)
                with NamedTemporaryFile(delete=False) as temp_file_2:
                    temp_file_2.write(image_path_2.getvalue())
                    file_path_2 = temp_file_2.name

            if image_path_1 and image_path_2:
                st.write("")
                if st.button("Create juxtaposed letter collage"):
                    image_data_1 = pytesseract_letter.extract_text_and_boxes(file_path_1)
                    image_data_2 = pytesseract_letter.extract_text_and_boxes(file_path_2)
                    pytesseract_letter.create_juxtaposed_collage(
                        image_data_1, image_data_2, file_path_1, file_path_2)
                    st.success("Juxtaposed letter collage created successfully!")

                    # Show juxtaposed collage image
                    collage_image = "juxtaposed_letter_collage_final.png"
                    if collage_image:
                        st.image(collage_image, use_column_width=True)

                    # Delete temporary files after we're done with them! (very necessary)
                    os.unlink(file_path_1)
                    os.unlink(file_path_2)

        if mode == "words":

            image_extensions = ["png", "jpg", "jpeg", "webp"]

            image_path_1 = st.file_uploader("Upload image 1", type=image_extensions)
            if image_path_1:
                show_image = st.checkbox("Show image 1", key="checkbox_1")
                if show_image:
                    st.image(image_path_1, use_column_width=True)
                with NamedTemporaryFile(delete=False) as temp_file_1:
                    temp_file_1.write(image_path_1.getvalue())
                    file_path_1 = temp_file_1.name

            image_path_2 = st.file_uploader("Upload image 2", type=image_extensions)
            if image_path_2:
                show_image = st.checkbox("Show image 2", key="checkbox_2")
                if show_image:
                    st.image(image_path_2, use_column_width=True)
                with NamedTemporaryFile(delete=False) as temp_file_2:
                    temp_file_2.write(image_path_2.getvalue())
                    file_path_2 = temp_file_2.name

            if image_path_1 and image_path_2:
                st.write("")
                if st.button("Create juxtaposed word collage"):
                    image_data_1 = pytesseract_word.extract_text_and_boxes(file_path_1)
                    image_data_2 = pytesseract_word.extract_text_and_boxes(file_path_2)
                    pytesseract_word.create_juxtaposed_collage(
                        image_data_1, image_data_2, file_path_1, file_path_2)
                    st.success("Juxtaposed word collage created successfully!")

                    # Show juxtaposed collage image
                    collage_image = "juxtaposed_word_collage_final.png"
                    if collage_image:
                        st.image(collage_image, use_column_width=True)

                    # Delete temporary files after we're done with them! (very necessary)
                    os.unlink(file_path_1)
                    os.unlink(file_path_2)

    if options == "EasyOCR":
        st.header("EasyOCR Algorithm")

        mode = st.radio("Select comparison mode",
                        ["letters", "words"])

        if mode == "letters":

            image_extensions = ["png", "jpg", "jpeg", "webp"]

            image_path_1 = st.file_uploader("Upload image 1", type=image_extensions)
            if image_path_1:
                show_image = st.checkbox("Show image 1", key="checkbox_1")
                if show_image:
                    st.image(image_path_1, use_column_width=True)
                with NamedTemporaryFile(delete=False) as temp_file_1:
                    temp_file_1.write(image_path_1.getvalue())
                    file_path_1 = temp_file_1.name

            image_path_2 = st.file_uploader("Upload image 2", type=image_extensions)
            if image_path_2:
                show_image = st.checkbox("Show image 2", key="checkbox_2")
                if show_image:
                    st.image(image_path_2, use_column_width=True)
                with NamedTemporaryFile(delete=False) as temp_file_2:
                    temp_file_2.write(image_path_2.getvalue())
                    file_path_2 = temp_file_2.name

            if image_path_1 and image_path_2:
                st.write("")
                if st.button("Create juxtaposed letter collage"):
                    image_data_1 = easyocr_letter.extract_text_and_boxes(file_path_1)
                    image_data_2 = easyocr_letter.extract_text_and_boxes(file_path_2)
                    easyocr_letter.create_juxtaposed_collage(
                        image_data_1, image_data_2, file_path_1, file_path_2)
                    st.success("Juxtaposed letter collage created successfully!")

                    # Show juxtaposed collage image
                    collage_image = "juxtaposed_letter_collage_final.png"
                    if collage_image:
                        st.image(collage_image, use_column_width=True)

                    # Delete temporary files after we're done with them! (very necessary)
                    os.unlink(file_path_1)
                    os.unlink(file_path_2)

        if mode == "words":

            image_extensions = ["png", "jpg", "jpeg", "webp"]

            image_path_1 = st.file_uploader("Upload image 1", type=image_extensions)
            if image_path_1:
                show_image = st.checkbox("Show image 1", key="checkbox_1")
                if show_image:
                    st.image(image_path_1, use_column_width=True)
                with NamedTemporaryFile(delete=False) as temp_file_1:
                    temp_file_1.write(image_path_1.getvalue())
                    file_path_1 = temp_file_1.name

            image_path_2 = st.file_uploader("Upload image 2", type=image_extensions)
            if image_path_2:
                show_image = st.checkbox("Show image 2", key="checkbox_2")
                if show_image:
                    st.image(image_path_2, use_column_width=True)
                with NamedTemporaryFile(delete=False) as temp_file_2:
                    temp_file_2.write(image_path_2.getvalue())
                    file_path_2 = temp_file_2.name

            if image_path_1 and image_path_2:
                st.write("")
                if st.button("Create juxtaposed word collage"):
                    image_data_1 = easyocr_word.extract_text_and_boxes(file_path_1)
                    image_data_2 = easyocr_word.extract_text_and_boxes(file_path_2)
                    easyocr_word.create_juxtaposed_collage(
                        image_data_1, image_data_2, file_path_1, file_path_2)
                    st.success("Juxtaposed word collage created successfully!")

                    # Show juxtaposed collage image
                    collage_image = "juxtaposed_word_collage_final.png"
                    if collage_image:
                        st.image(collage_image, use_column_width=True)

                    # Delete temporary files after we're done with them! (very necessary)
                    os.unlink(file_path_1)
                    os.unlink(file_path_2)


if __name__ == "__main__":
    main()
