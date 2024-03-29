from bs4 import BeautifulSoup
from django.db import models
from django.contrib.auth.models import User

import requests


# Django ya cuenta con una tabla de Usuario llamada User
# class User(models.Model):
#     username = models.CharField(max_length=80)
#     first_name = models.CharField(max_length=80)
#     last_name = models.CharField(max_length=80)
#     group = models.ForeignKey(Group)
#     email = models.EmailField()


# Create your models here.


class Playlister(models.Model):
    """ Define la tabla Playlister """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        null=True, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    GENERO = [
        ("H", "Hombre"),  # <- opcion
        ("M", "Mujer"),
        ("O", "Otro"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)  # VARCHAR(1)
    PAIS = [
        ('AF', 'Afganistán'),
        ('AL', 'Albania'),
        ('DE', 'Alemania'),
        ('DZ', 'Algeria'),
        ('AD', 'Andorra'),
        ('AG', 'Antigua & Barbuda'),
        ('AO', 'Angola'),
        ('AI', 'Anguilla'),
        ('AQ', 'Antárctica'),
        ('AN', 'Antillas Holandesas'),
        ('SA', 'Arabia Saudita'),
        ('AM', 'Armenia'),
        ('AR', 'Argentina'),
        ('AW', 'Aruba'),
        ('AT', 'Austria'),
        ('AU', 'Australia'),
        ('AZ', 'Azerbaiyán'),
        ('BS', 'Bahamas'),
        ('BB', 'Barbados'),
        ('BH', 'Baréin'),
        ('BD', 'Bangladesh'),
        ('BE', 'Bélgica'),
        ('BZ', 'Belice'),
        ('BJ', 'Benín'),
        ('BM', 'Bermuda'),
        ('BT', 'Bhutan'),
        ('BY', 'Bielorrusia'),
        ('BO', 'Bolivia'),
        ('BW', 'Botswana'),
        ('BV', 'Bouvet'),
        ('BA', 'Bosnia y Herzegovina'),
        ('BR', 'Brasil'),
        ('BN', 'Brunei Darussalam'),
        ('BG', 'Bulgaria'),
        ('BF', 'Burkina Faso'),
        ('BI', 'Burundi'),
        ('KH', 'Camboya'),
        ('CM', 'Camerún'),
        ('CA', 'Canadá'),
        ('QA', 'Catar'),
        ('TD', 'Chad'),
        ('CL', 'Chile'),
        ('CN', 'China'),
        ('CY', 'Chipre'),
        ('CO', 'Colombia'),
        ('KM', 'Comoras'),
        ('CG', 'Congo'),
        ('KP', 'Corea del Sur'),
        ('CI', 'Costa de Marfil'),
        ('CR', 'Costa Rica'),
        ('CU', 'Cuba'),
        ('HR', 'Croacia'),
        ('DK', 'Dinamarca'),
        ('EC', 'Ecuador'),
        ('EG', 'Egipto'),
        ('AE', 'Emiratos Árabes Unidos'),
        ('ER', 'Eritrea'),
        ('SK', 'Eslovaquia'),
        ('SI', 'Eslovenia'),
        ('ES', 'España'),
        ('US', 'Estados Unidos de América'),
        ('EE', 'Estonia'),
        ('ET', 'Etioppia'),
        ('PH', 'Filipinas'),
        ('FI', 'Finlandia'),
        ('FJ', 'Fiji'),
        ('FR', 'Francia'),
        ('GA', 'Gabón'),
        ('GM', 'Gambia'),
        ('GE', 'Georgia'),
        ('GH', 'Ghana'),
        ('GI', 'Gibraltar'),
        ('GD', 'Granada'),
        ('GR', 'Grecia'),
        ('GL', 'Groenlandia'),
        ('GU', 'Guam'),
        ('GF', 'Guayana Francesa'),
        ('GT', 'Guatemala'),
        ('GN', 'Guinea'),
        ('GQ', 'Guinea Ecuatorial '),
        ('HT', 'Haití'),
        ('HN', 'Honduras'),
        ('HK', 'Hong Kong'),
        ('HU', 'Hungría'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('IR', 'Iran'),
        ('IE', 'Irlanda'),
        ('IS', 'Islandia'),
        ('MS', 'Isla de Monserrat'),
        ('CX', 'Isla de Navidad'),
        ('NF', 'Isla Norfolk'),
        ('KY', 'Islas Caimán'),
        ('CC', 'Islas Cocos'),
        ('CK', 'Islas Cook'),
        ('FO', 'Islas Faroe'),
        ('MH', 'Islas Marshall'),
        ('PN', 'Islas Pitcairn'),
        ('SB', 'Islas Salomón'),
        ('TC', 'Islas Turcas y Caicos'),
        ('IL', 'Israel'),
        ('IT', 'Italia'),
        ('JM', 'Jamaica'),
        ('JP', 'Japón'),
        ('JO', 'Jordan'),
        ('KZ', 'Kazajistán'),
        ('KE', 'Kenya'),
        ('KG', 'Kirguistán'),
        ('KI', 'Kiribati'),
        ('KW', 'Kuwait'),
        ('LA', 'LAOS'),
        ('LS', 'Lesoto'),
        ('LV', 'Letonia'),
        ('LB', 'Líbano'),
        ('LR', 'Liberia'),
        ('LY', 'Libia'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lituania'),
        ('LU', 'Luxemburgo'),
        ('MO', 'Macao'),
        ('MG', 'Madagascar'),
        ('MW', 'Malaui'),
        ('MY', 'Malasia'),
        ('MV', 'Maldivas'),
        ('ML', 'Malí'),
        ('MT', 'Malta'),
        ('FK', 'Malvinas'),
        ('DM', 'Mancomunidad de Dominica'),
        ('MQ', 'Martinica'),
        ('MA', 'Marruecos'),
        ('MR', 'Mauritania'),
        ('MU', 'Mauricio'),
        ('YT', 'Mayotte'),
        ('MX', 'México'),
        ('FM', 'Micronesia'),
        ('MD', 'Moldavia'),
        ('MC', 'Mónaco'),
        ('MN', 'Mongolia'),
        ('MZ', 'Mozambique'),
        ('MM', 'Myanmar'),
        ('NA', 'Namibia'),
        ('NR', 'Nauru'),
        ('NP', 'Nepal'),
        ('NI', 'Nicaragua'),
        ('NU', 'Niue'),
        ('NE', 'Níger'),
        ('NG', 'Nigeria'),
        ('NO', 'Noruega'),
        ('NC', 'Nueva Caledonia'),
        ('NZ', 'Nueva Zelanda'),
        ('OM', 'Oman'),
        ('NL', 'Países Bajos'),
        ('PK', 'Pakistán'),
        ('PW', 'Palaos'),
        ('PA', 'Panamá'),
        ('PG', 'Papúa Nueva Guinea'),
        ('PY', 'Paraguay'),
        ('PE', 'Perú'),
        ('PF', 'Polinesia Francesa'),
        ('PL', 'Polonia'),
        ('PT', 'Portugal'),
        ('PR', 'Puerto Rico'),
        ('CV', 'República de Cabo Verde'),
        ('CZ', 'República Checa'),
        ('DJ', 'República de Djibouti'),
        ('DO', 'República Dominicana'),
        ('CF', 'República Centroafricana'),
        ('GB', 'Reino Unido'),
        ('RW', 'Ruanda'),
        ('RO', 'Rumania'),
        ('RU', 'Rusia'),
        ('KN', 'Saint Kitts y Nevis'),
        ('EH', 'Sahara Occidental'),
        ('AS', 'Samoa Americana'),
        ('SM', 'San Marino'),
        ('PM', 'San Pedro y Miquelón'),
        ('VC', 'San Vicente y las Granadinas'),
        ('SH', 'Santa Helena'),
        ('LC', 'Santa Lucía'),
        ('ST', 'Santo Tomé y Príncipe'),
        ('SN', 'Senegal'),
        ('SO', 'Somalia'),
        ('SE', 'Suecia'),
        ('SC', 'Seychelles'),
        ('SL', 'Sierra Leona'),
        ('SG', 'Singapur'),
        ('SY', 'Siria'),
        ('LK', 'Sri Lanka'),
        ('SZ', 'Suazilandia'),
        ('CH', 'Suiza'),
        ('SD', 'Sudán'),
        ('SR', 'Surinam'),
        ('SV', 'El Salvador'),
        ('TH', 'Tailandia'),
        ('TJ', 'Tayikistán'),
        ('TG', 'Togo'),
        ('TK', 'Tokelau'),
        ('TM', 'Turkmenistán'),
        ('TN', 'Túnez'),
        ('TO', 'Tonga'),
        ('TP', 'Timor Oriental'),
        ('TR', 'Turquía'),
        ('TT', 'Trinidad & Tobago'),
        ('TV', 'Tuvalu'),
        ('TW', 'Taiwán'),
        ('TZ', 'Tanzania'),
        ('UA', 'Ucrania'),
        ('UG', 'Uganda'),
        ('UY', 'Uruguay'),
        ('UZ', 'Uzbekistán'),
        ('VA', 'Vaticano'),
        ('VE', 'Venezuela'),
        ('VN', 'Vietnam'),
        ('VU', 'Vanuatu'),
        ('WS', 'Samoa'),
        ('YE', 'Yemen'),
        ('YU', 'Yugoslavia'),
        ('ZA', 'Sudáfrica'),
        ('ZM', 'Zambia'),
        ('ZR', 'Zaire'),
        ('ZW', 'Zimbabue'),
    ]
    pais = models.CharField(max_length=2, choices=PAIS, null=True, blank=True)  # VARCHAR(2)
    def __str__(self):
        return self.user.username


class Playlist(models.Model):
    """ Define la tabla Playlist"""
    nombre = models.CharField(max_length=145)
    playlister = models.ForeignKey(Playlister, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=256)
    canciones = models.IntegerField(default=0)
    MOOD = [
        ("Happy", "Happy"),
        ("Chill", "Chill"),
        ("Romantic", "Romantic"),
        ("Blue", "Blue"),
    ]
    mood = models.CharField(max_length=20, choices=MOOD, null=True, blank=True)  # VARCHAR(2)
    tag1 = models.CharField(max_length=256, null=True, blank=True)
    tag2 = models.CharField(max_length=256, null=True, blank=True)
    PLATAFORMA = [
        ("DZ", "Deezer"),
        ("SP", "Spotify"),
        ("TD", "Tidal"),
    ]
    plataforma = models.CharField(max_length=2, choices=PLATAFORMA, null=True, blank=True)  # VARCHAR(2)
    link = models.CharField(max_length=100)
    url_cover = models.CharField(max_length=500)


    def __str__(self):
        return str(self.nombre)
        
    @property
    def url_cover(self):
        """ Obtiene la url de la portada de la playlist"""
        url_image = ""
        if self.plataforma == "SP":
            html = requests.get(self.link).text
            soup = BeautifulSoup(html, 'html.parser')
            meta = soup.find(property = "og:image")
            url_image = meta.attrs["content"]

        elif self.plataforma == "DZ":
            html = requests.get(self.link).text
            soup = BeautifulSoup(html, 'html.parser')
            meta = soup.find(property = "og:image")
            url_image = meta.attrs["content"]
        
        return url_image

    @property
    def url_playlist(self):
        """ Obtiene la url de la playlist"""
        url = ""
        if self.plataforma == "SP":
            id_spotify = self.link.split("?")[0].split("/")[-1]
            url = f"https://open.spotify.com/embed/playlist/{id_spotify}"

        elif self.plataforma == "DZ":
            html = requests.get(self.link).text
            soup = BeautifulSoup(html, 'html.parser')
            og_deezer = soup.find(property = "og:url")
            url_deezer = og_deezer.attrs["content"]
            id_deezer = url_deezer.split("/")[-1]
            url = f"https://widget.deezer.com/widget/dark/playlist/{id_deezer}"

        elif self.plataforma == "TD":
            id_spotify = self.link.split("/")[-1]
            url = f"https://embed.tidal.com/playlists/{id_spotify}?layout=gridify"

        return url