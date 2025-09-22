#! /bin/bash

curl -X POST "http://localhost:8080/realms/master/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin" \
  -d "password=admin" \
  -d "grant_type=password" \
  -d "client_id=admin-cli"


# Create a new realm
curl -X POST "http://localhost:8080/admin/realms" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ3UjRJZDFWMkJvNWVoeVV2ZENROU9Zek12THZVSG9BZDQzZ0JIQTM5azZRIn0.eyJleHAiOjE3NTg1NTA5OTIsImlhdCI6MTc1ODU1MDkzMiwianRpIjoib25sdHJvOjkyYmM4NWNjLWMwMzEtNWVkNy0wOWQwLTRhMjAyYmFiNTk3ZSIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MC9yZWFsbXMvbWFzdGVyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWRtaW4tY2xpIiwic2lkIjoiZjg5YjljOTUtMjI0NC00MGYxLWIyZTktZDU4NTU0ZjEzODNmIiwic2NvcGUiOiJwcm9maWxlIGVtYWlsIn0.no7-GCzFROwUWtzJwtOHpgK7d_7RlaOE-8kHPSEOuU0aBSo5fA_I4EaK-00iN7Yjjwfxn7smNBhodTHphpemw2ZQAqup65s6SRAPpIVSpbVP5W_C4rms5LuXjsxGzm9QdjfvAIc9buGETMuyyPmd-wOcf5MlglNE5zi8VjsmobMoo338HUV8C1VmdFyqMbNMwU1AP1uGNELoz0a0qL47ftbcwtuYmmuO82vRgQdb1unkNcAXpZJmDjKK4ZFWY5JjRJ_xcCV1AB82eQ3y6syfVhUTlGOqvLyng7j2dspHpvsh9gtHS0ToftX0z3Q8I3rAf7evV5xXAw_8h1BLjpBEmw" \
  -d '{
        "realm": "lls-auth",
        "enabled": true
      }'


# Curl client

curl -X POST "http://localhost:8080/realms/lls-auth/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=lls-client" \
  -d "client_secret=XcNf6jxGiobpHryw6sd5Uc9uPkDj3wF0"
