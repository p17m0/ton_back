from django.db import models


class Competition(models.Model):
    """
    Комната конкурса.
    """
    name = models.CharField(
        'Название комнаты',
        max_length=200,
    )

    currency = models.CharField(
        'Аббревиатура валюты',
        max_length=3
    )

    type_of_competition = models.CharField(
        'Тип розыгрыша',
        max_length=5,
        choices=[
            ("БИНГО", "Бинго"),
            ("ЛОТО", "Лото")
        ])

    amount_of_members = models.PositiveIntegerField(
        'Количество участников'
    )

    date = models.DateField(
        'Дата розыгрыша')

    time = models.TimeField(
        'Время розыгрыша'
    )

    win = models.CharField(
        'Выигрыш',
        max_length=200
    )

    royalty = models.PositiveIntegerField(
        'Роялти'
    )

    competition_ticket_size = models.ForeignKey(
        'TicketSize',
        on_delete=models.CASCADE,
        verbose_name='Размер билета лотереи'
    )

    # tickets = models.ManyToManyField(
    #     'Ticket',
    # )

    # winners_tickets = models.ManyToManyField(
    #     'Winner',
    # )

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return self.name


class TicketSize(models.Model):
    """
    Размер билета по строкам и столбцам.
    """
    raws = models.PositiveIntegerField()
    columns = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Размер билета'
        verbose_name_plural = 'Размеры билетов'

    # def __str__(self):
    #     return self.сompetitions.name


class Ticket(models.Model):
    """
    Билет.
    """
    combination = models.CharField(
        'Комбинация',
        max_length=200
    )
    ticket_size = models.ForeignKey(
        TicketSize,
        on_delete=models.CASCADE,
        verbose_name='Размер билета'
    )
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'



class Winner(models.Model):
    """
    Местo, которое может выиграть.
    """
    win = models.PositiveIntegerField() # размер выигрыша
    place = models.PositiveIntegerField() # выигрышное место
    # competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    win_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Победитель'
        verbose_name_plural = 'Победители'
