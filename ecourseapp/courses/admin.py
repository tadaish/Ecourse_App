from django.contrib import admin
from courses.models import Category, Course
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import cloudinary


# Register your models here.
class CourseForm(forms.Form):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'created_date', 'updated_date', 'active']
    list_display_links = ['name']
    search_fields = ['id', 'name']
    list_filter = ['id', 'name', 'created_date']
    readonly_fields = ['my_image']

    def my_image(self, course):
        if course.image:
            if type(course.image) is cloudinary.CloudinaryResource:
                return mark_safe(f"<img width='300' src='{course.image.url}' />")
            return mark_safe(f"<img width='300' src='/static/{course.image.name}' />")


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)