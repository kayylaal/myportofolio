from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput

from main.models import Project, SocialWork

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "link",
            "thumbnail",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "link": "URL Proyek",
            "thumbnail": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "link": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class SocialWorkForm(ModelForm):
    class Meta:
        model = SocialWork
        fields = [
            "title",
            "description",
            "photo",
            "year",
        ]

        labels = {
            "title": "Nama Social Work",
            "description": "Deskripsi Social Work",
            "photo": "URL Gambar Social Work",
            "year": "Tahun Social Work",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Summer Volunteer",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Social Work-mu",
                    "rows": 3,
                }
            ),
            "photo": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "year": NumberInput(
                attrs={
                    "placeholder": "2007",
                }
            ),
        }