from django.db import models


class Rating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=Rating.choices,
        default=Rating.G,
        null=True,
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )

    def __repr__(self) -> str:
        return f"<Movie ({self.id} - {self.title})>"
