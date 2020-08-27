#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#https://www.youtube.com/watch?v=zo3p6cZaZtM&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=12
#https://www.youtube.com/watch?v=o4SbgPEff7o&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=21
#https://www.youtube.com/watch?v=h47Wx5118ng&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=24
#https://www.youtube.com/watch?v=N3VWvPqWnwc&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=26