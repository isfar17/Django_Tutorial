delete:


In [27]: target=People.objects.filter(name="David Thompson")

In [28]: target
Out[28]: <QuerySet [David Thompson - 45 - 1999-09-17]>

In [29]: target.delete()
Out[29]: (1, {'my_app.People': 1})

update:
In [31]: People.objects.get(name="Donna Nielsen")
Out[31]: Donna Nielsen - 33 - 1971-08-03

update:


In [32]: target=People.objects.get(name="Donna Nielsen")

In [33]: target.name
Out[33]: 'Donna Nielsen'

In [35]: target.name="Jubayer Isfar"

In [36]: target.save()

In [37]: target
Out[37]: Jubayer Isfar - 33 - 1971-08-03

In [38]: