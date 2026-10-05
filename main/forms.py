from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

# form kegiatan sosial, year pakai NumberInput
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
    # bersihin tag html biar aman dari xss
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama social work tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()