default datefield formats:
```
[
    "%Y-%m-%d",  # '2006-10-25'
    "%m/%d/%Y",  # '10/25/2006'
    "%m/%d/%y",  # '10/25/06'
    "%b %d %Y",  # 'Oct 25 2006'
    "%b %d, %Y",  # 'Oct 25, 2006'
    "%d %b %Y",  # '25 Oct 2006'
    "%d %b, %Y",  # '25 Oct, 2006'
    "%B %d %Y",  # 'October 25 2006'
    "%B %d, %Y",  # 'October 25, 2006'
    "%d %B %Y",  # '25 October 2006'
    "%d %B, %Y",  # '25 October, 2006'
]
```

default datetime formats:
```
'2006-10-25 14:30:59'
'2006-10-25T14:30:59'
'2006-10-25 14:30'
'2006-10-25T14:30'
'2006-10-25T14:30Z'
'2006-10-25T14:30+02:00'
'2006-10-25'

```

How to detect perfect age for any user:

from datetime  import datetime
current_date_year=datetime.now().year
>>> year
age=current_date_year-birthdate_year
>>> age


query:
In [40]: People.objects.filter(name__icontains="san") #insenstive containts, means caps or lower does not matter
Out[40]: <QuerySet [<People: People object (7)>, <People: People object (47)>]>
In [53]: People.objects.filter(birthdate__lte="1974-2-20") #less than equal to
Out[53]: <QuerySet [<People: People object (15)>, <People: People object (19)>, <People: People object (28)>, <People: People object (31)>, <People: People object (36)>, <People: People object (37)>]>
In [55]: People.objects.filter(birthdate__gte="2012-2-20") #greater than equal to
Out[55]: <QuerySet [<People: People object (6)>, <People: People object (7)>, <People: People object (11)>, <People: People object (21)>, <People: People object (25)>, <People: People object (33)>, <People: People object (48)>]>
In [57]: People.objects.filter(name__exact="John") #exact string match. Not even half
Out[57]: <QuerySet []>

In [58]: People.objects.filter(name__exact="Jhon Doe")
Out[58]: <QuerySet [<People: People object (1)>]>
In [59]: People.objects.filter(name__startswith="Jh")
Out[59]: <QuerySet [<People: People object (1)>, <People: People object (2)>]>
In [63]: People.objects.filter(name__endswith="oe")
Out[63]: <QuerySet [<People: People object (1)>]>


In [38]: target=People.objects.get(name__startswith="Jubayer")

In [39]: target
Out[39]: Jubayer Isfar - 33 - 1971-08-03

difference between filter and get():
get returns an object and can be accessed its attributes such as name,date etc. But, filter returns a list of query. So we have
to go index by index to get the attributes of the query results:

In [42]: target=People.objects.filter(name="Jubayer Isfar")

In [43]: target
Out[43]: <QuerySet [Jubayer Isfar - 33 - 1971-08-03]>

In [45]: target[0]
Out[45]: Jubayer Isfar - 33 - 1971-08-03

for more : https://docs.djangoproject.com/en/4.2/topics/db/queries/