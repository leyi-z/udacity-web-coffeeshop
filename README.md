### Leyi's Coffee Shop API



#### Backend

Before running anything, make sure that you have enerything specified in `requirements.txt` located in the directory `./backend`.



#### Frontend

The `node_modules` file is needed to run the frontend, but I did not include it in the git repository since it's a huge file. You wiil need to run the following command in the `./frontend`:
```
$ npm install
```
Then you can run the frontend with Ionic CLI
```
$ ionic serve
```



#### Database

I commented out the line `db_drop_and_create_all()` in `./backend/src/api.py`, which drops and recreates the database. You might need to uncomment it if you don't already have the database.



#### Authentication

The Auth0 setup for this api has the following configuration:
- Domain: `leyis-coffeeshop.us.auth0.com`
- Identifier: `coffee`
- Cliend ID: `JnIqvbFpIdvrH1t4MMJflx25agMXqCKh`

I created two users and you can use the following info to login:
- Barista
	- Email: `barista@gmail.com`
	- Password: `Barista&123`
- Manager
	- Email: `manager@gmail.com`
	- Password: `Manager&123`
	
This URL can be used to login and generate JWTs:
`https://leyis-coffeeshop.us.auth0.com/authorize?audience=coffee&response_type=token&client_id=JnIqvbFpIdvrH1t4MMJflx25agMXqCKh&redirect_uri=http://localhost:8100&state=STATE`

Some tokens:
- Barista: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1jWW9tQmNQcThZamdReWRpaEI0TCJ9.eyJpc3MiOiJodHRwczovL2xleWlzLWNvZmZlZXNob3AudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzVlOWEwMjZhZmExMDA3MDBiNWVmMiIsImF1ZCI6ImNvZmZlZSIsImlhdCI6MTYxNDIzMjYxMCwiZXhwIjoxNjE0MjM5ODEwLCJhenAiOiJKbklxdmJGcElkdnJIMXQ0TU1KZmx4MjVhZ01YcUNLaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.GYg1dbKMf3ZfoTFWz8CnMHRpZum8tLxhVmYHg4sYNecx3KsOYpI0mhuRd8X3uLr35b7B7iH8-P0C1fYOpGUbebrTTWhgRfkb0CjDT7dbHqivWrbsSSENgD7QLXDP2tBzlDU3L0qdf3FxqJHRCI3QaTZkaHo50OIK97gWqBF7okpMJoLPGNzystey01s4Ym3GUnRnEcHXTnPmB1adtQJoS7LpuZOwtzrph9-a1Xy6EfgLEt1j11vySOH1Z4qXTl5a8jEfzg6Bc5zrXlx7L1uuJuyD3_jYLrMOta8uiV6-dF_VJWeZnI1nr3x3CadcXhJjHScnP8eZJ7L8bgUObVaDLg`
- Manager: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1jWW9tQmNQcThZamdReWRpaEI0TCJ9.eyJpc3MiOiJodHRwczovL2xleWlzLWNvZmZlZXNob3AudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzVlOWU4MDY2YTZkMDA2OTQ3ZWQ3OSIsImF1ZCI6ImNvZmZlZSIsImlhdCI6MTYxNDIzMjczNSwiZXhwIjoxNjE0MjM5OTM1LCJhenAiOiJKbklxdmJGcElkdnJIMXQ0TU1KZmx4MjVhZ01YcUNLaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.YFs_z2XPK3mE4RAIqviqnBJgTCLjMDqAYIlZBR6saohisC7GIHFY7Vu2zeh0G398ekKvopMPeHMhsM5fcM0L6iqBPCxcsY943Fkhfu0XoHNLYdidzA1zYhr0ChFNPNaX0DCKTBR26Ik2kDkvqh71byMSLXyuXpTs5iuswFfgOjDqSQT8SNWce7mP8lUnWCsv5y9EPRkbqTEnz24ZW0xs7Bols8Q0spfxcKMzliFNInqs7vSAjqJRh-o0MLkj9NkbPzdCEK5LZGO44c6udMDlrdGa6cThdmJBnL98E-Obew5aFZctBBsaMpo4_5ozOEaz1hKVYda5BuJHaAhTQWp6xA`