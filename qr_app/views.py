import qrcode
import qrcode.image.svg
import pyshorteners
from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

from PIL import Image, ImageDraw, ImageFont
import os

def generate_qr(request):
    if request.method == 'POST':
        url = request.POST.get('url', '').strip()
        if not url:
            return JsonResponse({'error': 'URL is required'}, status=400)
            
        # Get custom filename or generate a default one
        filename = request.POST.get('filename', '').strip()
        if not filename:
            # Generate a default filename based on the URL
            from urllib.parse import urlparse
            parsed_url = urlparse(url)
            domain = parsed_url.netloc.replace('www.', '').split('.')[0] or 'qrcode'
            filename = f"{domain}-{hash(url) % 10000}"
        
        # Clean filename (remove extension if present)
        if filename.lower().endswith('.png'):
            filename = filename[:-4]
            
        try:
            # Generate QR code with higher error correction and larger size
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=13,  # Increased from 10 to ~30% larger
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            
            # Create QR code image with white background
            qr_img = qr.make_image(fill_color="black", back_color="white")
            
            # Convert to PIL Image if it's not already
            if not hasattr(qr_img, 'convert'):
                qr_img = qr_img.get_image()
            
            # Add more padding at the bottom for larger text and better spacing
            padding = 90  # Increased padding to ensure enough space
            img_width, img_height = qr_img.size
            new_img = Image.new('RGB', (img_width, img_height + padding), 'white')
            new_img.paste(qr_img, (0, 0))
            
            # Add text (filename) below the QR code
            draw = ImageDraw.Draw(new_img)
            try:
                # Try to use Arial Bold font with larger size, fallback to default
                font_path = "C:/Windows/Fonts/arialbd.ttf"  # Arial Bold
                if os.path.exists(font_path):
                    font = ImageFont.truetype(font_path, 22)  # Increased font size to 22
                else:
                    font = ImageFont.load_default()
            except Exception:
                font = ImageFont.load_default()
            
            # Calculate positions with better spacing
            text = filename[:30]  # Limit text length to prevent overflow
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            
            # Position the line and text with proper spacing
            line_y = img_height + 15  # Position line 15px below QR code
            text_y = line_y + 20  # Position text 20px below the line
            text_position = ((img_width - text_width) // 2, text_y)
            
            # Draw text with black color
            draw.text(text_position, text, fill="black", font=font)
            
            # Add a subtle line between QR code and text
            draw.line([(img_width * 0.15, line_y), (img_width * 0.85, line_y)], 
                     fill="#888888", width=2)  # Line is now properly spaced
            
            # Save the combined image to a buffer
            buffer = BytesIO()
            new_img.save(buffer, format="PNG")
            qr_code = buffer.getvalue()
            buffer.close()
            
            # Create response with content disposition header for download
            response = HttpResponse(qr_code, content_type='image/png')
            response['Content-Disposition'] = f'inline; filename="{filename}.png"'
            return response
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
        url = request.POST.get('url', '').strip()
        if not url:
            return JsonResponse({'error': 'URL is required'}, status=400)
            
        try:
            # Initialize the shortener
            shortener = pyshorteners.Shortener()
            
            # Shorten the URL using TinyURL service
            short_url = shortener.tinyurl.short(url)
            
            return JsonResponse({
                'original_url': url,
                'short_url': short_url
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
