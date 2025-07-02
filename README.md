# QR Code Generator & URL Shortener

A web application that allows users to generate QR codes for URLs and shorten long URLs. Built with Django and Python.

## Features

- **QR Code Generator**:
  - Generate QR codes from any URL
  - Download QR code as a PNG image
  - Clean, responsive interface

- **URL Shortener**:
  - Shorten long URLs using TinyURL service
  - Copy shortened URL to clipboard with one click
  - View original URL

## Screenshots

![QR Code Generator](screenshots/qr-generator.png)
![URL Shortener](screenshots/url-shortener.png)

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

## Running the Application

1. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

2. **Open your web browser** and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
qr-code-generator/
├── manage.py
├── requirements.txt
├── qr_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
└── qr_project/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Dependencies

- Django 5.0.3
- qrcode 7.4.2
- Pillow 10.2.0
- pyshorteners 1.0.1

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- QR Code generation using [qrcode](https://pypi.org/project/qrcode/)
- URL shortening using [pyshorteners](https://pypi.org/project/pyshorteners/)
