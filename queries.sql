CREATE TABLE IF NOT EXISTS "auth_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(150) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "email" varchar(254) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" datetime NOT NULL,
    "last_name" varchar(150) NOT NULL
);

CREATE TABLE IF NOT EXISTS "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);

CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");