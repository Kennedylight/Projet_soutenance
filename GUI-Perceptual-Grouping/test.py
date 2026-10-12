from GUI import GUI

gui = GUI(img_file="/public/images/img1.png", output_dir="data/output")
gui.detect_element(is_ocr=False, is_non_text=True, is_merge=True)