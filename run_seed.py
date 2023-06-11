import django
django.setup()

from about.seed import about_run
from skills.seed import skills_run
from services.seed import services_run
from contact.seed import contact_run
from testimonial.seed import testimonial_run
if __name__ == '__main__':
    # about_run()
    # skills_run()
    # services_run()
    # contact_run()
    testimonial_run()