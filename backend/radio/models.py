from django.db import models


class Song(models.Model):
    CATEGORY_CHOICES = [
        ("golden", "Golden Era"),
        ("80s", "80s"),
        ("90s", "90s"),
        ("2000s", "2000s"),
        ("bangla", "Bangla Classics"),
        ("hindi", "Old Hindi"),
        ("english", "Old English"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="other",
    )

    cover = models.ImageField(
        upload_to="covers/",
        blank=True,
        null=True,
    )

    audio_file = models.FileField(
        upload_to="music/",
    )

    duration = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Duration in seconds",
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} — {self.artist}"