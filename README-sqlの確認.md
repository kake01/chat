D:\djangoProject>docker compose exec db bash
root@44221dfa45e4:/# psql -U postgres
psql (16.1 (Debian 16.1-1.pgdg120+1))
Type "help" for help.

postgres=# \l
List of databases
Name | Owner | Encoding | Locale Provider | Collate | Ctype | ICU Locale | ICU Rules | Access privileges  
-----------+----------+----------+-----------------+------------+------------+------------+-----------+-----------------------
chatapp | postgres | UTF8 | libc | en_US.utf8 | en_US.utf8 | | |
postgres | postgres | UTF8 | libc | en_US.utf8 | en_US.utf8 | | |
template0 | postgres | UTF8 | libc | en_US.utf8 | en_US.utf8 | | | =c/postgres +
| | | | | | | | postgres=CTc/postgres
template1 | postgres | UTF8 | libc | en_US.utf8 | en_US.utf8 | | | =c/postgres +
| | | | | | | | postgres=CTc/postgres
(4 rows)

postgres=# \c chatapp
You are now connected to database "chatapp" as user "postgres".
chatapp=# \dt
Did not find any relations.
chatapp=#
