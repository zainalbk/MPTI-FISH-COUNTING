"""
Generate dummy images for SiBibit application
Run this script once: python generate_dummy_images.py
"""

try:
    from PIL import Image, ImageDraw
    
    # Logo SiBibit (ikan)
    img = Image.new('RGBA', (200, 200), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([40, 60, 140, 140], outline=(116, 29, 255), width=6)
    draw.polygon([(140, 100), (180, 70), (180, 130)], outline=(116, 29, 255), width=6)
    draw.ellipse([120, 85, 130, 95], fill=(116, 29, 255))
    img.save('assets/images/logo_sibibit.png')
    
    # Icon kamera
    img = Image.new('RGBA', (64, 64), (185, 149, 234, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse([12, 12, 52, 52], outline=(255, 255, 255), width=3)
    img.save('assets/images/icon_camera.png')
    
    # Thumbnail ikan Nila
    img = Image.new('RGB', (80, 60), (200, 200, 200))
    draw = ImageDraw.Draw(img)
    draw.ellipse([10, 15, 50, 45], fill=(100, 150, 200))
    draw.polygon([(50, 30), (70, 20), (70, 40)], fill=(100, 150, 200))
    img.save('assets/images/fish_nila.png')
    
    # Thumbnail ikan Lele
    img = Image.new('RGB', (80, 60), (200, 200, 200))
    draw = ImageDraw.Draw(img)
    draw.ellipse([10, 20, 55, 40], fill=(80, 80, 80))
    draw.polygon([(55, 30), (75, 22), (75, 38)], fill=(80, 80, 80))
    img.save('assets/images/fish_lele.png')
    
    # Thumbnail ikan Mujair
    img = Image.new('RGB', (80, 60), (200, 200, 200))
    draw = ImageDraw.Draw(img)
    draw.ellipse([10, 15, 50, 45], fill=(150, 180, 100))
    draw.polygon([(50, 30), (70, 20), (70, 40)], fill=(150, 180, 100))
    img.save('assets/images/fish_mujair.png')
    
    # Thumbnail ikan Kapal Laut
    img = Image.new('RGB', (80, 60), (200, 200, 200))
    draw = ImageDraw.Draw(img)
    draw.ellipse([10, 15, 50, 45], fill=(255, 150, 100))
    draw.polygon([(50, 30), (70, 20), (70, 40)], fill=(255, 150, 100))
    img.save('assets/images/fish_kapal.png')
    
    # Video thumbnail
    img = Image.new('RGB', (400, 240), (35, 49, 66))
    draw = ImageDraw.Draw(img)
    draw.polygon([(180, 100), (240, 120), (180, 140)], fill=(255, 255, 255))
    img.save('assets/images/video_preview.png')
    
    print("✓ Dummy images created successfully in assets/images/")
    
except ImportError:
    print("PIL/Pillow not installed. Install with: pip install Pillow")
    print("Or manually place images in assets/images/ folder")
