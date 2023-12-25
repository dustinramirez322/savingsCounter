Created to track my personal savings over a course of two years.

The project is composed of:

1. Flask running a single page that:
   a. Displays a graph pulled from my grafana server
   b. Allows me to input new desposits that will be posted to my sql server
2. Reachable grafana server
3. Reachable sql server

Example page:
-------------------------------------------------------------------------


                     -----------------------------
                    |                    x .  .   |
                    |                 x .         |
                    |             x  .            |
                    |         x.           +   +  |
                    |    x.  .   +   +   +        |
                    |  x.+   +                    |
                     -----------------------------
                   .=short-term x=401k +=extra house

                       How much did you deposit?
                            |---input---|

-------------------------------------------------------------------------

Basic directory structure:
.
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── brand
│   │   ├── dist
│   │   │   ├── css
│   │   │   └── js
│   │   ├── images
│   │   └── styles
│   │       └── starter-template.css
│   └── templates
│       ├── 404.html
│       ├── index.html
│       └── layouts
│           └── base.html
├── app.py
├── notes.txt
└── sql
    ├── crud.py
    ├── database.py
    └── models.py


Example data input:
input = {'date': '2023-12-24', 'year': '2023', 'amount': '1000', 'ShortTerm': 15000.0}
