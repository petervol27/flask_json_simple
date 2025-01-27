import sqlite3
cars = [
    {
        "id": "1",
        "number": "123-456",
        "img": "https://platform.cstatic-images.com/in/v2/stock_photos/90884105-7fd5-4da9-8479-27e482a4e479/2b678835-3279-4de7-8047-36484d4e2900.png",
        "description": "Ford Mustang 2022",
        "urgent": True,
    },
    {
        "id": "2",
        "number": "456-789",
        "img": "https://www.cars.com/i/large/in/v2/stock_photos/1fce77f4-454e-4338-b0ed-4b7c961910b2/c9dc2064-dd42-45ec-b973-c0a27688ed16.png",
        "description": "Toyota Corolla 2002",
        "urgent": False,
    },
    {
        "id": "3",
        "number": "789-012",
        "img": "https://cars.usnews.com/static/images/Auto/izmo/i284861/2016_ford_focus_angularfront.jpg",
        "description": "Ford Focus 2015",
        "urgent": True,
    },
    {
        "id": "4",
        "number": "123-456",
        "img": "https://cfx-vrf-main-imgs.imgix.net/8/3/0/b6311870e2aaf68832d5bbd2fb5c4ccd5184f038.png?fm=webp&fit=clip&w=368&h=276",
        "description": "Honda Civic 2010",
        "urgent": True,
    },
]

users = [
    {
        "id": "1",
        "email": "admin@admin.com",
        "password": "admin123",
        "username": "Admin-Man",
    },
    {
        "id": "2",
        "email": "user@user.com",
        "password": "user123",
        "username": "User-Man",
    },
]

con = sqlite3.connect('data.db')
cur = con.cursor()
for car in cars:
    cur.execute("INSERT INTO cars(number,img,description,urgent) VALUES(?,?,?,?)",(car['number'],car['img'],car['description'],car['urgent']))
con.commit()
con.close()