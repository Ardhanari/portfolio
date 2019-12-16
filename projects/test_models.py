from django.test import TestCase
from .models import Project
from datetime import datetime, timezone
from django.core.exceptions import ValidationError

class testProjectModel(TestCase):
    def test_fullname_cant_be_blank(self): 
        project = Project(name="")
        name = project.name
        self.assertRaises(ValidationError, name=name)

    def test_linkGit_can_be_empty(self):
        project = Project(name="Test Project", linkGit="", linkDepl="http:///", year=datetime.now)
        self.assertEqual(project.linkGit, '') 

    