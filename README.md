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

I generated some new tokens before submitting, and the expiration time is set to 864000s so they should be usable for a while. The following tokens are also used in the Postman tests.
- Barista: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1jWW9tQmNQcThZamdReWRpaEI0TCJ9.eyJpc3MiOiJodHRwczovL2xleWlzLWNvZmZlZXNob3AudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzVlOWEwMjZhZmExMDA3MDBiNWVmMiIsImF1ZCI6ImNvZmZlZSIsImlhdCI6MTYxNDI5OTg0MywiZXhwIjoxNjE0Mzg2MjQzLCJhenAiOiJKbklxdmJGcElkdnJIMXQ0TU1KZmx4MjVhZ01YcUNLaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.dJvltYqvVdQjugSMvz03C90J-H_r1U2lnXXwPVGUrtcxhMD47tmPcGKvWxfzqk82oBL2LN26QemOpLz_DDckJ5xNX9P72ixMqoE9Ow7vG8DdjfEztzE7fEJQ7wUIYD1PZgRIHlW0uB7oqF-mP643KznfPargV263mOocA8aUuvlxcajx206z2-JUZ9xMGQwgJCePcUNYgx4aza3AzGia44gK70bJvJp9gXpAoOIBDFqUVg2-6P5b0PHgJBS51OT30hHPI_9fkHLPSQSskaeffIGUq0am8HA6SrJE4eaiSpHeaz1UANWhSWOC7fTF-f1A0xE0om1-ICItU-813gGUDQ`
- Manager: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1jWW9tQmNQcThZamdReWRpaEI0TCJ9.eyJpc3MiOiJodHRwczovL2xleWlzLWNvZmZlZXNob3AudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzVlOWU4MDY2YTZkMDA2OTQ3ZWQ3OSIsImF1ZCI6ImNvZmZlZSIsImlhdCI6MTYxNDI5OTkwMCwiZXhwIjoxNjE0Mzg2MzAwLCJhenAiOiJKbklxdmJGcElkdnJIMXQ0TU1KZmx4MjVhZ01YcUNLaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.YLBlZ4JswIu0Fb0TFVX_Pxtctj_TXUfV3l8WxTlKIIjj3EGC7O-O9Pjtvz2zU5060NSoP8n9G1zmUggOxscGeDeqAG4Xj6UIKtZWVDqCRt-_f3Wbhf4ctZUI5H8WMkPGoz5LRVJHi7lumhAd6NOY-rkrSKA9kQQFkXG791BKTIh96h75FwdpT3J3LC7j_hjJmgl2mHxg-Wv1bgo3KXyxFrVJhwb-s3SwvowWSQwQAmnM7fQ7vvEGT2NRWQCeY0z0AsPwnl3FyYzygSEhgHTZV7eBTPj65wt-V5a_s9JWe9nLrtB7oAzSW56jBEN9UcwA3j81x0xabPTLGQvdbnXj_g`