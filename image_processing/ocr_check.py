from paddleocr import PaddleOCR

img_path = "test_capture.png"  # or your test image
ocr = PaddleOCR(use_angle_cls=True, lang="en")
result = ocr.predict(img_path)

print("blocks:", len(result))
for bi, block in enumerate(result):
    print(f"block {bi} lines:", len(block))
    for line in block:
        text, conf = line[1][0], float(line[1][1])
        print(f"{conf:.3f}  {text}")
