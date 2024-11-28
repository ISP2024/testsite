## Description

This is a Django project that provides some URLs that return various status codes.  I wrote this because I could not find any *real* web pages that return 403 or 406 status codes.

## How to Install and Run

1. Requires Python and Django.
2. Run migrations:
   ```
   python manage.py migrate
   ```
3. Run it on port 8000.  This port is referenced in URLs on the testpage.html), so a different port won't work.
